import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.blocks import block_utils
from analysis.helpers import constants, helper, execution_utils, file_utils
from utils import cache, logger
import properties

import random


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
DEBUG = True


def set_metadata_for_function(func_meta):
  arg_keys = execution_utils.get_function_arg_and_key(func_meta)
  grouped_arg_keys = execution_utils.group_arg_and_key(arg_keys)
  if execution_utils.has_too_many_arguments(grouped_arg_keys):
    return None
  function_input_key = execution_utils.get_function_args_key(grouped_arg_keys)
  if not function_input_key:
    return None
  func_meta.input_key = function_input_key
  args_permutation = execution_utils.permutate_args_and_key(grouped_arg_keys)
  if not args_permutation:
    return None
  func_meta.args_permutation = args_permutation[0]
  return func_meta


def check_output_validity(gen_func, results, args):
  assert len(results) == len(args)
  arg_matches = [True] * len(args[0])
  previous_result_match = True
  for res_index, res in enumerate(results):
    if res_index > 0 and previous_result_match:
      previous_result_match = res["return_json"] == results[res_index - 1]["return_json"]
    if any(arg_matches):
      for arg_index, arg in enumerate(args[res_index]):
        if not arg_matches[arg_index]:
          continue
        formatted = block_utils.format_value_as_json(arg, gen_func, arg_index)
        arg_matches[arg_index] = res["return_json"] == formatted
    if (not any(arg_matches)) and (not previous_result_match):
      return True
  return False


def is_valid_function(func_meta, func_obj):
  # 1. Set metadata
  func_meta = set_metadata_for_function(func_meta)
  if not func_meta:
    return False
  if len(func_meta.parameters) > properties.MAX_ARGUMENT_SIZE:
    return False
  # 2. Get function args
  args = execution_utils.get_function_args(func_meta)
  if not args:
    return False
  # 3. Execute functions
  results = []
  for arg_index, arg in enumerate(args):
    exec_results = execution_utils.execute_function(func_obj, arg)
    exec_results["return_json"] = block_utils.format_value_as_json(exec_results["return"], func_meta, arg_index)
    results.append(exec_results)
  if not results:
    return False
  # 4. Check if function changes
  cloned_args = execution_utils.get_function_args(func_meta)
  return check_output_validity(func_meta, results, cloned_args)


def filter_file(file_path):
  file_name = cache.get_file_name(file_path)
  if not file_name.startswith(constants.GENERATED_PREFIX):
    LOGGER.info("'%s'is not a generated file. Not validating the snippets!" % cache.get_repo_local_path(file_path))
    return
  LOGGER.info("Filtering file '%s' ... " % cache.get_repo_local_path(file_path))
  STORE = execution_utils.get_function_store()
  file_path = cache.get_repo_local_path(file_path)
  gen_funcs_meta = execution_utils.load_generated_functions_meta(file_path)
  generated_functions = helper.get_generated_functions(cache.get_absolute_path(file_path), as_dict=True)
  invalid_func_names = []
  bodies = []
  source_file = None
  func_index = 0
  for func_name, gen_func_obj in generated_functions.items():
    if len(bodies) == func_index == 5:
      LOGGER.info("'%s'is already filtered!" % cache.get_repo_local_path(file_path))
      return
    func_index += 1
    if func_name not in gen_funcs_meta:
      continue
    # if func_name != "func_26ff925edf694867b1fbcf4e828fefb8":
    #   continue
    # print(func_name)
    if func_index % 10 == 0:
      LOGGER.info("Filtering function %d / %d. # Valids = %d .... "
                  % (func_index, len(generated_functions), len(bodies)))
    gen_func_meta = gen_funcs_meta[func_name]
    if source_file is None:
      source_file = gen_func_meta.source_file
    file_utils.delete_input_temp_files(gen_func_meta.name)
    is_func_valid = is_valid_function(gen_func_meta, gen_func_obj)
    file_utils.delete_input_temp_files(gen_func_meta.name)
    if is_func_valid:
      bodies.append(gen_func_meta.body)
    else:
      invalid_func_names.append(func_name)
    # print(func_name, is_func_valid)
    # exit()
  if bodies and source_file:
    LOGGER.info("Saving '%d' functions ..." % len(bodies))
    local_python_file = source_file.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0]
    headers = ["import sys",
               "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME,
               "from %s import *" % local_python_file.replace(os.path.sep, ".")]
    content = "\n".join(headers) + "\n\n" + "\n\n".join(bodies)
    cache.write_file(cache.get_absolute_path(file_path), content)
  else:
    LOGGER.info("Deleting '%s' since it contains 0 valid files!" % file_path)
    cache.delete_file(cache.get_absolute_path(file_path))
  LOGGER.info("Deleting '%d' functions ..." % len(invalid_func_names))
  for func_name in invalid_func_names:
    STORE.del_py_function_metadata(func_name)


def filter_folder(folder_path):
  files = cache.list_files(folder_path, check_nest=True, is_absolute=True,
                           prefix=constants.GENERATED_PREFIX, extension=".py")
  # random.shuffle(files)
  for file_path in files:
    filter_file(file_path)


def filter_dataset():
  LOGGER.info("Filtering generated files for dataset: '%s' ... " % properties.CONFIG.get_dataset())
  filter_folder(properties.PYTHON_PROJECTS_HOME)


def _main():
  filter_dataset()


def _test():
  filter_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/CodeJam/Y13R5P1/gepa/generated_py_b362034eadb14e039a607fb083331620.py")


if __name__ == "__main__":
  # _test()
  _main()
