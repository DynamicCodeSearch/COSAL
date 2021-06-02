import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.helpers import constants as a_consts
from analysis.blocks import specific_types as st
from utils.lib import O
from utils import maths


class BasicType(O):
  """
  Legacy. Should be removed!
  """
  def __init__(self, **kwargs):
    self.name = None
    self.is_primitive_type = None
    self.module = None  # Set only for non primitives
    self.is_valid = True
    O.__init__(self, **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.is_primitive_type, self.module, self.is_valid])))

  def __eq__(self, other):
    if other is None or not isinstance(other, BasicType):
      return False
    return hash(self) == hash(other)

  @staticmethod
  def get_type(value):
    var_type = BasicType()
    var_type.name = BaseType.get_name(value)
    var_type.is_primitive = PrimitiveType.is_primitive(var_type.name, None)
    if not var_type.is_primitive:
      var_type.module = BaseType.get_module(value)
    return var_type


class BaseType(O):
  def __init__(self, name=None, module=None, **kwargs):
    self.name = name
    self.module = module
    self.is_valid = True
    O.__init__(self, **kwargs)

  @staticmethod
  def get_name(value):
    return type(value).__name__

  @staticmethod
  def get_module(value):
    return type(value).__module__

  @staticmethod
  def is_none(value):
    return value is None

  @staticmethod
  def is_none_type(name, module):
    return (module is None or module == "__builtin__") and name == "None"

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module])))

  def __eq__(self, other):
    if other is None or not isinstance(other, self.__class__):
      return False
    return hash(self) == hash(other)

  def to_bson(self):
    return {
      "slacc_type": self.__class__.__name__,
      "name": self.name,
      "module": self.module,
      "is_valid": self.is_valid
    }

  def to_specific_types(self):
    raise NotImplementedError("Implement in subclass!")

  def check_validity(self):
    return self.is_valid

  def clone(self):
    return BaseType(name=self.name, module=self.module)


class PrimitiveType(BaseType):
  def __init__(self, name, **kwargs):
    BaseType.__init__(self, name=name, module="__builtin__", **kwargs)

  @staticmethod
  def is_primitive(name, module):
    return (module is None or module == "__builtin__") and name in a_consts.PRIMITIVES

  def to_specific_types(self):
    return [st.PrimitiveSpecificType(name=self.name)]

  def clone(self):
    return PrimitiveType(name=self.name)


class CustomType(BaseType):
  def __init__(self, name, file_path=None, **kwargs):
    BaseType.__init__(self, name=name, **kwargs)
    self.file_path = file_path
    self.parameters = []

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.parameters])))

  @staticmethod
  def to_custom_type(base_type, file_path):
    o = CustomType(base_type.name, file_path)
    return o

  def to_bson(self):
    contents = super(CustomType, self).to_bson()
    contents["file_source"] = self.file_path
    contents["parameters"] = [param.to_bson() for param in self.parameters]
    contents["is_valid"] = self.check_validity()
    return contents

  def check_validity(self):
    is_valid = True
    for param in self.parameters:
      if not param.is_valid():
        is_valid = False
        break
    return is_valid and len(self.parameters) > 0

  def to_specific_types(self):
    if not self.check_validity():
      return None
    specific_params = []
    for param in self.parameters:
      expanded_params = param.to_specific_parameters()
      if expanded_params:
        specific_params.append(expanded_params)
    if not specific_params:
      return None
    specific_types = []
    for params in maths.permutate_lists(specific_params):
      custom_specific_type = st.CustomSpecificType(name=self.name, file_path=self.file_path, parameters=params)
      specific_types.append(custom_specific_type)
    return specific_types

  def clone(self):
    cloned = CustomType(self.name, file_path=self.file_path)
    cloned.parameters = [param.clone() for param in self.parameters]
    return cloned


class SystemType(BaseType):
  def __init__(self, name, module, **kwargs):
    BaseType.__init__(self, name=name, module=module, **kwargs)
    self.parameters = []  # List of sets. Each list element contains possible types as a set!

  def clone(self):
    cloned = SystemType(self.name, self.module)
    if self.parameters:
      cloned.parameters = [set([param_type.clone() for param_type in list(i_parameters)]) for i_parameters in self.parameters]
    return cloned

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.parameters])))

  def check_validity(self):
    if not self.parameters:
      return False
    for i_parameters in self.parameters:
      any_valid = False
      for param in i_parameters:
        if param.check_validity():
          any_valid = True
          break
      if not any_valid:
        return False
    return True

  def to_bson(self):
    contents = super(SystemType, self).to_bson()
    contents["parameters"] = [[param_type.to_bson() for param_type in list(i_parameters)]
                              for i_parameters in self.parameters] if self.parameters else None
    contents["is_valid"] = self.check_validity()
    return contents

  def to_specific_types(self):
    if not self.check_validity():
      return False
    specific_params = []
    for i_parameters in self.parameters:
      extended_params = []
      for param_type in i_parameters:
        expanded = param_type.to_specific_types()
        if expanded:
          extended_params += expanded
      if extended_params:
        specific_params.append(extended_params)
    specs = []
    for param_types in maths.permutate_lists(specific_params):
      system_specific_type = st.SystemSpecificType(self.name, self.module, parameter_types=param_types)
      specs.append(system_specific_type)
    return specs


class FileType(BaseType):
  def __init__(self, name, module, **kwargs):
    BaseType.__init__(self, name=name, module=module, **kwargs)
    self.is_valid = FileType.is_file_type(name, module)

  @staticmethod
  def is_file_type(name, module):
    return name == "file" and module == "__builtin__"

  def to_specific_types(self):
    if not self.check_validity():
      return False
    return [st.FileSpecificType(self.name, self.module)]

  def clone(self):
    return FileType(self.name, self.module)


class ListType(BaseType):
  def __init__(self, **kwargs):
    self.types = []
    BaseType.__init__(self, name="list", module="__builtin__", **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.types])))

  def to_bson(self):
    contents = super(ListType, self).to_bson()
    contents["types"] = [typ.to_bson() for typ in self.types] if self.types else None
    contents["is_valid"] = self.types and len(self.types) > 0
    return contents

  def check_validity(self):
    if not self.types:
      return False
    for typ in self.types:
      if typ.check_validity():
        return True
    return False

  def to_specific_types(self):
    if not self.check_validity():
      return None
    specific_types = []
    for typ in self.types:
      expanded_types = typ.to_specific_types()
      if not expanded_types:
        continue
      for specific_type in expanded_types:
        lst_specific_type = st.ListSpecificType(type=specific_type)
        specific_types.append(lst_specific_type)
    if not specific_types:
      return None
    return specific_types

  def clone(self):
    cloned = ListType()
    cloned.types = [typ.clone() for typ in self.types]
    return cloned

  @staticmethod
  def get_type(value):
    var_type = ListType()
    ind_types = ListType.get_each_types(value)
    var_type.types = ind_types
    return var_type

  @staticmethod
  def get_each_types(value):
    types = set()
    for v_i in value:
      if v_i is not None:
        types.add(get_type(v_i))
    return types


class SetType(ListType):
  def __init__(self, **kwargs):
    ListType.__init__(self, **kwargs)
    self.name = "set"

  @staticmethod
  def get_type(value):
    var_type = ListType()
    ind_types = ListType.get_each_types(value)
    var_type.types = ind_types
    return var_type

  def to_specific_types(self):
    if not self.check_validity():
      return None
    specific_types = []
    for typ in self.types:
      expanded_types = typ.to_specific_types()
      if not expanded_types:
        continue
      for specific_type in expanded_types:
        set_specific_type = st.SetSpecificType(type=specific_type)
        specific_types.append(set_specific_type)
    if not specific_types:
      return None
    return specific_types

  def clone(self):
    cloned = SetType()
    cloned.types = [typ.clone() for typ in self.types]
    return cloned


class DictType(BaseType):
  def __init__(self, **kwargs):
    self.key_types = None
    self.val_types = None
    BaseType.__init__(self, name="dict", module="__builtin__", **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.key_types, self.val_types])))

  @staticmethod
  def get_type(value):
    var_type = DictType()
    key_types = ListType.get_each_types(value.keys())
    var_type.key_types = key_types
    val_types = ListType.get_each_types(value.values())
    var_type.val_types = val_types
    return var_type

  def to_bson(self):
    contents = super(DictType, self).to_bson()
    contents["key_types"] = [typ.to_bson() for typ in self.key_types] if self.key_types else None
    contents["val_types"] = [typ.to_bson() for typ in self.val_types] if self.val_types else None
    contents["is_valid"] = self.key_types and len(self.key_types) > 0 and self.val_types and len(self.val_types) > 0
    return contents

  def check_validity(self):
    if not self.key_types or not self.val_types:
      return False
    is_valid = True
    for typ in self.key_types:
      if not typ.check_validity():
        is_valid = False
        break
    if not is_valid:
      return False
    for typ in self.val_types:
      if not typ.check_validity():
        return False
    return True

  def to_specific_types(self):
    if not self.check_validity():
      return None
    key_types = []
    for k_type in self.key_types:
      if not k_type.check_validity():
        continue
      expanded_k_types = k_type.to_specific_types()
      if not expanded_k_types:
        continue
      for expanded_k_type in expanded_k_types:
        key_types.append(expanded_k_type)
    if not key_types:
      return None
    val_types = []
    for v_type in self.val_types:
      if not v_type.check_validity():
        continue
      expanded_v_types = v_type.to_specific_types()
      if not expanded_v_types:
        continue
      for expanded_v_type in expanded_v_types:
        val_types.append(expanded_v_type)
    if not val_types:
      return None
    specific_types = []
    for kv in maths.permutate_lists([key_types, val_types]):
      specific_types.append(st.DictSpecificType(key_type=kv[0], val_type=kv[1]))
    return specific_types

  def clone(self):
    cloned = DictType()
    if self.key_types:
      cloned.key_types = [typ.clone() for typ in self.key_types]
    if self.val_types:
      cloned.val_types = [typ.clone() for typ in self.val_types]
    return cloned


class TupleType(ListType):
  def __init__(self, **kwargs):
    ListType.__init__(self, **kwargs)
    self.name = "tuple"

  def to_bson(self):
    contents = super(TupleType, self).to_bson()
    contents["is_valid"] = self.check_validity()
    return contents

  @staticmethod
  def get_type(value):
    var_type = TupleType()
    for v_0 in value:
      var_type.types.append(get_type(v_0))
    return var_type

  def check_validity(self):
    if not self.types:
      return False
    for typ in self.types:
      if not typ.check_validity():
        return False
    return True

  def to_specific_types(self):
    if not self.check_validity():
      return None
    each_types = []
    for typ in self.types:
      expanded_types = typ.to_specific_types()
      if not expanded_types:
        return None
      i_each_types = []
      for expanded_type in expanded_types:
        # if expanded_type.check_validity():
        if expanded_type.is_valid:
          i_each_types.append(expanded_type)
      if not i_each_types:
        return None
      each_types.append(i_each_types)
    if not each_types:
      return None
    specific_types = []
    for type_permutation in maths.permutate_lists(each_types):
      specific_types.append(st.TupleSpecificType(types=type_permutation))
    return specific_types

  def clone(self):
    cloned = TupleType()
    cloned.types = [typ.clone() for typ in self.types]
    return cloned


def get_type(value):
  if BaseType.get_name(value) == "list":
    return ListType.get_type(value)
  elif BaseType.get_name(value) == "dict":
    return DictType.get_type(value)
  elif BaseType.get_name(value) == "tuple":
    return TupleType.get_type(value)
  else:
    return BasicType.get_type(value)


def is_valid_type(value):
  return BaseType.get_name(value) != "tuple"
