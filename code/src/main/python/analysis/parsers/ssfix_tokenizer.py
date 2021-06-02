import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.blocks import block_utils
from analysis.helpers import constants as a_consts
from analysis.helpers import ast_utils, execution_utils
from analysis.parsers import arg_parser, parser
from utils import cache, logger
from store import mongo_store, elastic_store
import properties

import ast
import tokenize
import StringIO


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))

TOKEN_VARIABLE = "$v"
TOKEN_NON_PY_METHODS = "$m"
TOKEN_NON_PY_FIELDS = "$m"
TOKEN_LITERAL_STRING = "$ls$"
TOKEN_LITERAL_NUMBER = "$ln$"
TOKEN_LITERAL_BOOLEAN = "$lb$"


def get_token_store():
  if properties.STORE == "mongo":
    return mongo_store.TokenStore()
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def get_elastic_store():
  return elastic_store.TokenStore()


class TokenizerVisitor(parser.Traveller):
  TOKEN_VARIABLE_PRE = "__SLACC_v__"
  TOKEN_NON_PY_METHODS_PRE = "__SLACC_m__"
  TOKEN_NON_PY_FIELDS_PRE = "__SLACC_m__"

  def __init__(self, source_code, variable_map):
    parser.Traveller.__init__(self)
    self.source_code = source_code
    self.variable_map = variable_map
    self.tree = ast_utils.parse(self.source_code, use_ast_tokens=True)

  def is_default_py_type(self, name):
    if name not in self.variable_map:
      return False
    var = self.variable_map[name]
    if not var.types:
      return True
      # return False
    for var_type in var.types:
      class_name = type(var_type).__name__
      if class_name in ["CustomType", "BaseType"]:
        return False
    return False

  def get_parsed_code(self):
    return ast_utils.convert_ast_to_code(self.tree)

  def parse(self):
    # ast_utils.parse_print(self.tree)
    meta = {}
    if self.tree:
      self.visit(self.tree, meta)

  @staticmethod
  def get_base_caller(node):
    if isinstance(node, ast.Name):
      return node.id
    elif hasattr(node, "value"):
      return TokenizerVisitor.get_base_caller(node.value)
    elif hasattr(node, "func"):
      return TokenizerVisitor.get_base_caller(node.func)
    else:
      return None

  @staticmethod
  def set_base_caller(node):
    if isinstance(node, ast.Name):
      node.id = TokenizerVisitor.TOKEN_VARIABLE_PRE
    elif hasattr(node, "value"):
      return TokenizerVisitor.get_base_caller(node.value)
    elif hasattr(node, "func"):
      return TokenizerVisitor.get_base_caller(node.func)

  def visit_Attribute(self, node, meta):
    # print(ast_utils.convert_ast_to_code(node))
    base_value = TokenizerVisitor.get_base_caller(node.value)
    is_default_py_type = True if base_value and self.is_default_py_type(base_value) else False
    self.generic_visit(node, meta)
    if not is_default_py_type:
      node.attr = TokenizerVisitor.TOKEN_NON_PY_FIELDS_PRE
    # TokenizerVisitor.set_base_caller(node.value)
    # ast_utils.parse_print(node)
    # print(ast_utils.convert_ast_to_code(node))

  def visit_Call(self, node, meta):
    # ast_utils.parse_print(node)
    base_value = TokenizerVisitor.get_base_caller(node.func)
    is_default_py_type = True if base_value and self.is_default_py_type(base_value) else False
    self.generic_visit(node, meta)
    if not is_default_py_type and hasattr(node, "attr"):
      node.attr = TokenizerVisitor.TOKEN_NON_PY_FIELDS_PRE
    # TokenizerVisitor.set_base_caller(node.func)
    # ast_utils.parse_print(node)
    # print(ast_utils.convert_ast_to_code(node))
    # exit()

  def visit_Name(self, node, meta):
    self.generic_visit(node, meta)
    if node.id in self.variable_map:
      node.id = TokenizerVisitor.TOKEN_VARIABLE_PRE


def infer_variable_types(func_str):
  parsed = arg_parser.VariableVisitor(source_code=func_str)
  parsed.parse_pytype()
  func_name = ast_utils.get_func_name(func_str)
  scope_name = "%s%s%s" % (a_consts.ROOT_SCOPE, a_consts.SCOPE_SEPARATOR, func_name)
  variables = {}
  for n in parsed.scope_variable_map.keys():
    if str(n) == scope_name:
      variables = parsed.scope_variable_map[n]
  return variables


def get_token_generator(code_snippet):
    return tokenize.generate_tokens(StringIO.StringIO(code_snippet).readline)


def is_numeric(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


def tokenize_string(s):
  if s == TokenizerVisitor.TOKEN_VARIABLE_PRE:
    return TOKEN_VARIABLE
  elif s == TokenizerVisitor.TOKEN_NON_PY_METHODS_PRE:
    return TOKEN_NON_PY_METHODS
  elif s == TokenizerVisitor.TOKEN_NON_PY_FIELDS_PRE:
    return TOKEN_NON_PY_FIELDS
  elif s in ['True', 'False']:
    return TOKEN_LITERAL_BOOLEAN
  elif len(s) > 1 and s[0] == s[-1] and s[0] in ['"', '\'']:
    return TOKEN_LITERAL_STRING if " " in s else "\"%s\"" % s[1:-1]
  elif is_numeric(s):
    return TOKEN_LITERAL_NUMBER
  else:
    return s.strip()


def get_tokens(func_body, token_size):
  variables = infer_variable_types(func_body)
  func_stmts = ast_utils.get_function_body_as_str(func_body, as_lst=True)
  token_groups = []
  for stmt in func_stmts:
    # print("*****")
    # print(stmt)
    visitor = TokenizerVisitor(stmt, variables)
    visitor.parse()
    # print(visitor.get_parsed_code())
    # exit()
    parsed_stmt = visitor.get_parsed_code()
    token_gen = get_token_generator(parsed_stmt)
    tokens = []
    for token_num, token, start, end, line in token_gen:
      tokenized = tokenize_string(token)
      if len(tokenized) > 0:
        tokens.append(tokenized)
    if len(tokens) <= token_size:
      token_groups.append(tokens[:])
    else:
      for i in range(len(tokens) - token_size):
        token_groups.append(tokens[i: i + token_size])
  return token_groups


def get_hash_key(function_body):
  return hash(function_body.strip())


def index_tokens():
  _STORE = get_token_store()
  tokens = _STORE.get_tokens()
  els = get_elastic_store()
  els.create_index(delete_old=True)
  els.index_documents(tokens)


def tokenize_function(gen_func_meta, token_size):
  tokens = get_tokens(gen_func_meta.body, token_size)
  if not tokens:
    return
  hash_key = get_hash_key("$$".join(["@@".join(token_group) for token_group in tokens]))
  token_json = {
    "name": gen_func_meta.name,
    "tokens": tokens,
    "hash_key": hash_key,
    "body": ast_utils.get_function_body_as_str(gen_func_meta.body)
  }
  get_token_store().save_tokens(token_json)


def tokenize_from_db():
  token_size = properties.TOKEN_SIZE
  index = 0
  for function_metadata in execution_utils.load_generated_functions_from_db():
    index += 1
    LOGGER.info("Processing function '%d' ... " % index)
    gen_func_meta = block_utils.from_generated_function_bson(function_metadata)
    tokenize_function(gen_func_meta, token_size)


def test():
  file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt"
  contents = cache.read_file(file_path)
  print(get_tokens(contents, properties.TOKEN_SIZE))


def _main():
  # tokenize_from_db()
  index_tokens()


if __name__ == "__main__":
  _main()
  # tokenize_functions_from_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt")
