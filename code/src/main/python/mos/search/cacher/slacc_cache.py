import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search_store.code_store import ExecStore, MetaStore
from sos.function import Function, Outputs
from sos.cluster.multi_attribute_representative import multi_attribute_comparison
from utils import logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def group_executable_methods(all_executed, language):
  metadata = {}

  def get_metadata(source_file, original_function_name):
    orig_key = "%s::%s" % (source_file, original_function_name)
    if orig_key not in metadata:
      metadata[orig_key] = ExecStore().get_function_meta(language, source_file, original_function_name)
    return metadata[orig_key]

  method_groups = {}
  for i, executed in enumerate(all_executed):
    if i % 100 == 0:
      LOGGER.info("Fetching %d '%s' document ... " % (i + 1, language))
    file_path = executed["filePath"]
    method_key = executed["originalFunctionName"]
    key = "%s::%s" % (file_path, method_key)
    funct = Function()
    funct.id = executed["name"]
    funct.input_key = executed["inputKey"]
    funct.name = method_key
    funct.source_file = file_path
    funct_meta = get_metadata(file_path, method_key)
    funct.outputs = Outputs(executed["outputs"], funct_meta.get("returnMetadata", None))
    if funct.is_valid_function():
      method_group = method_groups.get(key, [])
      method_group.append(funct)
      method_groups[key] = method_group
  return method_groups


def compute_cross_language():
  store = ExecStore()
  py_executed = store.get_functions_executed(language=properties.LANGUAGE_PYTHON)
  py_method_groups = group_executable_methods(py_executed, properties.LANGUAGE_PYTHON)
  # for py_file_key, py_methods in py_method_groups.items():
  #   print("## #Methods: %d" % (len(py_methods)))
  java_executed = store.get_functions_executed(language=properties.LANGUAGE_JAVA)
  java_method_groups = group_executable_methods(java_executed, properties.LANGUAGE_JAVA)
  # for java_file_key, java_methods in java_method_groups.items():
  #   print("#Methods: %d" % (len(java_methods)))
  meta_store = MetaStore()
  for py_index, (py_key, py_method_group) in enumerate(py_method_groups.items()):
    py_file = py_method_group[0].source_file
    py_method_name = py_method_group[0].name
    if meta_store.is_py_file_exec_distance_computed(py_key):
      LOGGER.info("Already computed '%s'!" % py_key)
      continue
    if py_index % 1 == 0:
      LOGGER.info("Computing for py key %d/%d " % (py_index + 1, len(py_method_groups)))
    java_files_with_matches = {}
    for java_key, java_method_group in java_method_groups.items():
      if py_method_group[0].input_key != java_method_group[0].input_key:
        continue
      java_file = java_method_group[0].source_file
      java_method_name = java_method_group[0].name
      best_score = 0.0
      for py_method in py_method_group:
        for java_method in java_method_group:
          score, best_matching = multi_attribute_comparison(py_method_group[0], java_method_group[0])
          if score > best_score:
            best_score = score
      if best_score > 0.0:
        current_best_method = java_files_with_matches.get(java_file, None)
        if current_best_method and current_best_method["score"] > best_score:
          continue
        java_files_with_matches[java_file] = {
          "file1": py_file,
          "method1": py_method_name,
          "file2": java_file,
          "method2": java_method_name,
          "score": best_score
        }
    for exec_distance_map in java_files_with_matches.values():
      store.save_exec_distance(exec_distance_map)
    meta_store.update_py_file_exec_distance_computed(py_key)


if __name__ == "__main__":
  compute_cross_language()
