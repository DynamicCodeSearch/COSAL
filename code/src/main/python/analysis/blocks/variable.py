import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import constants as a_consts
from analysis.blocks import types as types_block
from analysis.blocks import parameter as parameter_block
from utils.lib import O


class Variable(O):
  def __init__(self, name, scope, var_type, positions, **kwargs):
    self.name = name
    self._scope = scope
    self.var_type = var_type
    self.positions = positions
    self.types = set()
    self.type = None
    self._store_positions = set()
    self._updated_positions = set()
    self._prev_value = None
    self._is_type_set = False
    self._is_default_arg_set = False
    self._is_valid = None
    O.__init__(self, **kwargs)

  def to_bson(self):
    d = {
      "name": self.name,
      "scope": str(self.get_scope()),
      "var_type": self.var_type,
      "positions": [],
      "type": None,
      "types": None,
      "_store_positions": [],
      "_updated_positions": []
    }
    if self.type:
      d['type'] = self.type.to_bson()
    if self.types:
      d['types'] = [typ.to_bson() for typ in self.types]
    if self.positions:
      for position in self.positions:
        d['positions'].append(position.to_bson())
    if self._store_positions:
      for position in self._store_positions:
        d['_store_positions'].append(position.to_bson())
    if self._updated_positions:
      for position in self._updated_positions:
        d['_updated_positions'].append(position.to_bson())
    return d

  def is_valid(self):
    # if self._is_valid is not None:
    #   return self._is_valid
    if self.type:
      # self._is_valid = self.type.is_valid
      return self.type.is_valid
    if self.types:
      for typ in list(self.types):
        if typ.is_valid:
          # self._is_valid = True
          return True
    # self._is_valid = False
    return False

  def get_scope(self):
    return self._scope

  def is_type_set(self):
    return self._is_type_set

  def set_is_default_arg_set(self, is_default_arg_set):
    self._is_default_arg_set = is_default_arg_set

  def is_default_arg_set(self):
    return self._is_default_arg_set

  def get_prev_value(self):
    return self._prev_value

  def set_prev_value(self, prev_value):
    self._prev_value = prev_value

  def update_store_position(self, position):
    self._store_positions.add(position)

  def get_store_positions(self):
    return self._store_positions

  def update_updated_position(self, position):
    self._updated_positions.add(position)

  def get_updated_positions(self):
    return self._updated_positions

  def get_position_by_line(self, line_no):
    for position in self.positions:
      if position.line == line_no:
        return position
    return None

  def is_used_in_range(self, start, end):
    for position in sorted(self.positions):
      if start <= position <= end:
        return True
    return False

  def is_updated_in_range(self, start, end):
    for position in sorted(self.get_updated_positions()):
      if start <= position <= end:
        return True
    return False

  def is_argument(self, start, local_variables, line_numbers):
    if self.var_type == a_consts.VAR_TYPE.ARG:
      return True
    if self not in local_variables and not isinstance(self.type, types_block.BaseType):
      return True
    updated_positions = set()
    for pos in self.get_updated_positions():
      if pos.line in line_numbers:
        updated_positions.add(pos)
    return len(updated_positions) == 0 or sorted(updated_positions)[0] < start

  def has_visited(self, position):
    return position in self.get_updated_positions()

  def get_first_position(self):
    return sorted(self.positions)[0]

  def to_specific_variables(self):
    if not self.types:
      return False
    specific_variables = []
    for typ in self.types:
      expanded_types = typ.to_specific_types()
      if not expanded_types:
        continue
      for index, expanded_type in enumerate(expanded_types):
        specific_variables.append(
          SpecificVariable(
            name=self.name,
            index=index,
            scope=self._scope,
            var_type=self.var_type,
            positions=self.positions,
            data_type=expanded_type
          )
        )
    if not specific_variables:
      return None
    return specific_variables


class SpecificVariable(O):
  def __init__(self, name, index, scope, var_type, positions, data_type, **kwargs):
    self.name = name
    self.index = index
    self._scope = scope
    self.var_type = var_type
    self.positions = positions
    self.type = data_type
    O.__init__(self, **kwargs)

  def get_scope(self):
    return self._scope

  def is_valid(self):
    return self.type and self.type.is_valid()

  def to_specific_parameter(self):
    specific_parameter = parameter_block.SpecificParameter(name=self.name, index=self.index)
    specific_parameter.type = self.type
    return specific_parameter

  def to_bson(self):
    d = {
      "slacc_type": self.get_obj_type(),
      "name": self.name,
      "index": self.index,
      "scope": None,
      "var_type": self.var_type,
      # "positions": [],
      "type": None
    }
    if self._scope:
      d["scope"] = str(self._scope)
    if self.type:
      d['type'] = self.type.to_bson()
    # if self.positions:
    #   for position in self.positions:
    #     d['positions'].append(position.to_bson())
    return d


