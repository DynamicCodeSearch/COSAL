import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.blocks import code_block, contest_meta_block
from mos.helpers import contexter
from mos.search.tree import java_tree, py_tree
from mos.search_store import code_store
from utils import logger, cache

import sqlite3
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
DB_PATH = os.path.join(properties.CONFIG.CODESEER_HOME, "atcoder", "java-python-clones.db")


def get_data_store():
  return code_store.CodeStore()


def get_file_store():
  return code_store.FileStore()


def update_ast(block):
  if block.language == properties.LANGUAGE_JAVA:
    code_ast = java_tree.get_java_tree(block.code)
  elif block.language == properties.LANGUAGE_PYTHON:
    code_ast = py_tree.get_py_tree(block.code, extract_first_func=False)
  else:
    raise RuntimeError("Unsupported language: '%s'" % block.language)
  block.ast = code_ast
  return block


def update_tokens(block):
  if block.language == properties.LANGUAGE_JAVA:
    tokens = contexter.tokenize_java_function(block.code)
  elif block.language == properties.LANGUAGE_PYTHON:
    tokens = contexter.tokenize_py_function(block.code)
  else:
    raise RuntimeError("Unsupported language: '%s'" % block.language)
  if not tokens or len(tokens) == 0:
    block.contextual_tokens = None
  else:
    block.contextual_tokens = tokens
  return block


def get_language(lang):
  if lang == 'python':
    return properties.LANGUAGE_PYTHON
  elif lang == 'java':
    return properties.LANGUAGE_JAVA
  else:
    raise RuntimeError('Unsupported lang: %s' % lang)


def make_code_block(record):
  block = code_block.CodeBlock()
  block.language = get_language(record[8])
  block.source_file = record[6]
  block.is_file = True
  block.code = record[12]
  block.contest_meta = contest_meta_block.ContestMeta()
  block.contest_meta.submission_id = record[0]
  block.contest_meta.contest_type = record[2]
  block.contest_meta.contest_id = record[3]
  block.contest_meta.problem_id = record[4]
  block.contest_meta.code_size = record[9]
  block.contest_meta.exec_time = record[10]
  return block


def get_all_records():
  conn = sqlite3.connect(DB_PATH)
  n_records = conn.execute("SELECT COUNT(*) FROM submissions").fetchall()[0][0]
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM submissions")
  blocks = []
  index = 0
  missed_asts = 0
  missed_tokens = 0
  print(n_records)
  data_store = get_data_store()
  data_store.drop_code_blocks()
  for row in cursor:
    index += 1
    if index % 1000 == 0:
      LOGGER.info("Processing %d/%d. Missed ASTs: %d. Missed Tokens: %d ... "  % (index, n_records, missed_asts, missed_tokens))
    block = make_code_block(row)
    if block.contest_meta.code_size > 6000:
      continue
    update_ast(block)
    if not block.ast:
      missed_asts += 1
    update_tokens(block)
    if not block.contextual_tokens:
      missed_tokens += 1
    data_store.save_code_block(block)
  LOGGER.info("Missed ASTs: %d/%d ... " % (missed_asts, n_records))
  LOGGER.info("Missed Tokens: %d/%d ... " % (missed_tokens, n_records))
  return blocks


# Preprocess for method level code blocks
def process_result_set(result_set):
  contest_meta = contest_meta_block.ContestMeta()
  contest_meta.submission_id = result_set[0]
  contest_meta.contest_type = result_set[2]
  contest_meta.contest_id = result_set[3]
  contest_meta.problem_id = result_set[4]
  contest_meta.code_size = result_set[9]
  contest_meta.exec_time = result_set[10]

  block = code_block.CodeBlock()
  block.contest_meta = contest_meta
  block.language = properties.LANGUAGE_PYTHON
  block.package_name = os.path.join("C%d.P%d" % (contest_meta.contest_id, contest_meta.problem_id))
  block.source_file = os.path.join(properties.CONFIG.get_python_projects_home(),
                                   os.path.join(*block.package_name.split(".")), result_set[6])
  block.project_lang_folder = properties.CONFIG.get_python_projects_home()
  block.project_source_path = properties.CONFIG.get_projects_home()
  block.is_file = True
  block.code = result_set[12]
  return block


def get_all_py_records():
  cache.delete_folder_contents(properties.CONFIG.get_python_projects_home())
  get_file_store().delete_all_file_blocks(language=properties.LANGUAGE_PYTHON)
  conn = sqlite3.connect(DB_PATH)
  param = ("python", )
  n_records = conn.execute("SELECT COUNT(*) FROM submissions WHERE language_code=?", param).fetchall()[0][0]
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM submissions WHERE language_code = ?", param)
  blocks = []
  index = 0
  for row in cursor:
    index += 1
    if index % 1000 == 0:
      LOGGER.info("Processing python %d/%d ..." % (index, n_records))
    block = process_result_set(row)
    parent_folder = cache.get_parent_folder(block.source_file)
    cache.mk_package(parent_folder)
    cache.write_file(block.source_file, block.code.encode('utf-8'))
    get_file_store().save_file_block(block)


def re_update_asts():
  file_store = code_store.CodeStore()
  fields = ["uid", "code", "language"]
  file_blocks = file_store.get_code_blocks(fields=fields)
  index = 0
  n_file_blocks = file_store.count_code_blocks()
  for fb in file_blocks:
    if index % 100 == 0:
      LOGGER.info("Processing %d/%d ... " % (index + 1, n_file_blocks))
    language = fb["language"]
    code = fb["code"]
    # print(code)
    code_ast = None
    try:
      if language == properties.LANGUAGE_JAVA:
        code_ast = java_tree.get_java_tree(code)
      elif language == properties.LANGUAGE_PYTHON:
        code_ast = py_tree.get_py_tree(code, extract_first_func=False)
      else:
        raise RuntimeError("Unsupported language: '%s'" % language)
      if code_ast:
        code_ast = str(code_ast.to_bson())
        file_store.update_code_block(fb["uid"], {"ast": code_ast})
    except Exception as e:
      LOGGER.info("Error in %d/%d. %s ... " % (index + 1, n_file_blocks, e.message))
    index += 1



if __name__ == "__main__":
  # get_all_py_records()
  # get_all_records()
  re_update_asts()
