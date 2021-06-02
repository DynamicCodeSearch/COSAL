import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.helpers import ast_utils, helper, execution_utils
from analysis.blocks import method as method_block
from utils import maths, cache
import properties


def expand_arguments(args):
  expanded_argsets = []
  for arg in args:
    expanded_args = arg.to_specific_variables()
    if expanded_args is None:
      return None
    expanded_argsets.append(expanded_args)
  if not expanded_argsets:
    return None
  return maths.permutate_lists(expanded_argsets)


def is_valid_function(header_str, function_body, parent_folder):
  file_name = helper.generate_py_temp_name()
  temp_file = os.path.join(parent_folder, "%s.py" % file_name)
  content = "%s\n\n%s" % (header_str, function_body)
  cache.write_file(temp_file, content)
  validity = helper.is_valid_file(temp_file)
  cache.delete_file(temp_file)
  return validity


def get_function_obj(function_body, func_name, headers, parent_folder):
  file_name = helper.generate_py_temp_name()
  temp_file = os.path.join(parent_folder, "%s.py" % file_name)
  try:
    contents = headers + ["\n", function_body]
    content = "\n".join(contents)
    cache.write_file(temp_file, content)
    sys.path.append(properties.PYTHON_PROJECTS_HOME)
    validity = helper.is_valid_file(temp_file)
    if not validity:
      return None
    python_name = temp_file.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0].replace(os.path.sep, ".")
    module = __import__(python_name)
    func_obj = getattr(module, func_name)
    return func_obj
  finally:
    cache.delete_file(temp_file)
    sys.path.remove(properties.PYTHON_PROJECTS_HOME)


def expand_function(function_nodes, base_function_meta, func_headers, parent_folder, debug=False):
  expanded_argsets = expand_arguments(base_function_meta['args'])
  generated_functions = []
  if not expanded_argsets:
    return generated_functions
  if debug:
    # for arg in function_meta['args']:
    #   if arg.name == "a":
    #     print(arg)
    #     print(expanded_argsets)
    #     exit()
    print("Num of Function nodes: %d" % len(function_nodes))
    print("Num of expanded argsets: %d" % len(expanded_argsets))
  for argset in expanded_argsets:
    arg_dict = {}
    for index, arg in enumerate(sorted(argset, key=lambda x: x.name)):
      arg.index = index
      arg_dict[arg.name] = arg.to_specific_parameter()
      # print(arg.name, arg_dict[arg.name].type)
    for function_name, function_node in function_nodes.items():
      fn = function_node
      if isinstance(function_node, method_block.GeneratedFunction):
        fn = function_node.get_ast()
      new_func_name = helper.generate_function_name()
      renamed_function_node = ast_utils.update_function_name(fn, new_func_name)
      function_body = ast_utils.convert_ast_to_code(renamed_function_node)
      if is_valid_function(func_headers, function_body, parent_folder):
        generated_function = method_block.GeneratedFunction(
          name=renamed_function_node.name,
          parameters=arg_dict,
          # source_file=file_name,
          # generated_file=generated_file_path,
          body=function_body
        )
        generated_functions.append(generated_function)
        # body.append(function_body)
        # store.update_py_function_metadata(generated_function.to_bson())
  return generated_functions


def permutate_function(generated_function):
  arg_keys = execution_utils.get_function_arg_and_key(generated_function)
  grouped_arg_keys = execution_utils.group_arg_and_key(arg_keys)
  if execution_utils.has_too_many_arguments(grouped_arg_keys):
    return None
  function_input_key = execution_utils.get_function_args_key(grouped_arg_keys)
  if not function_input_key:
    return None
  generated_function.input_key = function_input_key
  args_permutations = execution_utils.permutate_args_and_key(grouped_arg_keys)
  if not args_permutations:
    return None
  existing_perms = set()
  permutated_funcs = []
  for i, args_permutation in enumerate(args_permutations):
    serialized_arg_permutation = str(args_permutation)
    if serialized_arg_permutation in existing_perms:
      continue
    existing_perms.add(serialized_arg_permutation)
    func_ast = ast_utils.parse_function(generated_function.body)
    if func_ast is None:
      continue
    func_name = helper.generate_function_name()
    func_ast = ast_utils.update_function_name(func_ast, func_name)
    func_body = ast_utils.convert_ast_to_code(func_ast)
    cloned = generated_function.clone()
    cloned.name = func_name
    cloned.original_function_name = generated_function.name
    cloned.parameters = generated_function.parameters
    cloned.body = func_body
    cloned.args_permutation = args_permutation
    permutated_funcs.append(cloned)
  return permutated_funcs
