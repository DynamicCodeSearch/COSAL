import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from copy import deepcopy
import signal
import time

from store import mongo_store
from utils import cache, logger
from analysis.blocks import block_utils
from analysis.helpers import constants as a_consts
from haskell.db_store.function_store import FunctionStore
from haskell.executions import ffi_based
from haskell.type_checking import haskell_type_checker
import properties


DEBUG = False
LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
HASKELL_SRC_ROOT_FOLDER = os.path.join(properties.CONFIG.CODE_HOME, "src", "main", "haskell")


def get_argument_store():
  """
  Retrieve argument store
  :return: Implementation of `base_store.ArgumentStore`
  """
  if properties.STORE == "mongo":
    return mongo_store.ArgumentStore(properties.CONFIG.get_dataset())
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def convert_to_function_arguments(haskell_func, args, arg_index):
  arg_index_type_map = {}
  for type_key, arg_indices in haskell_func.args_permutation.items():
    for arg_index in arg_indices:
      sub_keys = block_utils.extract_keys(type_key)
      arg_val = args[type_key].pop(0) if len(sub_keys) == 1 else [args[sk].pop(0) for sk in sub_keys]
      arg_index_type_map[arg_index] = {
        "type": type_key,
        "arg": arg_val
      }
  func_args = []
  func_id = haskell_func.name
  parameters = [haskell_func.parameters[arg_index] for arg_index in sorted(haskell_func.parameters.keys())]
  for param_index, param in enumerate(parameters):
    func_args.append(convert_to_function_argument(param, param_index, arg_index_type_map[param_index]))
  return func_args


def convert_to_function_argument(arg_type, arg_name, arg_index_type_map):
  arg_type_class_name = arg_type.get_obj_type()
  if arg_type_class_name == haskell_type_checker.PrimitiveType.__name__:
    return haskell_type_checker.PrimitiveType.to_py_val(arg_index_type_map["type"],
                                                        arg_index_type_map["arg"])
  elif arg_type_class_name == haskell_type_checker.ArrayType.__name__:
    arg_vals = arg_index_type_map["arg"]
    converted = []
    for arg_val in arg_vals:
      converted.append(
        convert_to_function_argument_from_value(arg_val, arg_type.type)
      )
    return converted
  elif arg_type_class_name == haskell_type_checker.TupleType.__name__:
    arg_vals = arg_index_type_map["arg"]
    converted = []
    for typ in arg_type.types:
      converted.append(
        convert_to_function_argument_from_value(arg_vals, typ)
      )
    return converted
  else:
    raise RuntimeError("@COSAL: Complete this dodo!")


def convert_to_function_argument_from_value(value, arg_type):
  arg_type_class_name = arg_type.get_obj_type()
  if arg_type_class_name == haskell_type_checker.PrimitiveType.__name__:
    val = value
    while isinstance(val, list):
      val = val.pop(0)
    py_val = haskell_type_checker.PrimitiveType.to_py_val(arg_type.get_generic_name(), val)
    return py_val
  elif arg_type_class_name == haskell_type_checker.ArrayType.__name__:
    arg_vals = value
    converted = []
    for arg_val in arg_vals:
      if not isinstance(arg_val, list):
        arg_val = [arg_val]
      converted.append(
        convert_to_function_argument_from_value(arg_val, arg_type.type)
      )
    return converted
  elif arg_type_class_name == haskell_type_checker.TupleType.__name__:
    arg_vals = value
    converted = []
    for typ in arg_type.types:
      converted.append(
        convert_to_function_argument_from_value(arg_vals, typ)
      )
    converted = tuple(converted)
    return converted
  else:
    raise RuntimeError("@COSAL: Complete this dodo!")


def load_arguments(func):
  arg_data_obj = get_argument_store().load_args(func.input_key)
  if arg_data_obj is None:
    contents = cache.run_sh(["sh", "scripts/java/engines/argument_generation.sh",
                             func.input_key, str(properties.FUZZ_ARGUMENT_SIZE)],
                            properties.CONFIG.CODE_HOME)
    if not (contents and "SLACC args saved successfully!!" in str(contents)):
      raise RuntimeError("func_name: '%s'; Input_Key: '%s' \n%s"
                         % (func.name, func.input_key, contents))
    arg_data_obj = get_argument_store().load_args(func.input_key)
  if arg_data_obj is None:
    raise RuntimeError("Failed for fetch arguments for '%s' and key '%s'"
                       % (func.name, func.input_key))
  arg_data = arg_data_obj["args"]
  all_func_args = []
  for arg_index, arg in enumerate(arg_data):
    func_args = convert_to_function_arguments(func, arg, arg_index)
    all_func_args.append(func_args)
  return all_func_args


def get_file_header(base_module, export_module):
  file_header_template = """
{-# LANGUAGE ForeignFunctionInterface #-}
{-# LANGUAGE TemplateHaskell #-}

module %s where

import           Data.ByteString (ByteString)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Lazy as BSL
import qualified Data.MessagePack as MSG
import Foreign.C

import FFI.Anything.TypeUncurry.Msgpack

import %s as BasePack
  """
  return file_header_template % (export_module, base_module)


def validate_function(func_str, base_module, base_file_name, parent_folder_path):
  export_module = base_module + "TmpSLACCExport"
  export_file_name = base_file_name + "TmpSLACCExport"
  export_file_path = os.path.join(parent_folder_path, "%s.hs" % export_file_name)
  cache.delete_file(export_file_path)
  file_header = get_file_header(base_module, export_module)
  file_contents = file_header + "\n\n" + func_str
  cache.write_file(export_file_path, file_contents)
  executable_path = os.path.join(parent_folder_path, "%s.dylib" % export_file_name)
  validity = ffi_based.create_executable(export_file_path, executable_path, HASKELL_SRC_ROOT_FOLDER, delete_executable=True)
  cache.delete_file(export_file_path)
  return validity


def create_executable_hs_export_file(function_group, force_create=False):
  base_file_path = function_group["filePath"]
  base_module = function_group["module"]
  func_names = function_group["funcNames"]
  folder_path = cache.get_parent_folder(base_file_path)
  base_file_name = cache.get_file_name(base_file_path)
  export_module = base_module + ffi_based.SLACC_EXPORT_FILE_SUFFIX
  export_file_name = base_file_name + ffi_based.SLACC_EXPORT_FILE_SUFFIX
  export_file_path = os.path.join(folder_path, "%s.hs" % export_file_name)
  executable_path = os.path.join(folder_path, "%s.dylib" % export_file_name)
  if not force_create and cache.file_exists(executable_path):
    LOGGER.info("Executable exists for '%s'. Moving on .... " % base_file_path)
    return executable_path
  function_template = """
foreign export ccall %s%s :: CString -> IO CString
%s%s = export BasePack.%s
  """
  file_header = get_file_header(base_module, export_module)
  func_exports = []
  for func_name in func_names:
    func_export = function_template % (func_name, ffi_based.SLACC_EXPORT_HS, func_name, ffi_based.SLACC_EXPORT_HS, func_name)
    func_validity = validate_function(func_export, base_module, base_file_name, folder_path)
    if func_validity:
      func_exports.append(func_export)
    else:
      print(func_name)
    # print(func_name, func_validity)
  file_content = "%s\n\n%s" % (file_header, "\n\n".join(func_exports))
  cache.write_file(export_file_path, file_content)
  file_validity = ffi_based.create_executable(export_file_path, executable_path, HASKELL_SRC_ROOT_FOLDER, delete_executable=False)
  assert file_validity
  return executable_path


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
  duration = a_consts.METHOD_WAIT_TIMEOUT * 10
  return_variable, error_message = None, None
  try:
    start = time.time()
    return_variable = func(*cloned)
    duration = (time.time() - start) * 10
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


def format_value_as_json(ret_val):
  if ret_val is None:
    return None
  ret_type = type(ret_val)
  if haskell_type_checker.PrimitiveType.is_primitive_py_type(ret_type.__name__, ret_type.__module__):
    return ret_val
  elif isinstance(ret_val, list) or isinstance(ret_val, set) or isinstance(ret_val, tuple):
    return [format_value_as_json(r) for r in ret_val]
  else:
    return str(ret_val)


def execute(func, executable_path):
  func_obj = ffi_based.load_function(func.source_code_function_name, executable_path)
  function_store = FunctionStore(properties.CONFIG.get_dataset())
  if not func_obj:
    if DEBUG:
      LOGGER.warn("Permutation '%s' of func '%s' is not executable. Moving on ... "
                  % (func.name, func.source_code_function_name))
    return None
  args = load_arguments(func)
  results = []
  for arg_index, arg in enumerate(args):
    if DEBUG:
      LOGGER.info("Running for %d of %d args" % (arg_index + 1, len(args)))
    exec_results = execute_function(func_obj, arg)
    exec_results["return"] = format_value_as_json(exec_results["return"])
    results.append(exec_results)
  func_json = {
    "name": func.name,
    "fileName": cache.get_repo_local_path(func.file_path),
    "dataset": properties.CONFIG.get_dataset(),
    "inputKey": func.input_key
  }
  # print(func.source_code_function_name, func.name, len(results))
  if not results:
    LOGGER.warning("Function '%s' from file '%s' is not valid"
                   % (func.name, func.file_path))
    function_store.save_failed_hs_function(func_json)
    return None
  else:
    func_json["outputs"] = results
    function_store.save_success_hs_function(func_json)
    return func_json
