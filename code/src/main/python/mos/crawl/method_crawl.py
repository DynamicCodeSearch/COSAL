import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.parsers import parser
from analysis.helpers import ast_utils, constants
from mos.blocks import code_block
from mos.helpers import contexter
from mos.search.tree import py_tree
from mos.search_store.code_store import CodeStore
from utils import cache, logger
import properties

import traceback


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
CODE_STORE = CodeStore()


class MethodVisitor(parser.Traveller):
  def __init__(self, file_path):
    parser.Traveller.__init__(self)
    self.file_path = file_path
    self.code_blocks = []
    file_contents = cache.read_file(self.file_path)
    self.tree = ast_utils.parse(file_contents, use_ast_tokens=True)
    if self.tree:
      self.visit(self.tree)

  def get_code_blocks(self):
    return self.code_blocks

  def visit_ClassDef(self, node, meta):
    meta = {"class_name": str(node.name)}
    self.generic_visit(node, meta)

  def visit_FunctionDef(self, node, meta):
    asttokens_obj = getattr(self.tree, "asttokens_obj", None)
    source_code = ast_utils.convert_ast_to_code(node, asttokens_obj)
    comments = ast_utils.get_comments(source_code)
    doc_string = ast_utils.get_docstring(node)
    if doc_string:
      comments.append(doc_string)
    cleaned_source_code = ast_utils.remove_comments_and_docstrings(source_code)
    func = code_block.CodeBlock()
    func.language = properties.LANGUAGE_PYTHON
    func.source_file = self.file_path
    func.code = ast_utils.format_code(cleaned_source_code)
    if len(comments) > 0:
      func.comments = "\n".join(comments)
    func.is_method = True
    if meta and "class_name" in meta:
      func.parent_class_name = meta["class_name"]
    func.project_py_folder = properties.CONFIG.get_python_projects_home()
    self.code_blocks.append(func)
    self.generic_visit(node, meta)


def update_context_tokens(func):
  func_body = ast_utils.get_function_body_as_str(func.code)
  func_name = ast_utils.get_func_name(func.code)
  tokens = contexter.tokenize_func_body(func_body)
  if not func_name.startswith(constants.FUNCTION_PREFIX):
    tokens = tokens.union(contexter.tokenize_string(func_name))
  if func.parent_class_name and not func.parent_class_name.startswith(constants.PERMUTATED_PREFIX) \
          and not func.parent_class_name.startswith(constants.GENERATED_PREFIX):
    tokens = tokens.union(contexter.tokenize_string(func.parent_class_name))
  if func.comments:
    tokens = tokens.union(contexter.tokenize_string(func.comments))
  if not tokens:
    return False
  func.contextual_tokens = tokens
  return True


def get_generic_ast(func):
  try:
    node = py_tree.get_py_tree(func.code, extract_first_func=True)
    if node:
      func.ast = node.to_bson()
      return True
    return False
  except Exception:
    error_content = "Error: \n%s" % traceback.format_exc()
    LOGGER.error(error_content)
    LOGGER.error(func.code)
    return False


def generate_for_file(file_path):
  LOGGER.info("Processing file '%s' ... " % cache.get_repo_local_path(file_path))
  CODE_STORE.delete_code_blocks_from_file(file_path)
  visitor = MethodVisitor(file_path)
  code_blocks = visitor.get_code_blocks()
  LOGGER.info("Updating contexts and AST for '%d' functions ... " % len(code_blocks))
  contexts_found = asts_found = 0
  for func in code_blocks:
    if update_context_tokens(func):
      contexts_found += 1
    if get_generic_ast(func):
      asts_found += 1
    CODE_STORE.save_code_block(func)
  LOGGER.info("Contexts found for %d/%d ... " % (contexts_found, len(code_blocks)))
  LOGGER.info("AST found for %d/%d ... " % (contexts_found, len(code_blocks)))


def _test_single():
  file_contents = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt")
  tree = ast_utils.parse(file_contents, use_ast_tokens=True)
  if not tree:
    return
  func_node = tree.body[0]
  asttokens_obj = getattr(tree, "asttokens_obj", None)
  source_code = ast_utils.convert_ast_to_code(func_node, asttokens_obj)
  comments = ast_utils.get_comments(source_code)
  doc_string = ast_utils.get_docstring(func_node)
  if doc_string:
    comments.append(doc_string)
  print(comments)
  print(ast_utils.remove_comments_and_docstrings(source_code))
  exit()
  # source_match.GetSource(tree, file_contents)
  # print(tree.matcher.GetSource())


def _test_multi():
  file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/SystemLibs/string.py"
  generate_for_file(file_path)
  # visitor = MethodVisitor(file_path)
  # print(visitor.get_code_blocks()[0])


if __name__ == "__main__":
  _test_multi()
