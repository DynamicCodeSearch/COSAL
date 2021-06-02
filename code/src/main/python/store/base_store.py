import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O


class InputStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_inputs(self, args_key):
    raise NotImplementedError("Should be implemented in subclass")

  @staticmethod
  def is_array(arg_sets):
    if not type(arg_sets[0]) is list:
      return False
    return len(arg_sets[0]) != len(arg_sets[1]) != len(arg_sets[2])


class FunctionStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_function(self, function_name):
    raise NotImplementedError("Should be implemented in subclass")

  def load_functions(self, function_names=None, limit=None):
    raise NotImplementedError("Should be implemented in subclass")

  def load_all_metadata(self, limit=None):
    raise NotImplementedError("Should be implemented in subclass")

  def load_java_generated_functions(self, limit=None):
    raise NotImplementedError("Should be implemented in subclass")

  def load_metadata(self, function_name):
    raise NotImplementedError("Should be implemented in subclass")

  def update_py_function_metadata(self, function_json):
    raise NotImplementedError("Should be implemented in subclass")

  def load_py_function_metadata(self, function_name):
    raise NotImplementedError("Should be implemented in subclass")

  def load_py_functions_metadata(self, file_path):
    raise NotImplementedError("Should be implemented in subclass")

  def del_all_py_functions_metadata(self):
    raise NotImplementedError("Should be implemented in subclass")

  def load_py_generated_functions(self):
    raise NotImplementedError("Should be implemented in subclass")

  def load_py_functions_from_names(self, function_names):
    raise NotImplementedError("Should be implemented in subclass")

  def del_py_function_metadata(self, function_name):
    raise NotImplementedError("Should be implemented in subclass")

  def del_py_functions_metadata(self, file_path):
    raise NotImplementedError("Should be implemented in subclass")

  def get_generated_file(self, source_file_path):
    raise NotImplementedError("Should be implemented in subclass")

  def save_py_function(self, function_json):
    raise NotImplementedError("Should be implemented")

  def load_py_function(self, function_name):
    raise NotImplementedError("Should be implemented")

  def del_all_py_functions(self):
    raise NotImplementedError("Should be implemented in subclass")

  def exists_py_function(self, function_json):
    raise NotImplementedError("Should be implemented")

  def save_failed_py_function(self, function_json):
    raise NotImplementedError("Should be implemented")

  def is_invalid_py_function(self, function_name):
    raise NotImplementedError("Should be implemented")

  def load_py_functions(self):
    raise NotImplementedError("Should be implemented")

  def save_py_metadata(self, func_json):
    raise NotImplementedError("Should be implemented")

  def load_py_metadata(self, function_name):
    raise NotImplementedError("Should be implemented")

  @staticmethod
  def is_object_return(metadata):
    """
    Is the return type of object
    :param metadata:
    :return:
    """
    return not metadata["isArray"] and not metadata["isPrimitive"]

  @staticmethod
  def get_return_vals(returns):
    return_keys = []

    def get_key(d):
      keys = []
      for k in d.keys():
        if isinstance(d[k], dict):
          keys += ["%s.%s" % (k, k_i) for k_i in get_key(d[k])]
        else:
          keys.append(k)
      return keys

    def get_value(d):
      values = []
      for k in d.keys():
        if isinstance(d[k], dict):
          values += get_value(d[k])
        else:
          values.append(d[k])
      return values

    for ret in returns:
      if ret is None: continue
      return_keys = get_key(ret)
      break
    ret_vals_dict = {k: [] for k in return_keys}
    for ret in returns:
      if ret is None:
        for k in return_keys:
          ret_vals_dict[k].append(None)
      else:
        for k, v in zip(return_keys, get_value(ret)):
          ret_vals_dict[k].append(v)
    return ret_vals_dict


class PyFileMetaStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_meta(self, file_name):
    raise NotImplementedError("Should be implemented in subclass")

  def save_meta(self, bson_dict):
    raise NotImplementedError("Should be implemented in subclass")

  def del_meta(self, file_path):
    raise NotImplementedError("Should be implemented in subclass")


class ArgumentStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_args(self, arg_key):
    raise NotImplementedError("Should be implemented in subclass")


class ExecutionStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset


class ClusterStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def save_difference(self, difference, clustering_error):
    raise NotImplementedError("Should be implemented in subclass")

  def load_differences(self, clustering_error):
    raise NotImplementedError("Should be implemented in subclass")

  def count_differences(self, clustering_error):
    raise NotImplementedError("Should be implemented in subclass")

  def save_clusters(self, cluster, suffix):
    raise NotImplementedError("Should be implemented in subclass")

  def register_completed_function(self, function_name, clustering_error):
    raise NotImplementedError("Should be implemented in subclass")

  def get_completed_functions(self, clustering_error):
    raise NotImplementedError("Should be implemented in subclass")


class SystemClassStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def is_valid_class(self, project, class_key):
    raise NotImplementedError("Should be implemented in subclass")

  def get_class(self, project, class_key):
    raise NotImplementedError("Should be implemented in subclass")


class PyClassStore(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def is_valid_system_class(self, module, name):
    raise NotImplementedError("Should be implemented in subclass")

  def load_system_class(self, module, name):
    raise NotImplementedError("Should be implemented in subclass")

  def save_system_class(self, system_class):
    raise NotImplementedError("Should be implemented in subclass")

  def load_custom_class(self, file_source, name):
    raise NotImplementedError("Should be implemented in subclass")

  def save_custom_class(self, custom_class):
    raise NotImplementedError("Should be implemented in subclass")


class TokenStore(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def save_tokens(self, token_json):
    raise NotImplementedError("Should be implemented in subclass")

  def save_contextual_tokens(self, context_json):
    raise NotImplementedError("Should be implemented in subclass")

  def get_contextual_tokens(self, language=None):
    raise NotImplementedError("Should be implemented in subclass")

  def sample_documents(self, language, sample_size):
    raise NotImplementedError("Should be implemented in subclass")

  def get_tokens(self, language=None):
    raise NotImplementedError("Should be implemented in subclass")