import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import java_parse_utils
from mos.search_store.code_store import CodeStore
from mos.search.tree import java_tree, py_tree
from utils import logger, cache

import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_code_store():
  return CodeStore()


def make_java_key(code_block_db):
  code = code_block_db["code"]
  func_ast = java_tree.TreeVisitor.get_first_method_node(java_tree.parse_java(code, wrap_class=True))
  if func_ast is None:
    return None
  class_name = code_block_db["parentClassName"]
  func_name = func_ast.name
  ret_name = func_ast.return_type.name if func_ast.return_type else "void"
  parameters = ",".join([param.type.name for param in func_ast.parameters])
  key = "%s.%s(%s)->%s" % (class_name, func_name, parameters, ret_name)
  return key


def make_py_key(code_block_db):
  code = code_block_db["code"]
  func_ast = py_tree.get_ast(code, extract_first_func=True)
  if func_ast is None:
    return None
  class_name = code_block_db.get("parentClassName", None)
  func_name = func_ast.name
  args = [arg.id for arg in func_ast.args.args]
  if func_ast.args.vararg:
    args.append(func_ast.args.vararg)
  if func_ast.args.kwarg:
    args.append(func_ast.args.kwarg)
  args = ",".join(args)
  key = "%s(%s)" % (func_name, args)
  if class_name:
    key = "%s.%s" % (class_name, key)
  return key


def _update_function_keys():
  store = get_code_store()
  fields = ["uid", "language", "code", "parentClassName", "funcKey"]
  code_block_dbs = store.get_code_blocks(fields=fields, isMethod=True)
  n_code_blocks = store.count_code_blocks(isMethod=True)
  for i, code_block_db in enumerate(code_block_dbs):
    if i % 1000 == 0:
      LOGGER.info("Processing CodeBlock %d/%d ... " % (i + 1, n_code_blocks))
    if code_block_db.get("funcKey", None):
      continue
    lang = code_block_db["language"]
    key = None
    if lang == properties.LANGUAGE_JAVA:
      key = make_java_key(code_block_db)
    elif lang == properties.LANGUAGE_PYTHON:
      key = make_py_key(code_block_db)
    if key:
      store.update_code_block(code_block_db["uid"], {"funcKey": key})


def make_main_file_name_for_java(code_block):
  main_class_name = java_parse_utils.get_main_class_name(code_block["code"])
  contest_meta = code_block["contestMeta"]
  if main_class_name is None:
    return None
  return os.path.join(properties.CONFIG.get_java_projects_home(), "C%d" % contest_meta.get("contestId", 0),
                      "P%d" % contest_meta.get("problemId", 0), "S%d" % contest_meta["submissionId"],
                      "%s.java" % main_class_name)


def make_main_file_name_for_py(code_block):
  contest_meta = code_block["contestMeta"]
  return os.path.join(properties.CONFIG.get_python_projects_home(), "C%d" % contest_meta.get("contestId", 0),
                      "P%d" % contest_meta.get("problemId", 0), "%d.py" % contest_meta["submissionId"])


def _update_file_path_in_code_blocks():
  store = get_code_store()
  fields = ["uid", "language", "contestMeta", "code"]
  code_block_dbs = store.get_code_blocks(fields=fields)
  n_code_blocks = store.count_code_blocks()
  for i, code_block_db in enumerate(code_block_dbs):
    if i % 100 == 0:
      LOGGER.info("Updating file name for %d/%d ... " % (i + 1, n_code_blocks))
    file_name = None
    if code_block_db["language"] == properties.LANGUAGE_JAVA:
      file_name = make_main_file_name_for_java(code_block_db)
    elif code_block_db["language"] == properties.LANGUAGE_PYTHON:
      file_name = make_main_file_name_for_py(code_block_db)
    if file_name:
      store.update_code_block(code_block_db["uid"], {"sourceFile": cache.get_repo_local_path(file_name)})


def test():
  uid = "fc2d324077814ccf8bae74a766c1ed02"
  code = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt")
  code_block_db = {
    "code": code,
    # "parentClassName": "Main"
  }
  print(make_py_key(code_block_db))
  # code_block_db = get_code_store().fetch_code_block(uid, projections={"ast":0, "contextualTokens":0, "comments": 0, "imports": 0})
  # make_java_key(code_block_db)


if __name__ == "__main__":
  # _update_function_keys()
  _update_file_path_in_code_blocks()

