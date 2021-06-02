import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import re
import random
import multiprocessing
from copy import deepcopy

from utils import cache, logger, lib
from sos.function import Function, Outputs, FunctionCache, InputCache
from sos.cluster import cluster_utils, dbscan, representative, multi_attribute_representative
from store import json_store, mongo_store
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
__FUNCTION_STORE = None

def get_clusterer():
  if properties.CLUSTER_TYPE == "dbscan":
    return dbscan.DBScanClusterer
  elif properties.CLUSTER_TYPE == "representative":
    return representative.RepresentativeClusterer
  raise RuntimeError("Invalid cluster configuration: %s" % properties.CLUSTER_TYPE)


def get_store(dataset, is_test=False):
  global __FUNCTION_STORE
  if __FUNCTION_STORE:
    return __FUNCTION_STORE
  if properties.STORE == "json":
    __FUNCTION_STORE = json_store.FunctionStore(dataset)
    return __FUNCTION_STORE
  elif properties.STORE == "mongo":
    __FUNCTION_STORE = mongo_store.FunctionStore(dataset, is_test=is_test)
    return __FUNCTION_STORE
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def get_execution_store(dataset):
  if properties.STORE == "mongo":
    return mongo_store.ExecutionStore(dataset)
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def get_cluster_store(dataset):
  if properties.STORE == "mongo":
    return mongo_store.ClusterStore(dataset)
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def load_functions(dataset, is_test=False, update_clone_meta=False):
  LOGGER.info("Loading java functions for '%s' ... " % dataset)
  data_store = get_store(dataset, is_test=is_test)
  functions_arr = data_store.load_functions()
  function_pattern = re.compile(r'^func_')
  functions = []
  for func_dict in functions_arr:
    if not function_pattern.match(func_dict['name']): continue
    function_metadata = data_store.load_metadata(func_dict)
    if not function_metadata or not function_metadata.get("return", None):
      continue
    return_meta_data = function_metadata["return"]
    outputs = Outputs(func_dict["outputs"])
    funct = Function(name=func_dict["name"], dataset=dataset,
                     class_name=func_dict["class"], package=func_dict["package"],
                     input_key=func_dict["inputKey"], outputs=outputs,
                     lines_touched=function_metadata.get("linesTouched", None),
                     span=function_metadata.get("span", None), body=function_metadata["body"], source="java")
    if data_store.is_object_return(return_meta_data):
      cloned_function_names = get_execution_store(dataset).load_cloned_function_names(funct.name)
      updated_cloned_function_names = {}
      for attribute, returns in data_store.get_return_vals(outputs.returns).items():
        clone = funct.clone()
        clone.outputs = outputs.clone()
        clone.outputs.returns = returns[:]
        clone.return_attribute = attribute
        if cloned_function_names and attribute in cloned_function_names:
          clone.name = cloned_function_names[attribute]
        updated_cloned_function_names[attribute] = clone.name
        functions.append(clone)
      if update_clone_meta:
        get_execution_store(dataset).save_cloned_function_names(funct.name, updated_cloned_function_names)
    else:
      functions.append(funct)
  if is_test:
    return functions
  valid_functions = [func for func in functions if func.is_useful()]
  LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
  return valid_functions


def create_function_object(func_dict, dataset, is_test=False):
  data_store = get_store(dataset, is_test=is_test)
  function_metadata = data_store.load_metadata(func_dict)
  if not function_metadata or not function_metadata.get("returnMetadata", None):
    return None
  outputs = Outputs(func_dict["outputs"], function_metadata["returnMetadata"])
  funct = Function(name=func_dict["name"], dataset=dataset,
                   class_name=func_dict["class"], package=func_dict["package"],
                   input_key=func_dict["inputKey"], outputs=outputs,
                   lines_touched=function_metadata.get("linesTouched", None),
                   span=function_metadata.get("span", None), body=function_metadata["body"],
                   source="java", source_file=function_metadata["filePath"],
                   args_permutation=function_metadata.get("argsPermutation", None))
  return funct


def load_function(dataset, function_name, is_test=False):
  if FunctionCache.is_failed_function(function_name):
    return None
  funct = FunctionCache.load_function(function_name)
  if funct:
    return funct
  data_store = get_store(dataset, is_test=is_test)
  funct_dict = data_store.load_function(function_name)
  funct = create_function_object(funct_dict, dataset, is_test)
  if funct:
    FunctionCache.store_function(funct)
  else:
    FunctionCache.store_failed_function(function_name)
  return funct


def load_functions2(dataset, clustering_error=None, limit=None, is_test=False):
  LOGGER.info("Loading java functions for '%s' ... " % dataset)
  data_store = get_store(dataset, is_test=is_test)
  # functions_arr = data_store.load_functions(function_names=[
  #   "func_9c7c479f8fc444bda94016dc60d0f90e",
  #   "func_9bb5f3d9e88d4a96b7c0da78cdb1dbb4"]
  # )
  functions_arr = data_store.load_functions(limit=limit)
  n_functions = data_store.count_functions()
  if clustering_error is not None:
    cluster_store = mongo_store.ClusterStore(dataset=properties.CONFIG.get_dataset())
    completed_functions = set(cluster_store.get_completed_functions(clustering_error))
  i = 0
  for func_dict in functions_arr:
    i += 1
    if i % 1000 == 0:
      LOGGER.info("Processing functions: %d / %d; Valid functions so far: %d" % (i, n_functions, FunctionCache.size()))
    if func_dict["name"] in completed_functions:
      continue
    # if i > 1000:
    #   break
    funct = create_function_object(func_dict, dataset, is_test)
    if funct and funct.is_valid_function():
      FunctionCache.store_function(funct)
  LOGGER.info("Valid Functions : %d / %d" % (FunctionCache.size(), n_functions))


def load_py_functions(dataset, is_test=False):
  LOGGER.info("Loading python functions for '%s' ... " % dataset)
  data_store = get_store(dataset, is_test=is_test)
  functions_arr = data_store.load_py_functions()
  function_pattern = re.compile(r'^func_')
  functions = []
  for func_dict in functions_arr:
    if not function_pattern.match(func_dict['name']): continue
    function_metadata = data_store.load_py_metadata(func_dict['name'])
    outputs = Outputs(func_dict["outputs"])
    funct = Function(name=func_dict["name"], dataset=dataset,
                     input_key=func_dict["inputKey"], outputs=outputs,
                     lines_touched=function_metadata.get("linesTouched", None),
                     span=function_metadata.get("span", None), body=function_metadata["body"], source="python")
    functions.append(funct)
  if is_test:
    return functions
  valid_functions = [func for func in functions if func.is_useful()]
  LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
  return valid_functions


def compute_similarity(dataset, language=None, functions=None, base_folder=None, file_name=None,
                       skip_singles=False, update_clone_meta=False, clustering_error=0.01):
  if not functions:
    if language == "java":
      functions = load_functions(dataset, update_clone_meta=update_clone_meta)
    elif language == "python":
      functions = load_py_functions(dataset)
    elif language == "java_python":
      functions = load_functions(dataset, update_clone_meta=update_clone_meta) + load_py_functions(dataset)
    else:
      raise RuntimeError("Invalid language: %s" % language)
    # if dataset not in ["codejam", "introclass"]:
    #   raise RuntimeError("Invalid dataset: %s" % dataset)
  LOGGER.info("Clustering ... ")
  if file_name is None:
    file_name = language or "clusters"
    LOGGER.warning("A @file_name is not provided. Reverting file name to '%s'" % file_name)
  if base_folder is None:
    base_folder = lib.get_clusters_folder(dataset)
  clusters_txt_file = os.path.join(base_folder, "%s.txt" % file_name)
  clusters_pkl_file = os.path.join(base_folder, "%s.pkl" % file_name)
  clusters_report_file = os.path.join(base_folder, "%s.md" % file_name)
  clusters = get_clusterer()(functions).cluster(clusters_txt_file, skip_singles=skip_singles, clustering_error=clustering_error)
  cluster_utils.save_clusters_to_pkl(clusters, clusters_pkl_file)
  cluster_utils.save_clusters_to_db(dataset, clusters, "base")
  cluster_utils.save_clusters_metadata(clusters, len(functions), clusters_report_file)


def preprocess_for_similarity(dataset, clustering_error=0.01):
  LOGGER.info("Preprocessing on '%d' threads ..." % multiprocessing.cpu_count())
  load_functions2(dataset, clustering_error=clustering_error, limit=1000) # FunctionCache will be populated
  # load_functions2(dataset, clustering_error=clustering_error) # FunctionCache will be populated
  LOGGER.info("Preprocess for clustering ... ")
  clusterer = multi_attribute_representative.MultiAttributeRepresentativeClusterer()
  clusterer.preprocess(clustering_error=clustering_error)
  # clusterer.preprocess(clustering_error=clustering_error, processes=1)


def compute_similarity2(dataset, base_folder=None, file_name=None, skip_singles=False, clustering_error=0.01):
  # functions = load_functions2(dataset, limit=10000)
  functions = load_functions2(dataset)
  random.shuffle(functions)
  LOGGER.info("Clustering ... ")
  if file_name is None:
    file_name = "clusters"
    LOGGER.warning("A @file_name is not provided. Reverting file name to '%s'" % file_name)
  if base_folder is None:
    base_folder = lib.get_clusters_folder(dataset)
  cache.mkdir(base_folder)
  clusters_txt_file = os.path.join(base_folder, "%s.txt" % file_name)
  clusters_pkl_file = os.path.join(base_folder, "%s.pkl" % file_name)
  clusters_report_file = os.path.join(base_folder, "%s.md" % file_name)
  clusterer = multi_attribute_representative.MultiAttributeRepresentativeClusterer(functions)
  clusters = clusterer.cluster(clusters_txt_file, skip_singles=skip_singles, clustering_error=clustering_error)
  cluster_utils.save_clusters_to_db(dataset, clusters, "base")
  cluster_utils.save_clusters_to_pkl(clusters, clusters_pkl_file)
  cluster_utils.save_clusters_metadata(clusters, len(functions), clusters_report_file)


def dump_clones(dataset, clustering_error, dist_low, dist_high, input_key, is_test=False):
  def map_inputs(f1, f2):
      mappings = []
      for key in f1.args_permutation.keys():
        assert len(f1.args_permutation[key]) == len(f2.args_permutation[key])
        for f1_arg, f2_arg in zip(f1.args_permutation[key], f2.args_permutation[key]):
          mappings.append((key, f1_arg, f2_arg))
      return mappings

  def compare_outputs(o1, o2, index, keys):
    for key_pair in keys:
      k1, k2 = key_pair[0], key_pair[1]
      r1 = None if o1.returns[index] is None else o1.returns[index][k1]
      r2 = None if o2.returns[index] is None else o2.returns[index][k2]
      e1 = o1.errors[index]
      e2 = o2.errors[index]
      if r1 != r2 or e1 != e2:
        return False
    return True

  def map_inputs_to_values(mappings, input_values):
    inp = deepcopy(input_values)
    inp_mappings = []
    for mapping in mappings:
      inp_value = inp[mapping[0]].pop(0)
      inp_mappings.append((mapping[0], mapping[1], mapping[2], inp_value))
    return inp_mappings

  cluster_store = get_cluster_store(dataset)
  clones = cluster_store.get_clones(clustering_error, dist_low, dist_high, input_key)
  contents = []
  for clone in clones:
    funct1 = load_function(dataset, clone["f1"], is_test)
    funct2 = load_function(dataset, clone["f2"], is_test)
    input_mappings = map_inputs(funct1, funct2)
    inputs = InputCache.load(dataset, clone["input_key"])
    n = len(funct1.outputs.errors)
    mismatched = {}
    for i in xrange(n):
      if not compare_outputs(funct1.outputs, funct2.outputs, i, clone["best_matching"]):
        mismatched[i] = {
          "inputs": map_inputs_to_values(input_mappings, inputs[i]),
          "outputs": (funct1.outputs.returns[i], funct2.outputs.returns[i]),
          "errors": (funct1.outputs.errors[i], funct2.outputs.errors[i])
        }
    # TODO: Create report using all prints below
    content = ["\n**Function 1**",
               funct1.body,
               "\n**Function 2**",
               funct2.body,
               "\nDist: %f" % clone["dist"],
               "\nClone Key: %s" % clone["input_key"],
               "\n**Mismatches**"]
    inps_index = 0
    for i, mismatched_i in mismatched.items():
      inps_index += 1
      content.append("\nIndex: %d" % i)
      inputs = ["'%s'='%s'=%s" % (inp[1], inp[2], str(inp[3])) for inp in mismatched_i['inputs']]
      content.append("Inputs: %s" % "; ".join(inputs))
      content.append("Outputs: f1 = %s; f2 = %s" % (str(mismatched_i['outputs'][0]), str(mismatched_i['outputs'][1])))
      content.append("Errors: f1 = %s; f2 = %s" % (str(mismatched_i['errors'][0]), str(mismatched_i['errors'][1])))
      if inps_index == 3:
        break
    contents.append("\n".join(content))
  print("# Clones: %d" % len(contents))
  content_str = "\n\n***********************\n".join(contents)
  file_name = "clones"
  base_folder = lib.get_clusters_folder(dataset)
  cache.mkdir(base_folder)
  clusters_txt_file = os.path.join(base_folder, "%s.txt" % file_name)
  cache.write_file(clusters_txt_file, content_str)

"""
Validity
"""

def _test_function():
  dataset = "codejam"
  data_store = get_store("codejam")
  func_dict = data_store.load_function("func_b1d6e0e04b4f4065870c60fcba28ff0c")
  function_metadata = data_store.load_metadata(func_dict)
  outputs = Outputs(func_dict["outputs"])
  funct = Function(name=func_dict["name"], dataset=dataset,
                   class_name=func_dict["class"], package=func_dict["package"],
                   input_key=func_dict["inputKey"], outputs=outputs,
                   lines_touched=function_metadata.get("linesTouched", None),
                   span=function_metadata.get("span", None), body=function_metadata["body"], source="java")
  print func_dict
  print(funct.is_useful())


def _test_functions():
  # load_functions2("Dummy")
  compute_similarity2("IntroClassJava", skip_singles=False)
  # load_py_functions("codejam")

def _test_clones():
  # dump_clones("IntroClassJava", 0.30, 0.005, 0.05, "int##4")
  dump_clones("IntroClassJava", 0.30, 0.005, 0.25, input_key=None)

def _main():
  args = sys.argv
  message = """
    python sos/similiarity <dataset> <mode> <?language>
    dataset: codejam/introclass
    mode: preprocess/cluster
    language: java/python/java_python(default)
    """
  if len(args) < 3:
    print(message)
    exit(0)
  mode = args[2]
  language = args[3] if len(args) >= 4 else "java_python"
  if mode == "preprocess":
    preprocess_for_similarity(args[1], clustering_error=0.3)
  elif mode == "cluster":
    compute_similarity2(args[1], skip_singles=True, clustering_error=0.01)
  else:
    print(message)
  # compute_similarity(args[1], language, skip_singles=False, update_clone_meta=True)


if __name__ == "__main__":
  # _main()
  _test_clones()
