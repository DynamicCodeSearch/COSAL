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
from mos.search_store.code_store import CodeStore, FileStore
from utils import cache, logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
FILE_STORE = FileStore()
CODE_STORE = CodeStore()


def get_generic_ast(func, extract_first_func=False):
  try:
    return py_tree.get_py_tree(func.code, extract_first_func=extract_first_func)
  except Exception:
    # error_content = "Error: \n%s" % traceback.format_exc()
    # LOGGER.error(error_content)
    return None


def get_context_tokens(func):
  # func_body = ast_utils.get_function_body_as_str(func.code)
  # func_name = ast_utils.get_func_name(func.code)
  # if not func_body:
  #   func_body = func.code
  tokens = contexter.tokenize_func_body(func.code)
  # if func_name and not func_name.startswith(constants.FUNCTION_PREFIX):
  #   tokens = tokens.union(contexter.tokenize_string(func_name))
  if func.parent_class_name and not func.parent_class_name.startswith(constants.PERMUTATED_PREFIX) \
          and not func.parent_class_name.startswith(constants.GENERATED_PREFIX):
    tokens = tokens.union(contexter.tokenize_string(func.parent_class_name))
  if func.comments:
    tokens = tokens.union(contexter.tokenize_string(func.comments))
  if not tokens:
    return None
  return tokens


class MethodExtractor(parser.Traveller):
  def __init__(self, file_path):
    parser.Traveller.__init__(self)
    self.file_path = file_path
    file_bson = FILE_STORE.get_file_block(file_path)
    self.file_block = code_block.CodeBlock.from_bson(file_bson) if file_bson else None
    contents = cache.read_file(file_path)
    self.tree = ast_utils.parse(contents, use_ast_tokens=True)
    self.function_blocks = []
    if self.tree and self.file_block:
      self.visit(self.tree)

  def get_function_blocks(self):
    return self.function_blocks

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
    func.source_file = self.file_block.source_file
    func.code = ast_utils.format_code(cleaned_source_code)
    if len(comments) > 0:
      func.comments = "\n".join(comments)
    func.is_method = True
    if meta and "class_name" in meta:
      func.parent_class_name = meta["class_name"]
    func.project_source_path = self.file_block.project_source_path
    func.project_lang_folder = self.file_block.project_lang_folder
    func.ast = get_generic_ast(func, extract_first_func=True)
    func.contextual_tokens = get_context_tokens(func)
    # try:
    #
    # except Exception:
    #   print(ast_utils.get_function_body_as_str(func.code))
    #   exit(0)
    func.contest_meta = self.file_block.contest_meta
    self.function_blocks.append(func)
    self.generic_visit(node, meta)


def extract_methods_for_file(file_path):
  CODE_STORE.delete_code_blocks_from_file(file_path)
  extractor = MethodExtractor(file_path)
  func_blocks = extractor.function_blocks
  if not func_blocks:
    file_block = extractor.file_block
    if file_block:
      file_block.ast = get_generic_ast(file_block, extract_first_func=False)
      file_block.contextual_tokens = get_context_tokens(file_block)
      CODE_STORE.save_code_block(file_block)
  else:
    for func in extractor.function_blocks:
      CODE_STORE.save_code_block(func)


def extract_methods():
  index = 0
  source_files = cache.list_files(properties.CONFIG.get_python_projects_home(), check_nest=True, is_absolute=True,
                                  extension=".py", ignores=["__init__.py"])
  for source_file in source_files:
    if index % 100 == 0:
      LOGGER.info("Processing file %d/%d ... " % (index + 1, len(source_files)))
    extract_methods_for_file(source_file)
    index += 1


if __name__ == "__main__":
  extract_methods()
