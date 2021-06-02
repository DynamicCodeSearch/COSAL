import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import ast

from analysis.helpers import constants as a_consts
from analysis.helpers import ast_utils, helper, parse_utils
from analysis.parsers import method_parser, statement_parser
from analysis.blocks import method as method_block
from analysis.blocks import statements as statement_block
from analysis.blocks import types as types_block
from analysis.blocks import block_utils
from utils import cache, maths, logger
from store import json_store, mongo_store
import properties


DEBUG = False

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_store(dataset):
  if properties.STORE == "json":
    return json_store.FunctionStore(dataset)
  elif properties.STORE == "mongo":
    return mongo_store.FunctionStore(dataset)
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def get_py_class_store():
  if properties.STORE == "mongo":
    return mongo_store.PyClassStore()
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def print_statements(statement_group):
  for statement in statement_group:
    statement.pprint()


def create_function_nodes(statement_group, function_meta):
  args = ast.arguments(args=[ast.Name(id=variable.name) for variable in function_meta["args"]], vararg=None, kwarg=None,
                       defaults=[])
  function_nodes = {}
  function_body = [statement.get_ast() for statement in statement_group]
  if function_meta["has_return_statement"]:
    name = helper.generate_function_name()
    function_nodes[name] = ast.FunctionDef(name=name, args=args, body=function_body, decorator_list=[])
  else:
    for ret_variable in function_meta["returns"]:
      name = helper.generate_function_name()
      return_statement = ast.Return(value=ast.Name(id=ret_variable.name))
      function_nodes[name] = ast.FunctionDef(name=name, args=args, body=function_body + [return_statement],
                                             decorator_list=[])
  return function_nodes


def get_line_numbers(statement_group):
  line_numbers = set()
  for statement in statement_group:
    line_numbers.update(range(statement.start_pos.line, statement.end_pos.line + 1))
  return line_numbers


def get_meta_for_statement_group(statement_group, method, variable_map, local_variables):
  start = statement_group[0].start_pos
  end = statement_group[-1].end_pos
  line_numbers = get_line_numbers(statement_group)
  scope = method.get_scope()
  # if DEBUG:
  #   print(variable_map[str(scope)])
  variables = get_variables_in_range(variable_map, scope, start, end, line_numbers)
  has_return_statement = isinstance(statement_group[-1], statement_block.Statement) and statement_group[-1].is_return
  if DEBUG:
    print "Start: %s, End: %s" % (start, end)
  args, returns = set(), set()
  for variable in variables:
    if variable.get_first_position() < start:
      args.add(variable)
    if not has_return_statement and variable.is_used_in_range(start, end):
      returns.add(variable)
  is_valid = len(args) > 0
  for variable in args:
    if not variable.is_valid():
      is_valid = False
      break
  return {
    "args": sorted(list(args), key=lambda x: x.name),
    "returns": list(returns),
    "has_return_statement": has_return_statement,
    "is_valid": is_valid
  }


def check_type_validity(visitor, var_type):
  if isinstance(var_type, types_block.PrimitiveType):
    return True
  elif isinstance(var_type, types_block.FileType):
    return var_type.is_valid
  elif isinstance(var_type, types_block.SystemType):
    # TODO: Check in DB and remove the block below!
    class_store = get_py_class_store()
    return class_store.is_valid_system_class(var_type.module, var_type.name)
  elif type(var_type).__name__ in {'ListType', 'SetType', 'TupleType'}:
    types = []
    for param_type in var_type.types:
      if check_type_validity(visitor, param_type):
        types.append(param_type)
    if len(types) == 0:
      return False
    var_type.types = types
    return True
  elif isinstance(var_type, types_block.DictType):
    key_types = []
    for param_type in var_type.key_types:
      if check_type_validity(visitor, param_type):
        key_types.append(param_type)
    if len(key_types) == 0:
      return False
    var_type.key_types = key_types
    val_types = []
    for param_type in var_type.val_types:
      if check_type_validity(visitor, param_type):
        val_types.append(param_type)
    if len(val_types) == 0:
      return False
    var_type.val_types = val_types
    return True
  elif isinstance(var_type, types_block.CustomType):
    # Fetch class block and populate custom type
    class_store = get_py_class_store()
    class_instance = class_store.load_custom_class(visitor.file_path, var_type.name)
    if class_instance:
      class_instance = block_utils.from_class_bson(class_instance)
      return class_instance.is_valid()
    else:
      class_instance = visitor.classes.get(var_type.name, None)
      if class_instance:
        is_valid = True
        for parameter in class_instance.constructor_params:
          if not parameter.is_valid():
            is_valid = False
            break
        is_valid = is_valid and len(class_instance.construtor_params) > 0
        return is_valid
      return False
  else:
    raise RuntimeError("@COSAL: Invalid type '%s' for '%s'" % (type(var_type).__name__, var_type.name))


def validate_visitor_variables(visitor):
  for scope in visitor.scope_variable_map.keys():
    scope_variables = visitor.scope_variable_map[scope]
    valid_variables = {}
    for var_name, scope_variable in scope_variables.items():
      is_valid = True
      if not scope_variable.types:
        is_valid = False
      else:
        #TODO: check if class is reassigned to variable if valid
        valid_types = set()
        for var_type in scope_variable.types:
          # if isinstance(var_type, types_block.CustomType):
          #   clazz = visitor.classes[var_type.name]
          #   if not clazz:
          #     continue
          #   var_type = clazz.to_custom_type()
          var_type = check_and_cast_to_custom_type(visitor, var_type)
          if var_type and check_type_validity(visitor, var_type):
            valid_types.add(var_type)
        is_valid = len(valid_types) > 0
        scope_variable.types = valid_types
      if is_valid:
        valid_variables[var_name] = scope_variable
    visitor.scope_variable_map[scope] = valid_variables


def check_and_cast_to_custom_type(visitor, var_type):
  if not var_type:
    return None
  elif type(var_type) == types_block.CustomType:
    clazz = visitor.classes[var_type.name]
    if not clazz:
      return None
    return clazz.to_custom_type()
  elif type(var_type) in [types_block.PrimitiveType, types_block.FileType]:
    return var_type
  elif type(var_type) == types_block.SystemType:
    if var_type.parameters:
      var_type.parameters = [set([check_and_cast_to_custom_type(visitor, param_type)
                                  for param_type in list(i_parameters)])
                             for i_parameters in var_type.parameters]
    return var_type
  elif type(var_type) in [types_block.ListType, types_block.SetType, types_block.TupleType]:
    if var_type.types:
      var_type.types = [check_and_cast_to_custom_type(visitor, t) for t in var_type.types]
    return var_type
  elif type(var_type) == types_block.DictType:
    if var_type.key_types:
      var_type.key_types = [check_and_cast_to_custom_type(visitor, t) for t in var_type.key_types]
    if var_type.val_types:
      var_type.val_types = [check_and_cast_to_custom_type(visitor, t) for t in var_type.val_types]
    return var_type
  else:
    raise RuntimeError("@COSAL: Unsupported data type '%s'" % type(var_type).__name__)


def create_variable_map(visitor):
  variable_map = {}
  for scope in visitor.scope_variable_map.keys():
    curr_scope = scope
    variables = set()
    while curr_scope:
      for var in visitor.scope_variable_map[curr_scope].values():
        variables.add(var)
      curr_scope = curr_scope.parent
    variable_map[str(scope)] = variables
  return variable_map


def get_variables_in_range(variable_map, scope, start, end, line_numbers):
  ranged_variables = []
  current_scope = scope
  while current_scope:
    variables = variable_map[str(current_scope)]
    current_scope = current_scope.parent
    if not variables:
      continue
    for variable in variables:
      for pos in variable.positions:
        if pos.line not in line_numbers:
          continue
        if start <= pos <= end:
          ranged_variables.append(variable)
          break
  return ranged_variables

# def get_variables_in_range(variables, start, end, line_numbers):
#   ranged_variables = []
#   for variable in variables:
#     for pos in variable.positions:
#       if pos.line not in line_numbers:
#         continue
#       if start <= pos <= end:
#         ranged_variables.append(variable)
#         break
#   return ranged_variables

def generate_for_file(dataset, file_name, force_fetch=False):
  if not file_name.endswith(".py"):
    return
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  parent_folder = cache.get_parent_folder(file_name)
  store = get_store(dataset)
  generated_file_path = store.get_generated_file(file_name)
  if generated_file_path is not None and cache.file_exists(generated_file_path):
    LOGGER.info("Already snipped '%s'" % cache.get_repo_local_path(file_name))
    return
  elif generated_file_path is not None:
    store.del_py_functions_metadata(generated_file_path)
  visitor = statement_parser.StatementVisitor(file_name, dataset, infer_types=True, force_fetch=force_fetch)
  visitor.parse()
  validate_visitor_variables(visitor)
  variable_map = create_variable_map(visitor)
  generated_functions = {}
  python_file = file_name.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0]
  headers = ["import sys",
             "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME,
             "from %s import *" % python_file.replace(os.path.sep, ".")]
  header_str = "\n".join(headers)
  body = [header_str]
  generated_file_path = os.path.join(parent_folder, "%s.py" % helper.generate_py_file_name())
  for method in visitor.methods:
    if DEBUG:
      print("\n\n# Method Name: %s. Statement Blocks: %d" % (method.name, len(method.statement_blocks)))
    if method.name == a_consts.ROOT_SCOPE: continue
    for statement_group in method.get_statement_groups():
      if DEBUG:
        print("\n## SG")
        print_statements(statement_group)
        print("\n### Generated")
      # Save type for each function node
      function_meta = get_meta_for_statement_group(statement_group, method, variable_map,
                                                   visitor.scope_variable_map[method.get_scope()].values())
      if DEBUG:
        print("### Meta")
        print("#### Valid Meta: %s" % function_meta["is_valid"])
        print([a.name for a in function_meta['args']])
      if not function_meta["is_valid"]:
        continue
      function_nodes = create_function_nodes(statement_group, function_meta)
      for func in parse_utils.expand_function(function_nodes, function_meta, headers, parent_folder):
        func.source_file = file_name
        func.generated_file = generated_file_path
        body.append(func.body)
        store.update_py_function_metadata(func.to_bson())
      if DEBUG:
        print("#### Function Nodes: %d" % len(function_nodes))
  content = "\n\n".join(body)
  cache.write_file(generated_file_path, content)
  assert helper.is_valid_file(generated_file_path)
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  return generated_functions


def generate_whole_methods_for_file(file_name, do_force=False):
  if not file_name.endswith(".py"):
    return
  visitor = method_parser.MethodVisitor(file_name, properties.CONFIG.get_dataset())
  generated_functions = visitor.parse()
  store = get_store(properties.CONFIG.get_dataset())
  for gen_func in generated_functions:
    store.update_py_function_metadata(gen_func.to_bson())
  return generated_functions


def extract_method_names(dataset, file_name):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  parent_folder = cache.get_parent_folder(file_name)


def _test():
  generate_whole_methods_for_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/SystemLibs/string.py")
  exit()
  generate_for_file("CodeJam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/CodeJam/Y11R5P1/dozingcat/a.py", force_fetch=True)
  # generate_for_file("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/dozingcat/a.py")
  # generate_for_file("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/kia/a.py")


if __name__ == "__main__":
  _test()
