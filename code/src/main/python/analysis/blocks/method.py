import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.helpers import constants as a_consts
from analysis.helpers import ast_utils, helper
from analysis.blocks import statements as statement_block
from analysis.blocks import parameter as parameter_block
from utils import cache
from utils.lib import O

import properties


class Method(O):
  def __init__(self, **kwargs):
    self.file_source = None
    self.name = None
    self.return_type = None
    self.start_pos = None
    self.end_pos = None
    self.args = None
    self.statement_blocks = []  # [<Statements>]
    self._statement_groups = None  # [[<Statements>], [<Statements>]]
    self._ast = None
    self._scope = None
    self._prerequisite_statements = []
    O.__init__(self, **kwargs)

  def get_ast(self):
    return self._ast

  def get_scope(self):
    return self._scope

  def is_root(self):
    return self.name == a_consts.ROOT_SCOPE

  def split_statement_blocks(self):
    split = None
    for i, statement in enumerate(self.statement_blocks):
      if isinstance(statement, Method):
        split = i
    if split is None:
      return self.statement_blocks
    else:
      self._prerequisite_statements, statements = self.statement_blocks[:split+1], self.statement_blocks[split+1:]
    return statements

  def get_statement_groups(self):
    if self._statement_groups is not None:
      return self._statement_groups
    # self._statement_groups = Method.create_statement_groups(self.statement_blocks)
    # return self._statement_groups
    _statement_groups = []
    method_statement_blocks = self.split_statement_blocks()
    groups = Method.create_statement_groups(method_statement_blocks)
    for group in groups:
      combinations = Method.get_combinations(group)
      if combinations and len(combinations) > 0:
        _statement_groups += combinations
    for statement in method_statement_blocks:
      if isinstance(statement, statement_block.GroupedStatement) or \
         isinstance(statement, statement_block.ChoiceGroupedStatement):
        _statement_groups.append([statement])
    self._statement_groups = []
    if len(self._prerequisite_statements) >= properties.MIN_STATEMENT_SIZE:
      self._statement_groups.append(self._prerequisite_statements)
    for _statement_group in _statement_groups:
      _statement_group = self._prerequisite_statements + _statement_group
      if len(_statement_group) >= properties.MIN_STATEMENT_SIZE:
        self._statement_groups.append(_statement_group)
    return self._statement_groups

  def get_text(self):
    return ast_utils.convert_ast_to_code(self._ast).strip("\n")

  def pprint(self):
    print(self.get_text())

  @staticmethod
  def print_statement_group(groups):
    for combination in groups:
      print("\n*** Combination ***")
      for statement in combination:
        statement.pprint()
      print("********************")

  @staticmethod
  def create_statement_groups(statement_blocks):
    if not statement_blocks: return []
    ret_list = []
    statement_group = []
    for statement in statement_blocks:
      statement_group.append(statement)
      if isinstance(statement, statement_block.GroupedStatement):
        sub_ret_list = Method.create_statement_groups(statement.statements)
        if sub_ret_list:
          ret_list += sub_ret_list
      elif isinstance(statement, statement_block.ChoiceGroupedStatement):
        for choice in statement.choices:
          sub_ret_list = Method.create_statement_groups(choice)
          if sub_ret_list:
            ret_list += sub_ret_list
    # min_size = properties.MIN_STATEMENT_SIZE
    min_size = 1
    if len(statement_group) >= min_size:
      ret_list.append(statement_group)
    return ret_list

  @staticmethod
  def get_combinations(statement_blocks):
    step_start = properties.MIN_STATEMENT_SIZE
    # step_start = 1
    combinations = []
    for step_size in xrange(step_start, len(statement_blocks)):
      for counter in xrange(0, len(statement_blocks) - step_size + 1):
        combinations.append(statement_blocks[counter: counter + step_size])
    combinations.append(statement_blocks)
    return combinations


def is_constructor(method_name):
  return method_name == "__init__"


def get_parameters(method_node, skip_self):
  params = []
  if method_node.args and method_node.args.args:
    for arg in method_node.args.args:
      params.append(arg.id)
  if skip_self and params and params[0]:
    params = params[1:]
  return [parameter_block.Parameter(name, index) for index, name in enumerate(params)]


class GeneratedFunction(O):
  def __init__(self, **kwargs):
    self.name = None
    self.is_whole_method = False
    self.original_function_name = None
    self.source_code_function_name = None
    self.source_code_class_name = None
    self.parameters = None  # Same as argsMetadata from Java
    self.source_file = None
    self.generated_file = None
    self.body = None
    self.input_key = None
    self.args_permutation = None
    self.is_static_method = False
    self._ast = None
    self._func_obj = None
    self._method_meta = None
    O.__init__(self, **kwargs)

  def to_bson(self):
    d = {
      "name": self.name,
      "is_whole_method": self.is_whole_method,
      "original_function_name": self.original_function_name,
      "source_code_class_name": self.source_code_class_name,
      "source_code_function_name": self.source_code_function_name,
      "parameters": None,
      "source_file": cache.get_repo_local_path(self.source_file),
      "generated_file": cache.get_repo_local_path(self.generated_file),
      "body": self.body,
      "input_key": self.input_key,
      "args_permutation": None,
      "is_static_method": self.is_static_method
    }
    if self.parameters:
      d["parameters"] = {name: v.to_bson() for name, v in self.parameters.items()}
    if self.args_permutation:
      d["args_permutation"] = GeneratedFunction.encode_args_permutation(self.args_permutation)
    return d

  def to_bson_camel_case(self):
    d = {
      "name": self.name,
      "isWholeMethod": self.is_whole_method,
      "originalFunctionName": self.original_function_name,
      "sourceCodeClassName": self.source_code_class_name,
      "sourceCodeFunctionName": self.source_code_function_name,
      "parameters": None,
      "filePath": cache.get_repo_local_path(self.source_file),
      "generatedFile": cache.get_repo_local_path(self.generated_file),
      "body": self.body,
      "inputKey": self.input_key,
      "argsPermutation": None,
      "isStaticMethod": self.is_static_method
    }
    if self.parameters:
      d["parameters"] = {name: v.to_bson() for name, v in self.parameters.items()}
    if self.args_permutation:
      d["argsPermutation"] = GeneratedFunction.encode_args_permutation(self.args_permutation)
    return d

  def clone(self):
    cloned = GeneratedFunction()
    cloned.name = self.name
    cloned.is_whole_method = self.is_whole_method
    cloned.original_function_name = self.original_function_name
    cloned.source_code_class_name = self.source_code_class_name
    cloned.source_code_function_name = self.source_code_function_name
    cloned.parameters = self.parameters
    cloned.source_file = self.source_file
    cloned.generated_file = self.generated_file
    cloned.body = self.body
    cloned.input_key = self.input_key
    cloned.args_permutation = self.args_permutation
    cloned.is_static_method = self.is_static_method
    cloned._ast = self._ast
    cloned._func_obj = self._func_obj
    cloned._method_meta = self._method_meta
    return cloned

  @staticmethod
  def encode_args_permutation(permutation):
    return {k.replace(".", "$"): v for k, v in permutation.items()}

  @staticmethod
  def decode_args_permutation(permutation):
    return {k.replace("$", "."): v for k, v in permutation.items()}

  def set_ast(self, node):
    self._ast = node

  def get_ast(self):
    return self._ast

  def set_func_obj(self, func_obj):
    self._func_obj = func_obj

  def get_func_obj(self):
    return self._func_obj

  def get_method_meta(self):
    return self._method_meta

  def set_method_meta(self, method_meta):
    self._method_meta = method_meta

  def get_scope_name(self):
    name = self.source_code_function_name if self.source_code_function_name else self.name
    return "%s%s%s" % (a_consts.ROOT_SCOPE, a_consts.SCOPE_SEPARATOR, name)

  def get_base_function_name(self):
    return self.source_code_function_name if self.source_code_function_name else self.name

  def create_function_for_returns(self, method_meta):
    base_ast = self.get_ast()
    functions = {}
    if method_meta["has_return_statement"]:
      name = helper.generate_function_name()
      clone = self.clone()
      clone.name = name
      new_ast = ast_utils.create_function(name, base_ast.args, base_ast.body)
      clone.set_ast(new_ast)
      functions[name] = clone
    else:
      for ret_variable in method_meta["returns"]:
        name = helper.generate_function_name()
        clone = self.clone()
        clone.name = name
        return_stmt = ast_utils.create_return_statement(var_name=ret_variable.name)
        new_ast = ast_utils.create_function(name=name, args=base_ast.args, body=base_ast.body+[return_stmt])
        clone.set_ast(new_ast)
        functions[name] = clone
    return functions

