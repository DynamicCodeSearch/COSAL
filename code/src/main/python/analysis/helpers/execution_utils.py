import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from copy import deepcopy
import signal
import time

from analysis.blocks import block_utils
from analysis.helpers import constants as a_consts
from store import mongo_store, json_store
from utils import maths, cache
import properties


def get_function_store():
  """
  Retrieve function store
  :return: Implementation of `base_store.FunctionStore`
  """
  if properties.STORE == "mongo":
    return mongo_store.FunctionStore(properties.CONFIG.get_dataset())
  elif properties.STORE == "json":
    return json_store.FunctionStore(properties.CONFIG.get_dataset())
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def get_argument_store():
  """
  Retrieve argument store
  :return: Implementation of `base_store.ArgumentStore`
  """
  if properties.STORE == "mongo":
    return mongo_store.ArgumentStore(properties.CONFIG.get_dataset())
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def load_generated_functions_meta(file_path):
  """
  Load generated functions metadata from file path
  :param file_path: Path of generated file
  :return: {func_name: instance of GeneratedFunction}
  """
  gen_funcs_meta = {}
  for function_metadata in get_function_store().load_py_functions_metadata(file_path):
    gen_func_meta = block_utils.from_generated_function_bson(function_metadata)
    gen_funcs_meta[gen_func_meta.name] = gen_func_meta
  return gen_funcs_meta


def load_generated_functions_from_db():
  """
  Load generated functions metadata from database
  :return: Iterable of generated functions
  """
  return get_function_store().load_py_generated_functions()


def get_function_args(generated_func):
  """
  Retrieve function arguments for generated function
  :param generated_func: Instance of `method.GeneratedFunction`
  :return: [[arg_a, arg_b] * `properties.FUZZ_ARGUMENT_SIZE`]
  """
  arg_data_obj = get_argument_store().load_args(generated_func.input_key)
  if arg_data_obj is None:
    contents = cache.run_sh(["sh", "scripts/java/engines/argument_generation.sh",
                             generated_func.input_key, str(properties.FUZZ_ARGUMENT_SIZE)],
                            properties.CONFIG.CODE_HOME)
    if not (contents and "SLACC args saved successfully!!" in contents):
      raise RuntimeError("func_name: '%s'; Input_Key: '%s' \n%s"
                         % (generated_func.name, generated_func.input_key, contents))
    arg_data_obj = get_argument_store().load_args(generated_func.input_key)
  if arg_data_obj is None:
    raise RuntimeError("Failed for fetch arguments for '%s' and key '%s'"
                       % (generated_func.name, generated_func.input_key))
  arg_data = arg_data_obj["args"]
  all_func_args = []
  for arg_index, arg in enumerate(arg_data):
    func_args = block_utils.convert_to_function_arguments(generated_func, arg, arg_index)
    all_func_args.append(func_args)
  return all_func_args


def get_parameter_arg_and_key(parameter):
  """
  Get list of dicts where each dict represents name and key for the parameter
  :param parameter: Instance of `parameter.SpecificParameter`
  :return: [{"name": <arg_name>, "key": <arg_key>}]
  """
  if not parameter.type:
    return None
  if block_utils.is_custom_type(parameter):
    arg_and_key_lst = []
    for param in parameter.type.parameters:
      param_arg_and_key_lst = get_parameter_arg_and_key(param)
      for param_arg_and_key in param_arg_and_key_lst:
        param_arg_and_key["name"] = "%s.%s" % (parameter.name, param_arg_and_key["name"])
        arg_and_key_lst.append(param_arg_and_key)
    return arg_and_key_lst
  else:
    arg_and_key = {
      "name": parameter.name,
      "key": block_utils.to_type_key(parameter.type)
    }
    return [arg_and_key]


def get_function_arg_and_key(generated_function):
  """
  Get list of dicts where each dict represents name and key for the function args
  :param generated_function: Instance of `method.GeneratedFunction`
  :return: [{"name": <arg_name>, "key": <arg_key>}]
  """
  if not generated_function.parameters:
    return None
  function_arg_and_key = []
  for param_name, parameter in generated_function.parameters.items():
    parameter_arg_and_keys = get_parameter_arg_and_key(parameter)
    if parameter_arg_and_keys:
      function_arg_and_key += parameter_arg_and_keys
  if not function_arg_and_key:
    return None
  return function_arg_and_key


def group_arg_and_key(parameter_arg_and_keys):
  """
  Group argnames based on key
  :param parameter_arg_and_keys: [{"name": <arg_name>, "key": <arg_key>}]
  :return: {"<arg_key>": [<arg_name1>, <arg_name2>]}
  """
  keys_argnames_dict = {}
  for parameter_arg_and_key in parameter_arg_and_keys:
    typ = parameter_arg_and_key["key"]
    name = parameter_arg_and_key["name"]
    if typ in keys_argnames_dict:
      keys_argnames_dict[typ].append(name)
    else:
      keys_argnames_dict[typ] = [name]
  return keys_argnames_dict


def get_function_args_key(keys_argnames_dict):
  """
  Get the input arg key for function give the args key
  :param keys_argnames_dict: {"<arg_key>": [<arg_name1>, <arg_name2>]}
  :return: "<arg_key1>##num_args"
  """
  keys = sorted(keys_argnames_dict.keys())
  key_count = {}
  for k in keys:
    for sk in block_utils.extract_keys(k):
      cnt = len(keys_argnames_dict[k])
      if sk in key_count:
        key_count[sk] += cnt
      else:
        key_count[sk] = cnt
  keys = sorted(key_count.keys())
  arg_keys = []
  for key in keys:
    arg_keys.append("%s##%d" % (key, key_count[key]))
  return ",".join(arg_keys)


def permutate_args_and_key(key_argnames_dict):
  """
  Permutate args and key for dict
  :param key_argnames_dict: {"<arg_key>": [<arg_name1>, <arg_name2>]}
  :return: List of list of args where each inner list is a permutation
  """
  permutations = []
  type_group_permutations = {}
  for key, argnames in key_argnames_dict.items():
    type_group_permutations[key] = maths.permutate_list(argnames)
  for typ in type_group_permutations.keys():
    type_permutations = type_group_permutations[typ]
    this_permutations = []
    for type_permutation in type_permutations:
      if len(permutations) == 0:
        this_permutations.append({
          typ: type_permutation
        })
      else:
        for permutation in permutations:
          this_permutation = deepcopy(permutation)
          this_permutation[typ] = type_permutation
          this_permutations.append(this_permutation)
    permutations = this_permutations
  return permutations


def has_too_many_arguments(grouped_arg_keys):
  """
  Return true if there are too many arguments
  :param grouped_arg_keys: {<type>: [List of arg names]}
  :return: True if there are too many arguments
  """
  arg_length = 0
  for k, vs in grouped_arg_keys.items():
    arg_length += len(vs)
  return arg_length > properties.MAX_ARGUMENT_SIZE


"""
Executions
"""


class TimeoutException(Exception):
  pass


def timeout_handler(signum, frame):
  raise TimeoutException


def execute_function(func, arg):
  """
  Execute function on arguments
  :param func: Instance of function
  :param arg: arguments to execute function on
  :return: {
    "return": ...,
    "errorMessage": ...,
    "duration": ...
  }
  """
  cloned = [deepcopy(x) for x in arg]
  prev_signal = signal.getsignal(signal.SIGALRM)
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(a_consts.METHOD_WAIT_TIMEOUT)
  duration = a_consts.METHOD_WAIT_TIMEOUT * 1000
  return_variable, error_message = None, None
  try:
    start = time.time()
    return_variable = func(*cloned)
    duration = (time.time() - start) * 1000
  except TimeoutException:
    error_message = "Method timed out after %d seconds" % a_consts.METHOD_WAIT_TIMEOUT
  except Exception as e:
    error_message = e.message
  signal.alarm(0)
  signal.signal(signal.SIGALRM, prev_signal)
  return {
    "return": return_variable,
    "errorMessage": error_message,
    "duration": duration
  }


# def create_arg_keys(func):
#   """
#   Create keys for each argument of fucntion
#   :param func: Instance of `method.GeneratedFunction`
#   :return: [key for each arg]
#   """
#   store = get_function_store()
#   func_bson = store.load_py_function_metadata(func.__name__)
#   if not func_bson:
#     return None
#   arg_names = helper.get_func_arg_names(func)
#   if not arg_names:
#     return None
#   arg_keys = []
#   for arg_name in arg_names:
#     arg_bson = func_bson['parameters'][arg_name]
#     arg_key = create_arg_key(arg_bson)
#     if arg_key is None:
#       return None
#     arg_keys.append(arg_key)
#   return arg_keys
#
#
# def create_arg_key(arg_bson):
#   parameter = block_utils.from_specific_parameter_bson(arg_bson)
#   if not parameter.type:
#     return False
#   return block_utils.to_type_key(parameter.type)

if __name__ == "__main__":
  print(get_function_args_key({'float': [u'c'], 'int,float,(int,float)@1': [u'a']}))
