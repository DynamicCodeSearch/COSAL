import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import constants, execution_utils, helper, parse_utils
from utils import cache, logger
from store import mongo_store, json_store
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_function_store():
  if properties.STORE == "mongo":
    return mongo_store.FunctionStore(properties.CONFIG.get_dataset())
  elif properties.STORE == "json":
    return json_store.FunctionStore(properties.CONFIG.get_dataset())
  else:
    raise RuntimeError("Invalid store: %s" % properties.STORE)


def permutate_file(file_path, do_force):
  file_name = cache.get_file_name(file_path)
  if not file_name.startswith(constants.GENERATED_PREFIX):
    LOGGER.info("'%s'is not a generated file. Not permutating!" % cache.get_repo_local_path(file_path))
    return
  folder_path = cache.get_parent_folder(file_path)
  suffix = file_name[len(constants.GENERATED_PREFIX):]
  permutated_file = os.path.join(folder_path, constants.PERMUTATED_PREFIX + suffix + ".py")
  if cache.file_exists(permutated_file) and not do_force:
    LOGGER.info("Processed file: '%s'. Moving on ...")
    return
  STORE = get_function_store()
  STORE.del_py_functions_metadata(permutated_file)
  gen_funcs_meta = execution_utils.load_generated_functions_meta(file_path)
  all_permutated_functions = []
  source_file = None
  for func_name, gen_func_meta in gen_funcs_meta.items():
    print(func_name)
    if source_file is None:
      source_file = gen_func_meta.source_file
    permutated_funcs = parse_utils.permutate_function(gen_func_meta)
    if not permutated_funcs:
      LOGGER.critical("Skipping function: %s since it returns null on permutation of args. "
                      "Debug permutateFunction method!" % func_name)
      continue
    all_permutated_functions += permutated_funcs
  bodies = []
  for cloned_func in all_permutated_functions:
    bodies.append(cloned_func.body)
    cloned_func.generated_file = permutated_file
    STORE.update_py_function_metadata(cloned_func.to_bson())
  if all_permutated_functions:
    local_python_file = source_file.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0]
    headers = ["import sys",
               "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME,
               "from %s import *" % local_python_file.replace(os.path.sep, ".")]
    content = "\n".join(headers) + "\n\n" + "\n\n".join(bodies)
    LOGGER.info("Saving cloned functions in '%s'" % cache.get_repo_local_path(permutated_file))
    cache.write_file(cache.get_absolute_path(permutated_file), content)


def permutate_folder(folder_path):
  for file_path in cache.list_files(folder_path, check_nest=True, is_absolute=True,
                                    prefix=constants.GENERATED_PREFIX, extension=".py"):
    permutate_file(file_path, True)


def permutate_dataset():
  LOGGER.info("Permutating generated files for dataset: '%s' ... " % properties.CONFIG.get_dataset())
  permutate_folder(properties.PYTHON_PROJECTS_HOME)


def _test():
  permutate_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/generated_py_aa49227f074a4b9a831ddd9ecd8db60e.py", True)


if __name__ == "__main__":
  _test()
