import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O

from analysis.helpers import file_utils


class BaseSpecificType(O):
  def __init__(self, name=None, module=None, **kwargs):
    self.name = name
    self.module = module
    self.is_valid = True
    self._arg_meta = None
    O.__init__(self, **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module])))

  def __eq__(self, other):
    if other is None or not isinstance(other, self.__class__):
      return False
    return hash(self) == hash(other)

  def to_bson(self):
    return {
      "slacc_type": self.get_obj_type(),
      "name": self.name,
      "module": self.module,
      "is_valid": self.is_valid
    }

  def get_arg_meta(self):
    raise NotImplementedError("Must be implemented in sub class.")

  def arg_meta_to_str(self, arg_meta):
    if not arg_meta:
      return None
    dims = arg_meta.get("arr_dims", 0)
    if dims == 0:
      return arg_meta["type"]
    else:
      return "(%s)@%d" % (arg_meta["type"], dims)

  def clone(self):
    return BaseSpecificType(name=self.name, module=self.module)


class PrimitiveSpecificType(BaseSpecificType):
  __PY_TO_GENERIC__ = {
    "int": "int",
    "float": "float",
    "bool": "boolean",
    "str": "string"
  }

  __GENERIC_TO_PY__ = {
    "int": "int",
    "float": "float",
    "boolean": "bool",
    "string": "str"
  }

  __GENERIC_CONVERSION_FUNC__ = {
    "int": int,
    "float": float,
    "boolean": bool,
    "string": str
  }

  def __init__(self, name, **kwargs):
    BaseSpecificType.__init__(self, name=name, module="__builtin__", **kwargs)

  def get_arg_meta(self):
    return {
      "type": PrimitiveSpecificType.to_generic_name(self.name),
      "arr_dims": 0
    }

  def get_generic_name(self):
    return PrimitiveSpecificType.to_generic_name(self.name)

  @staticmethod
  def to_generic_name(name):
    return PrimitiveSpecificType.__PY_TO_GENERIC__[name]

  @staticmethod
  def to_py_name(name):
    return PrimitiveSpecificType.__GENERIC_TO_PY__[name]

  @staticmethod
  def to_py_val(name, value):
    try:
      return PrimitiveSpecificType.__GENERIC_CONVERSION_FUNC__[name](value)
    except UnicodeEncodeError:
      return value

  def clone(self):
    return PrimitiveSpecificType(self.name)


class CustomSpecificType(BaseSpecificType):
  def __init__(self, name, file_path=None, **kwargs):
    self.file_path = file_path
    self.parameters = []
    BaseSpecificType.__init__(self, name=name, **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.parameters])))

  def to_bson(self):
    contents = super(CustomSpecificType, self).to_bson()
    contents["file_source"] = self.file_path
    contents["parameters"] = [param.to_bson() for param in self.parameters]
    is_valid = True
    for param in self.parameters:
      if not param.is_valid():
        is_valid = False
        break
    is_valid = is_valid and len(self.parameters) > 0
    contents["is_valid"] = is_valid
    return contents

  def get_arg_meta(self):
    param_strs = []
    for p in self.parameters:
      if p and p.type:
        param_strs.append(p.type.get_arg_meta())
    if len(param_strs) == 0:
      return None
    elif param_strs == 1:
      return param_strs[0]
    else:
      param_str = ",".join(map(self.arg_meta_to_str, param_strs))
      return {
        "type": param_str,
        "arr_dims": 0
      }

  def clone(self):
    cloned = CustomSpecificType(self.name, file_path=self.file_path)
    cloned.parameters = [param.clone() for param in self.parameters]
    return cloned


class SystemSpecificType(BaseSpecificType):
  def __init__(self, name, module, **kwargs):
    self.parameter_types = []
    BaseSpecificType.__init__(self, name=name, module=module, **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.parameter_types])))

  def to_bson(self):
    contents = super(SystemSpecificType, self).to_bson()
    contents["parameters"] = [pt.to_bson() for pt in self.parameter_types] if self.parameter_types else None
    contents["is_valid"] = len(self.parameter_types) > 0 and all([pt.is_valid for pt in self.parameter_types])
    return contents

  def get_arg_meta(self):
    param_strs = []
    for pt in self.parameter_types:
      if pt:
        param_strs.append(pt.get_arg_meta())
    if len(param_strs) == 0:
      return None
    elif param_strs == 1:
      return param_strs[0]
    else:
      param_str = ",".join(map(self.arg_meta_to_str, param_strs))
      return {
        "type": param_str,
        "arr_dims": 0
      }

  def clone(self):
    cloned = SystemSpecificType(self.name, self.module)
    cloned.parameter_types = [pt.clone() for pt in self.parameter_types]
    return cloned


class FileSpecificType(BaseSpecificType):
  def __init__(self, name, module, **kwargs):
    BaseSpecificType.__init__(self, name=name, module=module, **kwargs)

  def get_arg_meta(self):
    return {
      "type": file_utils.FILE_INPUT_TYPE,
      "arr_dims": 0
    }

  def clone(self):
    return FileSpecificType(self.name, self.module)


class ListSpecificType(BaseSpecificType):
  def __init__(self, **kwargs):
    self.type = None
    BaseSpecificType.__init__(self, name="list", module="__builtin__", **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.type])))

  def to_bson(self):
    contents = super(ListSpecificType, self).to_bson()
    contents["type"] = self.type.to_bson() if self.type else None
    contents["is_valid"] = self.type is not None and self.type.is_valid
    return contents

  def get_arg_meta(self):
    if not self.type:
      return None
    arg_meta = self.type.get_arg_meta()
    arg_meta["arr_dims"] += 1
    return arg_meta

  def clone(self):
    cloned = ListSpecificType()
    if self.type:
      cloned.type = self.type.clone()
    return cloned

class SetSpecificType(ListSpecificType):
  def __init__(self, **kwargs):
    ListSpecificType.__init__(self, **kwargs)
    self.name = "set"

  def clone(self):
    cloned = SetSpecificType()
    if self.type:
      cloned.type = self.type.clone()
    return cloned


class DictSpecificType(BaseSpecificType):
  def __init__(self, **kwargs):
    self.key_type = None
    self.val_type = None
    BaseSpecificType.__init__(self, name="dict", module="__builtin__", **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.key_type, self.val_type])))

  def to_bson(self):
    contents = super(DictSpecificType, self).to_bson()
    contents["key_type"] = self.key_type.to_bson() if self.key_type else None
    contents["val_type"] = self.val_type.to_bson() if self.val_type else None
    contents["is_valid"] = self.key_type is not None and self.val_type is not None \
                           and self.key_type.is_valid and self.val_type.is_valid
    return contents

  def get_arg_meta(self):
    if not self.key_type or not self.val_type:
      return None
    key_arg_meta_str = self.arg_meta_to_str(self.key_type.get_arg_meta())
    val_arg_meta_str = self.arg_meta_to_str(self.val_type.get_arg_meta())
    return {
      "type": "%s,%s" % (key_arg_meta_str, val_arg_meta_str),
      "arr_dims": 1
    }

  def clone(self):
    cloned = DictSpecificType()
    if self.key_type:
      cloned.key_type = self.key_type.clone()
    if self.val_type:
      cloned.val_type = self.val_type.clone()
    return cloned


class TupleSpecificType(BaseSpecificType):
  def __init__(self, **kwargs):
    self.types = []
    BaseSpecificType.__init__(self, name="tuple", module="__builtin__", **kwargs)

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.module, self.types])))

  def to_bson(self):
    contents = super(TupleSpecificType, self).to_bson()
    contents["types"] = []
    for t in self.types:
      if t.is_valid:
        contents["types"].append(t.to_bson())
    # contents["types"] = self.type.to_bson() if self.type else None
    contents["is_valid"] = len(self.types) > 0 and all([t.is_valid for t in self.types])
    return contents

  def get_arg_meta(self):
    type_strs = []
    for typ in self.types:
      if typ:
        type_strs.append(typ.get_arg_meta())
    if len(type_strs) == 0:
      return None
    elif type_strs == 1:
      return type_strs[0]
    else:
      type_str = ",".join(map(self.arg_meta_to_str, type_strs))
      return {
        # "type": map(self.arg_meta_to_str, type_strs),
        "type": type_str,
        "arr_dims": 0
      }

  def clone(self):
    cloned = TupleSpecificType()
    cloned.types = [typ.clone() for typ in self.types]
    return cloned
