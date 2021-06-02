import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import properties
from analysis.blocks import block_utils
from analysis.helpers import ast_utils, execution_utils, helper, parse_utils
from analysis.parsers import method_parser
from store import mongo_store
from utils import cache, logger

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_function_store():
  if properties.STORE != "mongo":
    raise RuntimeError("Currently supports only mongo store. Not supported for '%s'" % properties.STORE)
  return mongo_store.FunctionStore(properties.CONFIG.get_dataset(), is_test=False)


def create_function_file(func_bodies):
  body = ["import sys",
          "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME]
  for func_body in func_bodies:
    body.append("")
    body.append(func_body)
  file_name = "standalone_%s.py" % helper.generate_random_string()[-8:]
  file_path = os.path.join(properties.PYTHON_PROJECTS_HOME, file_name)
  cache.write_py_file(file_path, "\n".join(body))
  return file_path


def get_headers(file_name):
  python_file = file_name.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0]
  headers = ["import sys",
             "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME,
             "from %s import *" % python_file.replace(os.path.sep, ".")]
  return headers


def generate_for_file(file_name):
  if not file_name.endswith(".py"):
    return
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  parent_folder = cache.get_parent_folder(file_name)
  headers = get_headers(file_name)
  generated_file_name = helper.generate_py_file_name()
  generated_file_path = os.path.join(parent_folder, "%s.py" % generated_file_name)
  visitor = method_parser.WholeMethodVisitor(file_name, properties.CONFIG.get_dataset())
  methods = visitor.parse()
  generated_functions = []
  for orig_gen_method in methods:
    method_meta = visitor.get_meta_for_method(orig_gen_method)
    if not method_meta["is_valid"]:
      LOGGER.info("Function '%s' is invalid. Not running!!" % orig_gen_method.get_base_function_name())
      continue
    function_nodes = orig_gen_method.create_function_for_returns(method_meta)
    expanded_funcs = parse_utils.expand_function(function_nodes, method_meta, headers, parent_folder)
    if not expanded_funcs:
      continue
    for func in expanded_funcs:
      perm_funcs = parse_utils.permutate_function(func)
      if not perm_funcs:
        continue
      for perm_func in perm_funcs:
        perm_func.source_file = file_name
        perm_func.generated_file = generated_file_path
        perm_func.source_code_function_name = orig_gen_method.source_code_function_name
        perm_func.source_code_class_name = orig_gen_method.source_code_class_name
        perm_func.original_function_name = orig_gen_method.name
        generated_functions.append(perm_func)
  return generated_functions


def execute_for_function_body(func_body):
  generated_functions = []
  try:
    function_store = get_function_store()
    file_path = create_function_file([func_body])
    generated_functions = generate_for_file(file_path)
    if not generated_functions:
      return
    headers = get_headers(file_path)
    parent_folder = cache.get_parent_folder(file_path)
    for gen_func in generated_functions:
      func_obj = parse_utils.get_function_obj(gen_func.body, gen_func.name, headers, parent_folder)
      if func_obj is None:
        LOGGER.info("Failed to fetch FUNCTION object for %s" % str(func_obj))
        continue
      args = execution_utils.get_function_args(gen_func)
      if not args:
        LOGGER.info("Failed to fetch ARGS for %s" % str(func_obj))
        continue
      results = []
      for arg_index, arg in enumerate(args):
        exec_results = execution_utils.execute_function(func_obj, arg)
        exec_results["return_json"] = block_utils.format_value_as_json(exec_results["return"], gen_func, arg_index)
        results.append(exec_results)
      function_store.save_py_metadata(gen_func.to_bson())
      function_store.save_py_function({
        "name": gen_func.name,
        "fileName": gen_func.generated_file,
        "dataset": properties.CONFIG.get_dataset(),
        "inputKey": gen_func.input_key,
        "outputs": results
      })
  finally:
    if generated_functions:
      for gen_func in generated_functions:
        cache.delete_file(gen_func.source_file)


def read_from_file(file_path):
  function_store = get_function_store()
  function_store.del_all_py_functions()
  function_store.del_all_py_functions_metadata()
  contents = cache.load_json(file_path)
  for content in contents:
    execute_for_function_body(content)


def _test():
  func_body = """
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swops = 0
        for j in range(i+1, n):
            if array[j] < array[i]:
               array[j], array[i] = array[i], array[j]
               swops += 1
        if swops == 0:
            break
  """
  # execute_for_function_body(func_body)
  # file_path = create_function_file([func_body])
  # generate_for_file(file_path)
  read_from_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_expts/sample_py_functions.json")


def _main():
  args = sys.argv
  message = """
    python engines/execute.py <path to python json file>
    """
  if len(args) < 2:
    print(message)
    exit(0)
  read_from_file(args[1])


if __name__ == "__main__":
  _main()

