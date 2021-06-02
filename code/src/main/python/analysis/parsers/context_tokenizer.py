import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.blocks import block_utils
from analysis.helpers import ast_utils, constants, execution_utils
from utils import cache, logger
from store import mongo_store, elastic_store
from mos.helpers import contexter
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_token_store():
  if properties.STORE == "mongo":
    return mongo_store.TokenStore()
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def get_elastic_store():
  return elastic_store.ContextStore()


def get_hash_key(function_body):
  return hash(function_body.strip())


def tokenize_functions_from_file(file_path):
  file_name = cache.get_file_name(file_path)
  if not file_name.startswith(constants.GENERATED_PREFIX):
    LOGGER.info("'%s'is not a generated file. No point in tokenizing" % cache.get_repo_local_path(file_path))
    return
  gen_funcs_meta = execution_utils.load_generated_functions_meta(file_path)
  func_index = 0
  for func_name, gen_func_meta in gen_funcs_meta.items():
    func_index += 1
    if func_index % 10 == 0:
      LOGGER.info("Filtering function %d / %d .... " % (func_index, len(gen_funcs_meta)))
    tokenize_function(gen_func_meta)


def tokenize_function(gen_func_meta):
  func_body = ast_utils.get_function_body_as_str(gen_func_meta.body)
  func_name = ast_utils.get_func_name(gen_func_meta.body)
  tokens = contexter.tokenize_func_body(func_body)
  if not func_name.startswith(constants.FUNCTION_PREFIX):
    tokens = tokens.union(contexter.tokenize_string(func_name))
  if gen_func_meta.source_code_function_name:
    tokens = tokens.union(contexter.tokenize_string(gen_func_meta.source_code_function_name))
  if gen_func_meta.source_code_class_name:
    tokens = tokens.union(contexter.tokenize_string(gen_func_meta.source_code_class_name))
  if not tokens:
    return
  tokens = list(tokens)
  hash_key = get_hash_key("$$".join(tokens))
  context_json = {
    "name": gen_func_meta.name,
    "tokens": tokens,
    "hash_key": hash_key,
    "body": func_body
  }
  # print(func_body)
  # print(tokens)
  # print("***************************")
  get_token_store().save_contextual_tokens(context_json)


def index_tokens():
  _STORE = get_token_store()
  tokens = _STORE.get_contextual_tokens()
  els = get_elastic_store()
  els.create_index(delete_old=True)
  els.index_documents(tokens)


def tokenize_folder(folder_path):
  for file_path in cache.list_files(folder_path, check_nest=True, is_absolute=True,
                                    prefix=constants.GENERATED_PREFIX, extension=".py"):
    tokenize_functions_from_file(file_path)


def tokenize_from_db():
  for function_metadata in execution_utils.load_generated_functions_from_db():
    gen_func_meta = block_utils.from_generated_function_bson(function_metadata)
    tokenize_function(gen_func_meta)


def tokenize_dataset(use_file_system):
  if use_file_system:
    LOGGER.info("Tokenizing generated files for dataset: '%s' ... " % properties.CONFIG.get_dataset())
    tokenize_folder(properties.PYTHON_PROJECTS_HOME)
  else:
    LOGGER.info("Tokenizing functions from db for dataset: '%s' ... " % properties.CONFIG.get_dataset())
    tokenize_from_db()


def _main():
  # tokenize_dataset(use_file_system=False)
  index_tokens()


def _test():
  # tokenize_functions_from_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/CodeJam/Y11R5P1/zibada/generated_py_b90acec3634b439bbaa1bbfc8ddd36c4.py")
#   func_body = """
# l = 0.0
# r = x0
# for i in xrange(100):
#     m = (l + r) / 2.0
#     if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
#         r = m
#     else:
#         l = m
# return m
#   """
  func_body = """
NAs = np.arange(1, G, dtype='float') * area / G
points = [bisect(lambda x: cumul_area(x) - NA, 0, W) for NA in NAs]
return G
  """
  print(contexter.is_legit_token("None"))
  print(contexter.tokenize_string("descriptor '__init__' of 'OrderedDict' object needs an argument"))
  # print(tokenize_function_body(func_body))


if __name__ == "__main__":
  # _test()
  # exit()
  # print(re.match("^[a-zA-Z]+$", "cumul"))
  _main()
