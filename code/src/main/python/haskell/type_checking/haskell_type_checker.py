import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from lark import Lark, Tree

from utils.lib import O

TYPE_SIGNATURE_GRAMMAR = """
  start: (context "=>")? arg_types ret_type
  context: bracketed_context | unbracketed_context
  unbracketed_context: class_name var_name
  bracketed_context: "(" unbracketed_context ("," unbracketed_context)* ")"
  class_name: WORD
  var_name: WORD
  arg_types: (arg_type "->")*
  arg_type: array_type | tuple_type | simple_type
  array_type: "[" arg_type "]"
  tuple_type: "(" arg_type ("," arg_type)* ")"
  simple_type: WORD
  ret_type: arg_type
  
  %import common.WORD
  %import common.WS
  %ignore WS
"""


def get_haskell_type_parser():
  return Lark(TYPE_SIGNATURE_GRAMMAR)


class TypeVisitor(O):
  def __init__(self, **updates):
    O.__init__(self, **updates)
    self.var_map = {}
    self.    arg_types = []
    self.return_type = None

  def visit(self, node):
    visitor_name = ("visit_" + node.data) if node.data else None
    default_visitor = self.generic_visit
    visitor = getattr(self, visitor_name, default_visitor)
    return visitor(node)

  def generic_visit(self, node):
    if not node:
      return None
    for child in node.children:
      if isinstance(child, Tree):
        self.visit(child)
    return None

  def visit_unbracketed_context(self, node):
    class_name = node.children[0].children[0].value
    var_name = node.children[1].children[0].value
    self.var_map[var_name] = class_name
    return None

  def visit_arg_types(self, node):
    args = []
    for child in node.children:
      args.append(self.visit(child))
    self.arg_types = args
    return None

  def visit_arg_type(self, node):
    return self.visit(node.children[0])

  def visit_simple_type(self, node):
    return_name = node.children[0].value
    type_str = self.var_map.get(return_name, return_name)
    if PrimitiveType.is_primitive_type(type_str):
      return PrimitiveType(type_str)
    else:
      return None

  def visit_array_type(self, node):
    child_type = self.visit(node.children[0])
    if child_type:
      return ArrayType(child_type)
    else:
      return None

  def visit_tuple_type(self, node):
    child_types = []
    for child in node.children:
      child_type = self.visit(child)
      if child_type:
        child_types.append(child_type)
      else:
        return None
    if child_types:
      return TupleType(child_types)
    return None

  def visit_ret_type(self, node):
    self.return_type = self.visit(node.children[0])
    return None


def parse_type(type_str):
  type_parser = get_haskell_type_parser()
  try:
    root_node = type_parser.parse(type_str)
    # print(root_node)
  except Exception as e:
    msg = str(e).split("\n")[0].strip()
    print("Exception while parsing type string '%s'. Error: '%s'" % (type_str, msg))
    return None
  visitor = TypeVisitor()
  visitor.visit(root_node)
  # print(visitor.var_map)
  # print(visitor.get_input_args_types_as_str())
  # print(visitor.return_type)
  return {
    "arg_types": visitor.arg_types,
    "return_type": visitor.return_type
  }


def _test_type_parser():
  parse_type("(Num a, Ord b) => a -> (a, b) -> Int")
  # parse_type("IO()")


class BaseType(O):
  def __init__(self, name, **kwargs):
    self.name = name
    O.__init__(self, **kwargs)

  def to_bson(self):
    return {
      "slacc_type": self.get_obj_type(),
      "name": self.name
    }

  def is_valid(self):
    return False

  def arg_meta_to_str(self, arg_meta):
    if not arg_meta:
      return None
    dims = arg_meta.get("arr_dims", 0)
    if dims == 0:
      return arg_meta["type"]
    else:
      return "(%s)@%d" % (arg_meta["type"], dims)

  def get_arg_meta(self):
    raise NotImplementedError("To be implemented in subclass .....")

  @staticmethod
  def to_type_key(arg_type):
    if not arg_type:
      return None
    arg_meta = arg_type.get_arg_meta()
    if not arg_meta:
      return None
    dims = arg_meta.get("arr_dims", 0)
    if dims == 0:
      return arg_meta["type"]
    else:
      return "(%s)@%d" % (arg_meta["type"], dims)


class PrimitiveType(BaseType):
  __HS_TO_GENERIC__ = {
    "Bool": "boolean",
    "Char": "char",
    "Eq": "int",
    "Ord": "int",
    "Int": "int",
    "Integral": "int",
    "Integer": "int",
    "Num": "float",
    "Real": "float",
    "RealFrac": "float",
    "Float": "float",
    "Double": "float",
  }

  __GENERIC_CONVERSION_FUNC__ = {
    "int": int,
    "float": float,
    "boolean": bool,
    "string": str,
    "char": chr
  }

  def __init__(self, name, **kwargs):
    BaseType.__init__(self, name, **kwargs)

  @staticmethod
  def to_generic_name(name):
    return PrimitiveType.__HS_TO_GENERIC__[name]

  def get_generic_name(self):
    return PrimitiveType.to_generic_name(self.name)

  def get_arg_meta(self):
    return {
      "type": PrimitiveType.to_generic_name(self.name),
      "arr_dims": 0
    }

  def is_valid(self):
    return True

  @staticmethod
  def is_primitive_type(hs_type):
    return hs_type in PrimitiveType.__HS_TO_GENERIC__

  @staticmethod
  def is_primitive_py_type(name, module):
    return (module is None or module == "__builtin__") and name in a_consts.PRIMITIVES

  @staticmethod
  def to_py_val(name, value):
    try:
      return PrimitiveType.__GENERIC_CONVERSION_FUNC__[name](value)
    except UnicodeEncodeError:
      return value


class ArrayType(BaseType):
  def __init__(self, base_type, **kwargs):
    self.type = base_type
    BaseType.__init__(self, name="array", **kwargs)

  def to_bson(self):
    contents = super(ArrayType, self).to_bson()
    contents["type"] = self.type.to_bson() if self.type else None
    return contents

  def get_arg_meta(self):
    if not self.type:
      return None
    arg_meta = self.type.get_arg_meta()
    if arg_meta["type"] == "char":
      arg_meta["type"] = "string"
    else:
      arg_meta["arr_dims"] += 1
    return arg_meta

  def is_valid(self):
    return self.type and self.type.is_valid()


class TupleType(BaseType):
  def __init__(self, base_types=None, **kwargs):
    if base_types:
      self.types = base_types
    else:
      self.types = []
    BaseType.__init__(self, name="tuple", **kwargs)

  def is_valid(self):
    if not self.types:
      return False
    for typ in self.types:
      if not typ.is_valid():
        return False
    return True

  def to_bson(self):
    contents = super(TupleType, self).to_bson()
    contents["types"] = []
    for t in self.types:
      contents["types"].append(t.to_bson())

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
        "type": type_str,
        "arr_dims": 0
      }


if __name__ == "__main__":
  _test_type_parser()
