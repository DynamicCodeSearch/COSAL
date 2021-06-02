import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.blocks import class_block
from analysis.blocks import method as method_block
from analysis.blocks import parameter as parameter_block
from analysis.blocks import position as position_block
from analysis.blocks import types as types_block
from analysis.blocks import specific_types as stypes_block
from analysis.blocks import variable as variable_block
from analysis.helpers import helper, file_utils
from store import mongo_store
from utils import cache

import properties


def get_py_class_store():
  if properties.STORE == "mongo":
    return mongo_store.PyClassStore()
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


"""
****** START BSON ******
"""

"""
Classes
"""


def from_class_bson(bson_dict):
  clazz = class_block.Class(bson_dict["name"])
  clazz.file_source = cache.get_absolute_path(bson_dict["file_source"])
  if "start_pos" in bson_dict:
    clazz.start_pos = position_block.Position.from_bson(bson_dict["start_pos"])
  if "end_pos" in bson_dict:
    clazz.end_pos = position_block.Position.from_bson(bson_dict["end_pos"])
  if "scope_str" in bson_dict:
    clazz.scope_str = bson_dict["scope_str"]
  if "constructor_params" in bson_dict:
    clazz.constructor_params = [from_parameter_bson(param)
                                for param in bson_dict["constructor_params"]]
  return clazz


"""
Methods
"""


def from_generated_function_bson(bson_dict):
  """

  :param bson_dict: A dictionary in JSON format
  :return: Instance of GeneratedFunction
  """
  gen_func = method_block.GeneratedFunction()
  gen_func.name = bson_dict["name"]
  gen_func.is_whole_method = bson_dict.get("is_whole_method", False)
  gen_func.original_function_name = bson_dict.get("original_function_name", None)
  gen_func.source_code_function_name = bson_dict.get("source_code_function_name", None)
  gen_func.source_code_class_name = bson_dict.get("source_code_class_name", None)
  gen_func.source_file = cache.get_absolute_path(bson_dict["source_file"])
  gen_func.generated_file = cache.get_absolute_path(bson_dict["generated_file"])
  gen_func.body = bson_dict["body"]
  gen_func.input_key = bson_dict.get("input_key", None)
  params_json = bson_dict.get("parameters", None)
  if params_json:
    gen_func.parameters = {
      name: from_specific_parameter_bson(var_json) for name, var_json in params_json.items()
    }
  args_permutation = bson_dict.get("args_permutation", None)
  if args_permutation:
    gen_func.args_permutation = method_block.GeneratedFunction.decode_args_permutation(args_permutation)
  return gen_func


def convert_to_function_arguments(generated_func, args, arg_index):
  name_arg_type_map = {}
  for type_key, arg_names in generated_func.args_permutation.items():
    for arg_name in arg_names:
      sub_keys = extract_keys(type_key)
      arg_val = args[type_key].pop(0) if len(sub_keys) == 1 else [args[sk].pop(0) for sk in sub_keys]
      name_arg_type_map[arg_name] = {
        "type": type_key,
        "arg": arg_val
      }
  func_args = []
  func_id = generated_func.name
  parameters = sorted(generated_func.parameters.values(), key=lambda x: x.index)
  for param in parameters:
    func_args.append(convert_to_function_argument(param.type, param.name, name_arg_type_map, func_id, arg_index))
  return func_args


"""
Parameters and Variables
"""


def convert_to_function_argument(arg_type, arg_name, name_arg_type_map, func_id, arg_index):
  arg_type_class_name = arg_type.get_obj_type()
  if arg_type_class_name == stypes_block.PrimitiveSpecificType.__name__:
    return stypes_block.PrimitiveSpecificType.to_py_val(
      name_arg_type_map[arg_name]["type"],
      name_arg_type_map[arg_name]["arg"]
    )
  elif arg_type_class_name == stypes_block.CustomSpecificType.__name__:
    constructor_vals = []
    for parameter in arg_type.parameters:
      param_type = parameter.type
      param_name = "%s.%s" % (arg_name, parameter.name)
      constructor_vals.append(
        convert_to_function_argument(param_type, param_name, name_arg_type_map, func_id, arg_index)
      )
    clazz = helper.load_class(arg_type.file_path, arg_type.name)
    return clazz(*constructor_vals)
  elif arg_type_class_name == stypes_block.SystemSpecificType.__name__:
    arg_vals = name_arg_type_map[arg_name]["arg"]
    params = []
    for t in arg_type.parameter_types:
      params.append(
        convert_to_function_argument_from_value(arg_vals, t, func_id, arg_index)
      )
    clazz = helper.load_class_from_module(arg_type.module, arg_type.name)
    return clazz(*params)
  elif arg_type_class_name == stypes_block.ListSpecificType.__name__:
    arg_vals = name_arg_type_map[arg_name]["arg"]
    converted = []
    for arg_val in arg_vals:
      converted.append(
        convert_to_function_argument_from_value(arg_val, arg_type.type, func_id, arg_index)
      )
    return converted
  elif arg_type_class_name == stypes_block.SetSpecificType.__name__:
    arg_vals = name_arg_type_map[arg_name]["arg"]
    converted = set()
    for arg_val in arg_vals:
      converted.add(
        convert_to_function_argument_from_value(arg_val, arg_type.type, func_id, arg_index)
      )
    return converted
  elif arg_type_class_name == stypes_block.TupleSpecificType.__name__:
    arg_vals = name_arg_type_map[arg_name]["arg"]
    converted = []
    for typ in arg_type.types:
      converted.append(
        convert_to_function_argument_from_value(arg_vals, typ, func_id, arg_index)
      )
    converted = tuple(converted)
    return converted
  elif arg_type_class_name == stypes_block.DictSpecificType.__name__:
    arg_vals = name_arg_type_map[arg_name]["arg"]
    d = {}
    for arg_val in arg_vals:
      key = convert_to_function_argument_from_value(arg_val, arg_type.key_type, func_id, arg_index)
      val = convert_to_function_argument_from_value(arg_val, arg_type.val_type, func_id, arg_index)
      d[key] = val
    return d
  elif arg_type_class_name == stypes_block.FileSpecificType.__name__:
    file_content = name_arg_type_map[arg_name]["arg"]
    file_type = "%s.%s" % (arg_type.module, arg_type.name)
    return file_utils.convert_to_file_input(file_content, file_type, func_id, arg_index)
  else:
    raise RuntimeError("@COSAL: Complete this dodo!")


def convert_to_function_argument_from_value(value, arg_type, func_id, arg_index):
  arg_type_class_name = arg_type.get_obj_type()
  if arg_type_class_name == stypes_block.PrimitiveSpecificType.__name__:
    val = value
    while isinstance(val, list):
      val = val.pop(0)
    # val = value.pop(0) if isinstance(value, list) else value
    py_val = stypes_block.PrimitiveSpecificType.to_py_val(arg_type.get_generic_name(), val)
    return py_val
  elif arg_type_class_name == stypes_block.CustomSpecificType.__name__:
    constructor_vals = []
    for param in sorted(arg_type.parameters, key=lambda x: x.index):
      param_value = value.pop(0)
      param_type = param.type
      constructor_vals.append(
        convert_to_function_argument_from_value(param_value, param_type, func_id, arg_index)
      )
    clazz = helper.load_class(arg_type.file_path, arg_type.name)
    return clazz(*constructor_vals)
  elif arg_type_class_name == stypes_block.SystemSpecificType.__name__:
    params = []
    for t in arg_type.parameter_types:
      params.append(
        convert_to_function_argument_from_value(value, t, func_id, arg_index)
      )
    clazz = helper.load_class_from_module(arg_type.module, arg_type.name)
    return clazz(*params)
  elif arg_type_class_name == stypes_block.ListSpecificType.__name__:
    arg_vals = value
    converted = []
    for arg_val in arg_vals:
      if not isinstance(arg_val, list):
        arg_val = [arg_val]
      converted.append(
        convert_to_function_argument_from_value(arg_val, arg_type.type, func_id, arg_index)
      )
    return converted
  elif arg_type_class_name == stypes_block.SetSpecificType.__name__:
    arg_vals = value
    converted = set()
    for arg_val in arg_vals:
      if not isinstance(arg_val, list):
        arg_val = [arg_val]
      converted.add(
        convert_to_function_argument_from_value(arg_val, arg_type.type, func_id, arg_index)
      )
    return converted
  elif arg_type_class_name == stypes_block.TupleSpecificType.__name__:
    arg_vals = value
    converted = []
    for typ in arg_type.types:
      converted.append(
        convert_to_function_argument_from_value(arg_vals, typ, func_id, arg_index)
      )
    converted = tuple(converted)
    return converted
  elif arg_type_class_name == stypes_block.DictSpecificType.__name__:
    arg_vals = value
    d = {}
    for arg_val in arg_vals:
      key = convert_to_function_argument_from_value(arg_val, arg_type.key_type, func_id, arg_index)
      val = convert_to_function_argument_from_value(arg_val, arg_type.val_type, func_id, arg_index)
      d[key] = val
    return d
  elif arg_type_class_name == stypes_block.FileSpecificType.__name__:
    file_type = "%s.%s" % (arg_type.module, arg_type.name)
    return file_utils.convert_to_file_input(value, file_type, func_id, arg_index)
  else:
    raise RuntimeError("@COSAL: Complete this dodo!")


def from_parameter_bson(bson_dict):
  param = parameter_block.Parameter(bson_dict["name"], bson_dict["index"])
  param.has_default_value = bson_dict["has_default_value"]
  if "types" in bson_dict:
    param.types = [from_types_bson(typ) for typ in bson_dict["types"]]
  return param


def from_specific_parameter_bson(bson_dict):
  param = parameter_block.SpecificParameter(bson_dict["name"], bson_dict["index"])
  param.has_default_value = bson_dict["has_default_value"]
  if "type" in bson_dict:
    param.type = from_types_bson(bson_dict["type"])
  return param


def from_variable_bson(bson_dict, scope):
  positions = [position_block.Position.from_bson(pos) for pos in bson_dict['positions']]
  variable = variable_block.Variable(str(bson_dict['name']), scope, str(bson_dict['var_type']), positions)
  if "type" in bson_dict:
    variable.type = from_types_bson(bson_dict['type'])
  if "_store_positions" in bson_dict:
    variable._store_positions = set([position_block.Position.from_bson(p) for p in bson_dict['_store_positions']])
  if "_updated_positions" in bson_dict:
    variable._updated_positions = set([position_block.Position.from_bson(p)
                                       for p in bson_dict['_updated_positions']])
  return variable


def from_specific_variable_bson(bson_dict, scope=None):
  return variable_block.SpecificVariable(
    name=bson_dict["name"],
    index=bson_dict["index"],
    scope=scope,
    var_type=bson_dict["var_type"],
    positions=bson_dict.get("positions", None),
    data_type=from_types_bson(bson_dict.get("type", None))
  )


def is_custom_type(parameter):
  return parameter.type and isinstance(parameter.type, stypes_block.CustomSpecificType)


def is_custom_class(val, source_file):
  return get_py_class_store().load_custom_class(source_file, val.__class__.__name__) is not None


def is_system_class(val):
  return get_py_class_store().load_system_class(val.__class__.__module__, val.__class__.__name__) is not None


"""
Types
"""


def to_type_key(arg_type):
  return arg_type.arg_meta_to_str(arg_type.get_arg_meta())


def from_types_bson(bson_dict):
  if bson_dict is None:
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
  o = types_block.BaseType()
  o.name = str(bson_dict['name'])
  if "module" in bson_dict:
    o.module = str(bson_dict['module'])
  o.is_valid = bson_dict['is_valid']
  return o


def from_BaseSpecificType_bson(bson_dict):
  o = stypes_block.BaseSpecificType()
  o.name = str(bson_dict['name'])
  if "module" in bson_dict:
    o.module = str(bson_dict['module'])
  o.is_valid = bson_dict['is_valid']
  return o


def from_PrimitiveType_bson(bson_dict):
  return types_block.PrimitiveType(name=str(bson_dict['name']))


def from_PrimitiveSpecificType_bson(bson_dict):
  return stypes_block.PrimitiveSpecificType(name=str(bson_dict['name']))


def from_CustomType_bson(bson_dict):
  name, file_path = bson_dict["name"], cache.get_absolute_path(bson_dict["file_source"])
  o = types_block.CustomType(name, file_path=file_path)
  params_json = bson_dict.get('parameters', None)
  if params_json:
    o.parameters = [from_parameter_bson(param_json) for param_json in params_json]
  is_valid = True
  for param in o.parameters:
    if not param.is_valid():
      is_valid = False
      break
  o.is_valid = is_valid and len(o.parameters) > 0
  return o


def from_CustomSpecificType_bson(bson_dict):
  name, file_path = bson_dict["name"], cache.get_absolute_path(bson_dict["file_source"])
  o = stypes_block.CustomSpecificType(name, file_path=file_path)
  params_bson = bson_dict.get('parameters', None)
  if params_bson:
    o.parameters = [from_specific_parameter_bson(param_bson) for param_bson in params_bson]
  o.is_valid = bson_dict["is_valid"]
  return o


def from_SystemType_bson(bson_dict):
  name, module = bson_dict["name"], bson_dict.get("module", None)
  o = types_block.SystemType(name, module)
  o.is_valid = bson_dict['is_valid']
  params_bson = bson_dict.get('parameters', None)
  if params_bson:
    o.parameters = [[from_types_bson(p_i) for p_i in param] for param in params_bson]
  return o


def from_SystemSpecificType_bson(bson_dict):
  name, module = bson_dict["name"], bson_dict.get("module", None)
  o = stypes_block.SystemSpecificType(name, module)
  o.is_valid = bson_dict['is_valid']
  params_bson = bson_dict.get('parameters', None)
  if params_bson:
    o.parameter_types = [from_types_bson(param) for param in params_bson]
  return o


def from_FileType_bson(bson_dict):
  return types_block.FileType(name=bson_dict["name"], module=bson_dict.get("module", None))


def from_FileSpecificType_bson(bson_dict):
  return stypes_block.FileSpecificType(name=bson_dict["name"], module=bson_dict.get("module", None))


def from_ListType_bson(bson_dict):
  o = types_block.ListType()
  o.is_valid = bson_dict['is_valid']
  o.types = [from_types_bson(typ) for typ in bson_dict['types']] if 'types' in bson_dict else None
  return o


def from_ListSpecificType_bson(bson_dict):
  o = stypes_block.ListSpecificType()
  o.is_valid = bson_dict["is_valid"]
  type_bson = bson_dict.get("type", None)
  if type_bson:
    o.type = from_types_bson(type_bson)
  return o


def from_SetType_bson(bson_dict):
  o = types_block.SetType()
  o.is_valid = bson_dict['is_valid']
  o.types = [from_types_bson(typ) for typ in bson_dict['types']] if 'types' in bson_dict else None
  return o


def from_SetSpecificType_bson(bson_dict):
  o = stypes_block.SetSpecificType()
  o.is_valid = bson_dict["is_valid"]
  type_bson = bson_dict.get("type", None)
  if type_bson:
    o.type = from_types_bson(type_bson)
  return o


def from_DictType_bson(bson_dict):
  o = types_block.DictType()
  o.is_valid = bson_dict['is_valid']
  o.key_types = [from_types_bson(typ) for typ in bson_dict['key_types']] if 'key_types' in bson_dict else None
  o.val_types = [from_types_bson(typ) for typ in bson_dict['val_types']] if 'val_types' in bson_dict else None
  return o


def from_DictSpecificType_bson(bson_dict):
  o = stypes_block.DictSpecificType()
  o.is_valid = bson_dict["is_valid"]
  key_type_bson = bson_dict.get("key_type", None)
  if key_type_bson:
    o.key_type = from_types_bson(key_type_bson)
  val_type_bson = bson_dict.get("val_type", None)
  if val_type_bson:
    o.val_type = from_types_bson(val_type_bson)
  return o


def from_TupleType_bson(bson_dict):
  o = types_block.TupleType()
  o.is_valid = bson_dict['is_valid']
  o.types = [from_types_bson(t) for t in bson_dict['types']] if 'types' in bson_dict else None
  return o


def from_TupleSpecificType_bson(bson_dict):
  o = stypes_block.TupleSpecificType()
  o.is_valid = bson_dict['is_valid']
  o.types = [from_types_bson(t) for t in bson_dict['types']] if 'types' in bson_dict else None
  return o


"""
****** END BSON ******
"""

"""
****** START UTILS ******
"""


def extract_keys(grand_key):
  keys = []
  i, n = 0, len(grand_key)
  bracket_count = 0
  key = ""
  while i < n:
    c = grand_key[i]
    if c == ',' and bracket_count == 0:
      keys.append(key)
      key = ""
    elif c == '(':
      key += c
      bracket_count += 1
    elif c == ')':
      key += c
      bracket_count -= 1
      if bracket_count == 0:
        i += 1
        while i < n and grand_key[i] != ',':
          key += grand_key[i]
          i += 1
        keys.append(key)
        key = ""
    else:
      key += grand_key[i]
    i += 1
  if len(key) > 0:
    keys.append(key)
  return keys


def format_value_as_json(ret_val, gen_func, arg_index):
  if ret_val is None:
    return None
  ret_type = type(ret_val)
  func_id = gen_func.name
  if types_block.PrimitiveType.is_primitive(ret_type.__name__, ret_type.__module__):
    return ret_val
  elif types_block.FileType.is_file_type(ret_type.__name__, ret_type.__module__):
    return file_utils.convert_to_file_output(ret_val)
  elif isinstance(ret_val, list) or isinstance(ret_val, set) or isinstance(ret_val, tuple):
    return [format_value_as_json(r, gen_func, arg_index) for r in ret_val]
  elif isinstance(ret_val, dict):
    d = {}
    for k, v in ret_val.items():
      key = format_value_as_json(k, gen_func, arg_index)
      val = format_value_as_json(v, gen_func, arg_index)
      d[key] = val
    return d
  elif is_custom_class(ret_val, gen_func.source_file):
    return format_value_as_json(ret_val.__dict__, gen_func, arg_index)
  elif is_system_class(ret_val):
    if hasattr(ret_val, "__dict__") and ret_val.__dict__:
      return format_value_as_json(ret_val.__dict__, gen_func, arg_index)
    else:
      return str(ret_val)


# def is_same_objects(val1, val2, gen_func):
#   if type(val1) != type(val2):
#     return False
#   val_type = type(val1)
#   if types_block.PrimitiveType.is_primitive(val_type.__name__, val_type.__module__):
#     return val1 == val2
#   elif isinstance(val_type, list) or isinstance(val_type, set) or isinstance(val_type, tuple):
#     if len(val1) != len(val2):
#       return False
#     for v1, v2 in zip(val1)

"""
****** END UTILS ******
"""

"""
****** START TYPE EXPANSION ******
"""
