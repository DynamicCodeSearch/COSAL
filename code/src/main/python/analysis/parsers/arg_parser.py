import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import ast
import asttokens

from analysis.helpers import constants as a_consts
from analysis.helpers import ast_utils
from analysis.blocks import block_utils
from analysis.blocks import position as position_block
from analysis.blocks import scope as scope_block
from analysis.blocks import types as types_block
from analysis.blocks import variable as variable_block
from analysis.blocks import class_block as class_block
from analysis.blocks import method as method_block
from analysis.parsers import parser
from analysis.type_checking import type_checker
from utils import cache


class VariableVisitor(parser.Traveller):
  def __init__(self, file_path=None, source_code=None):
    parser.Traveller.__init__(self)
    self.file_path = file_path
    self._source_code = source_code
    scope = scope_block.Scope(a_consts.ROOT_SCOPE, None)
    self.tree = None
    self._current_scope = scope
    # Map: Key = Scope, Value = Map<VarName, Var>
    self.scope_variable_map = {
      scope: {}
    }
    # Map: Key = Name, Value = Scope
    self.scopes = {
      str(scope): scope
    }
    self.classes = {}
    self.system_classes = set()
    self.method_scopes = {a_consts.ROOT_SCOPE: str(scope)}
    self._valid_custom_classes = None

  def get_source_code(self):
    return self._source_code

  def is_local_class(self, class_name):
    return class_name in self.classes

  def to_bson(self):
    d = {'file_path': self.file_path}
    if self.scopes:
      d['scopes'] = {}
      for key, val in self.scopes.items():
        d['scopes'][key] = val.to_bson()
    if self.scope_variable_map:
      d['scope_variable_map'] = {}
      for scope, variable_map in self.scope_variable_map.items():
        var_map = {}
        for var_name, variable in variable_map.items():
          var_map[var_name] = variable.to_bson()
        d['scope_variable_map'][str(scope)] = var_map
    if self.method_scopes:
      d['method_scopes'] = self.method_scopes
    return d

  @staticmethod
  def from_bson(bson_dict):
    o = VariableVisitor(bson_dict['file_path'])
    if 'scopes' in bson_dict:
      o.scopes = scope_block.from_bson(bson_dict['scopes'])
    if 'scope_variable_map' in bson_dict:
      o.scope_variable_map = {}
      for scope_str, var_map in bson_dict['scope_variable_map'].items():
        scope = o.scopes[scope_str]
        variables_map = {}
        for var_name, var_dict in var_map.items():
          variable = block_utils.from_variable_bson(var_dict, scope)
          variables_map[var_name] = variable
        o.scope_variable_map[scope] = variables_map
    if 'method_scopes' in bson_dict:
      o.method_scopes = bson_dict['method_scopes']
    return o

  @staticmethod
  def _is_variable_store(node):
    return types_block.BaseType.get_name(node.ctx) == "Store"

  def create_scope(self, name):
    scope = scope_block.Scope(name, self._current_scope)
    self.scopes[str(scope)] = scope
    self.scope_variable_map[scope] = {}
    self._current_scope.children[name] = scope
    self._current_scope = scope
    if name in self.method_scopes:
      raise RuntimeError("Method %s already")
    self.method_scopes[name] = str(scope)
    return scope

  def get_scope(self, scope_name):
    return self.scopes.get(scope_name, None)

  def list_variables(self):
    variables = []
    for variables_map in self.scope_variable_map.values():
      for scope_variables in variables_map.items():
        variables += scope_variables
    return variables

  def find_variable(self, variable_name, scope):
    curr_scope = scope
    while curr_scope and curr_scope in self.scope_variable_map:
      if variable_name in self.scope_variable_map[curr_scope]:
        return self.scope_variable_map[curr_scope][variable_name]
      curr_scope = curr_scope.parent
    return None

  def add_variable(self, name, position, var_type):
    variable_map = self.scope_variable_map.get(self._current_scope, {})
    variable = variable_block.Variable(name=name, scope=self._current_scope, var_type=var_type, positions={position})
    variable_map[name] = variable
    self.scope_variable_map[self._current_scope] = variable_map
    return variable

  def update_variable(self, name, scope, position):
    variable = self.scope_variable_map.get(scope, {}).get(name, None)
    if not variable:
      raise RuntimeError("Variable with name '%s' not found in scope '%s'" % (name, scope.name))
    variable.positions.add(position)
    return variable

  def visit_Name(self, node, meta):
    variable_name = node.id
    variable = self.find_variable(variable_name, self._current_scope)
    is_variable_store = VariableVisitor._is_variable_store(node)
    position = position_block.Position.get_position(node)
    if not variable and not is_variable_store:
      # Might be loading a global variable
      self._current_scope.update_dangling(variable_name, position)
      return
    if meta and meta["var_type"]:
      var_type = meta["var_type"]
    elif self._current_scope.name == a_consts.ROOT_SCOPE:
      var_type = a_consts.VAR_TYPE.GLOBAL
    else:
      var_type = a_consts.VAR_TYPE.LOCAL
    if not variable:
      variable = self.add_variable(variable_name, position, var_type)
    else:
      variable = self.update_variable(variable_name, variable.get_scope(), position)
    py_resolved_type = getattr(node, "resolved_type", None)
    # print("*********")
    # ast_utils.parse_print(node)
    # print(py_resolved_type)
    # print(type(py_resolved_type))
    data_types = type_checker.get_data_types(py_resolved_type)
    if data_types:
      for data_type in data_types:
        # print(data_type)
        data_type = self.check_and_cast_to_custom_type(data_type)
        if data_type and data_type not in variable.types:
          variable.types.add(data_type)
        if data_type and type(data_type) == types_block.SystemType:
          self.system_classes.add(data_type)
      # TODO: Remove prints below
      # print(ast.dump(node, include_attributes=True, annotate_fields=True))
      # print(py_resolved_type)
      # print(data_type)
      # print("**********\n")

  def check_and_cast_to_custom_type(self, data_type):
    if not data_type:
      return None
    elif type(data_type) == types_block.BaseType and self.is_local_class(data_type.name):
      return types_block.CustomType.to_custom_type(data_type, self.file_path)
    elif type(data_type) in [types_block.PrimitiveType, types_block.FileType]:
      return data_type
    elif type(data_type) == types_block.CustomType:
      if data_type.parameters:
        for p in data_type.parameters:
          p.types = [self.check_and_cast_to_custom_type(t_i) for t_i in p.types]
      return data_type
    elif type(data_type) == types_block.SystemType:
      if data_type.parameters:
        data_type.parameters = [set([self.check_and_cast_to_custom_type(param_type)
                                     for param_type in list(i_parameters)])
                                for i_parameters in data_type.parameters]
      return data_type
    elif type(data_type) in [types_block.ListType, types_block.SetType, types_block.TupleType]:
      if data_type.types:
        data_type.types = [self.check_and_cast_to_custom_type(t) for t in data_type.types]
      return data_type
    elif type(data_type) == types_block.DictType:
      if data_type.key_types:
        data_type.key_types = [self.check_and_cast_to_custom_type(t) for t in data_type.key_types]
      if data_type.val_types:
        data_type.val_types = [self.check_and_cast_to_custom_type(t) for t in data_type.val_types]
      return data_type
    else:
      # TODO: Handle other non system libraries here
      return None
      # raise RuntimeError("@COSAL: Unsupported data type '%s'" % type(data_type).__name__)

  def visit_FunctionDef(self, node, meta):
    scope = self.create_scope(node.name)
    args = node.args.args
    variables = []
    for arg in args:
      variables.append(self.add_variable(arg.id, position_block.Position.get_position(arg), a_consts.VAR_TYPE.ARG))
    default_positions = []
    if node.args.defaults:
      for default in node.args.defaults:
        default_positions.append(position_block.Position.get_position(default))
    if default_positions:
      var_index = 0
      for position in default_positions:
        while var_index < len(variables):
          if var_index == len(variables) - 1:
            variables[var_index].set_is_default_arg_set(True)
          elif variables[var_index].get_first_position() < position < variables[var_index + 1].get_first_position():
            variables[var_index].set_is_default_arg_set(True)
          var_index += 1
    if method_block.is_constructor(node.name):
      class_name = scope.parent.name
      if class_name in self.classes:
        self.classes[class_name].constructor_params = method_block.get_parameters(node, skip_self=True)
    for child in node.body:
      self.visit(child, meta)
    self._current_scope = scope.parent

  def visit_ClassDef(self, node, meta):
    scope = self.create_scope(node.name)
    clazz = class_block.Class.load(node, file_source=self.file_path, scope=scope)
    self.classes[clazz.name] = clazz
    for child in node.body:
      self.visit(child, meta)
    self._current_scope = scope.parent

  def dump(self, store_name):
    json_dict = {}
    for scope, variables in self.scope_variable_map.items():
      json_dict[str(scope)] = variables
    cache.store_json(json_dict, store_name)

  def update_danglings(self):
    for scope in self.scopes.values():
      for var_name, positions in scope.get_danglings().items():
        par_scope = scope.parent
        while par_scope and par_scope in self.scope_variable_map:
          if var_name in self.scope_variable_map[par_scope]:
            self.scope_variable_map[par_scope][var_name].positions.update(positions)
            break
          par_scope = par_scope.parent
      scope.set_danglings({})

  def parse(self):
    source_code = cache.read_file(self.file_path)
    tree = ast.parse(source_code)
    self.tree = tree
    self.visit(tree)
    self.update_danglings()
    return self

  def parse_pytype(self):
    source_code = self._source_code if self._source_code else cache.read_file(self.file_path)
    tree = type_checker.annotate(source_code)
    try:
      ast_tokenized = asttokens.ASTTokens(source_code, tree=tree)
      tree = ast_tokenized.tree
    except ValueError as ignored:
      pass
    self.tree = tree
    self.visit(tree)
    self.update_danglings()
    return self

  def update_classes(self):
    if self._valid_custom_classes is not None:
      return self._valid_custom_classes
    self._valid_custom_classes = []
    for class_name, clazz in self.classes.items():
      if not clazz.scope_str:
        continue
      constructor_scope = self.scopes[clazz.scope_str].children.get("__init__", None)
      scope_variables = self.scope_variable_map[constructor_scope]
      is_valid_constructor = True
      for param in clazz.constructor_params:
        param_variable = scope_variables[param.name]
        if param_variable.types:
          param.types = param_variable.types
        param.has_default_value = param_variable.is_default_arg_set()
        if not param.is_valid():
          is_valid_constructor = False
          break
      if is_valid_constructor:
        self._valid_custom_classes.append(clazz)
      # print(clazz)
      # exit()
    return self._valid_custom_classes

  def get_system_classes(self):
    return self.system_classes

  def print_variables(self):
    for scope, variable_map in self.scope_variable_map.items():
      print("\n\n### Scope: %s\n" % str(scope))
      for variable in variable_map.values():
        print("Variable: %s, Type: %s" % (variable.name, variable.type and variable.type.name))
        print("Positions: ", variable.positions)
        print("Store Positions: ", variable.get_store_positions())
        print("Update Positions: ", variable.get_updated_positions())


