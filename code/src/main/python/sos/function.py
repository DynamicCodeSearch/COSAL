import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O
from store import json_store, mongo_store
from analysis.helpers import helper as analysis_helper
from sos.types import Primitive
import properties

__SYSTEM_CLASS_STORE = None


def get_system_class_store(dataset):
  global __SYSTEM_CLASS_STORE
  if __SYSTEM_CLASS_STORE is None:
    if properties.STORE == "json":
      __SYSTEM_CLASS_STORE = json_store.SystemClassStore(dataset)
    elif properties.STORE == "mongo":
      __SYSTEM_CLASS_STORE = mongo_store.SystemClassStore(dataset)
  return __SYSTEM_CLASS_STORE


def get_store(dataset):
  if properties.STORE == "json":
    return json_store.InputStore(dataset)
  elif properties.STORE == "mongo":
    return mongo_store.InputStore(dataset)
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


class InputCache(O):
  _cache = {}
  _store = None

  @staticmethod
  def load(dataset, key):
    if key in InputCache._cache:
      return InputCache._cache[key]
    if not InputCache._store or InputCache._store.dataset != dataset:
      InputCache._store = get_store(dataset)
    arguments = InputCache._store.load_inputs(key)
    InputCache._cache[key] = arguments
    return arguments


class Function(O):
  _id = 0

  def __init__(self, **kwargs):
    Function._id += 1
    self.id = Function._id
    self.name = None
    self.body = None
    self.dataset = None
    self.package = None
    self.className = None
    self.source = None
    self.source_file = None
    self.lines_touched = None
    self.span = None
    self.input_key = None
    self.return_attribute = None
    self.outputs = None
    self.args_permutation = None
    # Meta-info
    self.useful = None
    self.is_cloned = False
    self.base_name = None
    O.__init__(self, **kwargs)

  def clone(self):
    new = Function()
    for key in self.has().keys():
      if key in ["id", "name"]:
        continue
      else:
        new[key] = self[key]
    new.base_name = self.name
    new.name = analysis_helper.generate_function_name()
    new.is_cloned = True
    return new

  def deep_clone(self):
    new = Function()
    for key in self.has().keys():
      new[key] = self[key]
    return new

  @staticmethod
  def match_values(val1, val2):
    return val1 == val2

  def is_valid_function(self):
    if self.useful is not None:
      return self.useful
    # inputs = InputCache.load(self.dataset, self.input_key)
    # if inputs is None:
    #   self.useful = False
    #   return self.useful
    self.useful = False
    prev_result_match = True
    for return_index, retrn in enumerate(self.outputs.returns):
      if return_index > 0 and prev_result_match:
        prev_result_match = Function.match_values(retrn, self.outputs.returns[return_index - 1])
      if not prev_result_match:
        self.useful = True
    return self.useful


  def is_useful(self):
    # TODO: check usefulness of function
    if self.useful is not None:
      return self.useful
    inputs = InputCache.load(self.dataset, self.input_key)
    # No inputs found
    if inputs is None:
      self.useful = False
      return self.useful
    only_none = True
    return_not_nones_indices = []
    last_return_value = None
    returns_same_value = True
    for i, retrn in enumerate(self.outputs.returns):
      if retrn is not None:
        only_none = False
        if last_return_value is None:
          last_return_value = retrn
        elif returns_same_value and last_return_value != retrn:
          returns_same_value = False
        return_not_nones_indices.append(i)
    # If outputs contain only None
    if only_none:
      self.useful = False
      return self.useful
    # If it returns same value
    if returns_same_value:
      self.useful = False
      return self.useful
    # If contains non return indices
    if len(return_not_nones_indices) == 0:
      self.useful = False
      return self.useful
    # Check if any of the args are the same as the return types
    for input_arg in inputs:
      is_valid_input = False
      for i in return_not_nones_indices:
        if input_arg[i] != self.outputs.returns[i]:
          is_valid_input = True
          break
      if not is_valid_input:
        self.useful = False
        return self.useful
    self.useful = True
    return self.useful

  def __hash__(self):
    return self.id


class Outputs(O):
  DEFAULT_KEY = "__slacc_default_output"

  def __init__(self, outputs_json=None, output_meta=None, **kwargs):
    O.__init__(self, **kwargs)
    self.returns = []
    self.errors = []
    self.durations = []
    self.is_all_same = False
    if outputs_json is not None:
      for output_json in outputs_json:
        if output_meta and "return" in output_json and output_json.get("return", None) is not None:
          ret = format_return(output_json["return"], output_meta["key"], output_meta["arrayDimensions"])
          if not isinstance(ret, dict):
            ret = {
              Outputs.DEFAULT_KEY: ret
            }
        else:
          ret = {
            Outputs.DEFAULT_KEY: output_json.get("return", None)
          }
        self.returns.append(ret)
        self.errors.append(output_json["errorMessage"] if "errorMessage" in output_json else None)
        self.durations.append(output_json["duration"] if "duration" in output_json else None)

  def clone(self):
    new = Outputs()
    new.returns = self.returns[:]
    new.errors = self.errors[:]
    new.durations = self.durations[:]
    new.is_all_same = self.is_all_same
    return new

  def subset(self, start, end):
    new = Outputs()
    new.returns = self.returns[start:end]
    new.errors = self.errors[start:end]
    new.durations = self.durations[start:end]
    new.is_all_same = self.is_all_same
    return new


def format_return(return_val, return_type, array_dimensions):
  if array_dimensions == 0:
    if Primitive.is_valid_type(return_type):
      return return_val
    else:
      dataset = properties.CONFIG.get_dataset()
      project = properties.CONFIG.get_project_name()
      system_class_store = get_system_class_store(dataset)
      clazz_json = system_class_store.get_class(project, return_type)
      rets = {}
      for variable in clazz_json["variables"]:
        var_name = variable["name"]
        if "primitive" in variable:
          var_type = variable["primitive"]
        else:
          var_type = "%s.%s" % (variable["packageName"], variable["type"])
        # TODO: Recurse tomorrow!
        var_rets = format_return(return_val[var_name], var_type, variable["arrayDimensions"])
        if isinstance(var_rets, dict):
          for k in var_rets.keys():
            rets["%s.%s" % (var_name, k)] = var_rets[k]
        else:
          rets[var_name] = var_rets
      return rets
  else:
    return [(format_return(return_val_i, return_type, array_dimensions - 1)) for return_val_i in return_val]


class FunctionCache(O):
  __STORE = {}
  __FAILED_FUNCTIONS = set()

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  @staticmethod
  def store_function(funct):
    FunctionCache.__STORE[funct.name] = funct

  @staticmethod
  def load_function(funct_name):
    return FunctionCache.__STORE.get(funct_name, None)

  @staticmethod
  def load_functions():
    return FunctionCache.__STORE.values()

  @staticmethod
  def get_function_names():
    return FunctionCache.__STORE.keys()

  @staticmethod
  def is_failed_function(funct_name):
    return funct_name in FunctionCache.__FAILED_FUNCTIONS

  @staticmethod
  def store_failed_function(funct_name):
    FunctionCache.__FAILED_FUNCTIONS.add(funct_name)

  @staticmethod
  def size():
    return len(FunctionCache.__STORE)


