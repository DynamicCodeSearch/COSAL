import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from haskell.type_checking import haskell_type_checker
from analysis.helpers import execution_utils, helper
from utils import cache
from utils.lib import O


class HaskellFunction(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.name = helper.generate_function_name()
    self.source_code_function_name = None
    self.module = None
    self.file_path = None
    self.def_string = None
    self.parameters = None
    self.return_type = None
    self.input_key = None
    self.args_permutation = None

  def clone(self):
    cloned = HaskellFunction()
    for k, v in self.__dict__.items():
      cloned.__dict__[k] = v
    cloned.name = helper.generate_function_name()
    return cloned

  def to_bson(self):
    d = {
      "name": self.name,
      "isWholeMethod": True,
      "sourceCodeFunctionName": self.source_code_function_name,
      "module": self.module,
      "filePath": cache.get_repo_local_path(self.file_path),
      "defString": self.def_string,
      "parameters": None,
      "returnType": None,
      "inputKey": self.input_key,
      "argsPermutation": None
    }
    if self.parameters:
      d["parameters"] = {str(index): typ.to_bson() if typ else None for index, typ in self.parameters.items()}
    if self.args_permutation:
      d["argsPermutation"] = HaskellFunction.encode_args_permutation(self.args_permutation)
    if self.return_type:
      d["returnType"] = self.return_type.to_bson()
    return d

  @staticmethod
  def from_bson(bson_dict):
    hs_func = HaskellFunction()
    hs_func.name = bson_dict["name"]
    hs_func.source_code_function_name = bson_dict.get("sourceCodeFunctionName", None)
    hs_func.module = bson_dict.get("module", None)
    hs_func.file_path = bson_dict.get("filePath", None)
    hs_func.def_string = bson_dict.get("defString", None)
    hs_func.input_key = bson_dict.get("inputKey", None)
    params_json = bson_dict.get("parameters", None)
    if params_json:
      hs_func.parameters = {
        int(index): from_types_bson(type_json) for index, type_json in params_json.items()
      }
    args_permutation = cache.get_absolute_path(bson_dict.get("argsPermutation", None))
    if args_permutation:
      hs_func.args_permutation = HaskellFunction.decode_args_permutation(args_permutation)
    return hs_func

  def is_valid(self):
    return self.parameters is not None and self.return_type is not None

  # @staticmethod
  # def parse

  def get_input_args_types_as_str(self, format_type="dict"):
    """
    :param format_type: dict | lst | str
    :return:
    """
    if not self.parameters:
      return None
    if format_type == "dict":
      return {i: haskell_type_checker.BaseType.to_type_key(arg_type) for i, arg_type in self.parameters.items()}
    as_lst = [haskell_type_checker.BaseType.to_type_key(self.parameters[arg_index]) for arg_index in sorted(self.parameters.keys())]
    if format_type == "str":
      return str(as_lst)
    return as_lst

  def set_types(self, function_def_string):
    self.def_string = function_def_string.replace("\\n'", "")
    type_meta = haskell_type_checker.parse_type(self.def_string)
    # print(function_def_string)
    if not type_meta:
      return
    if type_meta["arg_types"]:
      self.parameters = {i: arg_type for i, arg_type in enumerate(type_meta["arg_types"])}
    self.return_type = type_meta["return_type"]
    self.input_key = self.get_input_key()
    # print(self.types)
    # print(self.return_type)
    # print("")

  def get_args_and_keys(self):
    input_arg_types = self.get_input_args_types_as_str(format_type="dict")
    if not input_arg_types:
      return None
    return [{"name": i, "key": arg_type} for i, arg_type in input_arg_types.items()]

  def _get_grouped_arg_keys(self):
    args_and_keys = self.get_args_and_keys()
    if not args_and_keys:
      return args_and_keys
    for arg_and_key in args_and_keys:
      if not arg_and_key["key"]:
        return None
    return execution_utils.group_arg_and_key(args_and_keys)

  def get_input_key(self):
    grouped_arg_keys = self._get_grouped_arg_keys()
    if not grouped_arg_keys or execution_utils.has_too_many_arguments(grouped_arg_keys):
      return None
    return execution_utils.get_function_args_key(grouped_arg_keys)

  def permutate_args(self):
    grouped_arg_keys = self._get_grouped_arg_keys()
    if grouped_arg_keys:
      return execution_utils.permutate_args_and_key(grouped_arg_keys)
    return None

  def __repr__(self):
    return """
    Name: %s
    Definition: %s
    Types: %s
    Return Type: %s
    Input Key: %s
    Args Permutation: %s
    """ % (self.name, self.def_string, self.get_input_args_types_as_str("str"),
           haskell_type_checker.BaseType.to_type_key(self.return_type) if self.return_type else None,
           self.input_key, self.args_permutation)

  @staticmethod
  def encode_args_permutation(permutation):
    return {k.replace(".", "$"): v for k, v in permutation.items()}

  @staticmethod
  def decode_args_permutation(permutation):
    return {k.replace("$", "."): v for k, v in permutation.items()}


def from_types_bson(bson_dict):
  if not bson_dict:
    return None
  slacc_type = bson_dict.get("slacc_type", None)
  if not slacc_type:
    raise RuntimeError("'slacc_type' key not found in bson_dict: %s" % bson_dict)
  method_name = "from_%s_bson" % slacc_type
  method_to_call = getattr(sys.modules[__name__], method_name, None)
  if not method_to_call:
    raise RuntimeError("@COSAL: Invalid slacc_type: '%s'" % slacc_type)
  return method_to_call(bson_dict)


def from_BaseType_bson(bson_dict):
  o = haskell_type_checker.BaseType(bson_dict["name"])
  o.is_valid = bson_dict['is_valid']
  return o


def from_PrimitiveType_bson(bson_dict):
  o = haskell_type_checker.PrimitiveType(bson_dict["name"])
  o.is_valid = bson_dict['is_valid']
  return o


def from_ArrayType_bson(bson_dict):
  type_bson = bson_dict.get("type", None)
  typ = None
  if type_bson:
    typ = from_types_bson(type_bson)
  o = haskell_type_checker.ArrayType(typ)
  o.is_valid = bson_dict['is_valid']
  return o


def from_TupleType_bson(bson_dict):
  o = haskell_type_checker.TupleType()
  o.is_valid = bson_dict['is_valid']
  o.types = [from_types_bson(t) for t in bson_dict['types']] if 'types' in bson_dict else None
  return o


def permutate_function(haskell_function):
  args_permutations = haskell_function.permutate_args()
  if args_permutations is None:
    return [haskell_function]
  permutations = []
  for args_permutation in args_permutations:
    cloned = haskell_function.clone()
    cloned.args_permutation = args_permutation
    permutations.append(cloned)
  return permutations
