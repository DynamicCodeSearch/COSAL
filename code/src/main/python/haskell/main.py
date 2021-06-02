import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from collections import defaultdict

from haskell.parsers import haskell_parser
from haskell.blocks import haskell_function
from haskell.executions import execute
from haskell.db_store.function_store import FunctionStore

import properties


HASKELL_PROJECT_SRC = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell"


def parse_and_store_functions(file_path):
  local_path = file_path
  if local_path.startswith(HASKELL_PROJECT_SRC):
    local_path = local_path[len(HASKELL_PROJECT_SRC) + len(os.path.sep):]
  if local_path.endswith(".hs"):
    local_path = local_path[:-3]
  mod = local_path.replace(os.path.sep, ".")
  functions_or_error = haskell_parser.parse(mod, file_path)
  if not functions_or_error:
    return None
  store = FunctionStore(properties.CONFIG.get_dataset())
  store.del_hs_functions_by_file_path(file_path)
  all_functions = []
  for function in functions_or_error:
    permutations = haskell_function.permutate_function(function)
    if not permutations:
      continue
    all_functions += permutations
    for permutation in permutations:
      store.save_hs_function(permutation.to_bson())
  return all_functions


def group_functions(functions):
  groups = defaultdict(dict)
  for func in functions:
    group = groups.get(func.file_path, {})
    func_names = group.get("funcNames", set())
    func_names.add(func.source_code_function_name)
    group["funcNames"] = func_names
    group["filePath"] = func.file_path
    group["module"] = func.module
    groups[func.file_path] = group
  return groups


def execute_functions(functions, skip_functions=None):
  if skip_functions:
    functions = [func for func in functions if func.source_code_function_name not in skip_functions]
  function_groups = group_functions(functions)
  file_executable_path = {}
  store = FunctionStore(properties.CONFIG.get_dataset())
  for file_path, function_group in function_groups.items():
    executable_path = execute.create_executable_hs_export_file(function_group, force_create=True)
    file_executable_path[file_path] = executable_path
    store.del_executed_hs_functions_by_file_path(file_path)
  for func in functions:
    execute.execute(func, file_executable_path[file_path])


def runner(file_path):
  functions = parse_and_store_functions(file_path)
  skip_functions = ["fib"]
  execute_functions(functions, skip_functions=skip_functions)


def _test_executable_generation():
  func_group = {
    "funcNames": set(['hasPath', 'isAsc', 'fac', 'asc', 'prefixes', 'el', 'doubleList', 'lagrange',
                      'nub', 'rev', 'in_range', 'fibTail', 'greet', 'tempFunc', 'fib', 'facTail', 'add', 'foldTrie']),
    "filePath": "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell/Tutorial/Example.hs",
    "module": "Tutorial.Example"
  }
  execute.create_executable_hs_export_file(func_group, force_create=True)


def _test_runner(file_path):
  runner(file_path)


if __name__ == "__main__":
  _test_runner("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell/Tutorial/Example.hs")
  # _test_executable_generation()
