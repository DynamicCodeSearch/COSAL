import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from store import base_store, mongo_driver
from utils import logger, lib, cache
import properties
import re

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class InputStore(base_store.InputStore):
  def __init__(self, dataset, **kwargs):
    base_store.InputStore.__init__(self, dataset, **kwargs)

  def load_inputs(self, args_key):
    arguments = mongo_driver.get_collection(self.dataset, "fuzzed_args").find_one({"key": args_key})["args"]
    assert len(arguments) == properties.FUZZ_ARGUMENT_SIZE
    # if self.is_array(arguments):
    #   key_args = arguments
    # else:
    #   key_args = [[] for _ in range(len(arguments[0]))]
    #   for i in range(len(arguments[0])):
    #     for arg in arguments:
    #       key_args[i].append(arg)
    # return key_args
    return arguments


class FunctionStore(base_store.FunctionStore):
  PY_FUNCTION_METADATA = "py_functions_metadata"

  def __init__(self, dataset, **kwargs):
    self.is_test = None
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def load_function(self, function_name):
    collection_name = "test_functions_executed" if self.is_test else "functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name})

  def load_functions(self, function_names=None, limit=None):
    collection_name = "test_functions_executed" if self.is_test else "functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not function_names:
      if limit is not None:
        return collection.find(limit=limit)
      else:
        return collection.find()
    else:
      return [self.load_function(function_name) for function_name in function_names]

  def count_functions(self):
    collection_name = "test_functions_executed" if self.is_test else "functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.count()

  def load_all_metadata(self, limit=None):
    collection = mongo_driver.get_collection(self.dataset, "functions_metadata")
    if limit is not None:
      return collection.find(limit=limit)
    else:
      return collection.find()

  def load_java_generated_functions(self, limit=None):
    collection = mongo_driver.get_collection(self.dataset, "functions_metadata")
    query = {"$or": [
      {"originalFunctionName": None},
      {"originalFunctionName": {"$exists": False}}
    ]}
    if limit is not None:
      return collection.find(query, limit=limit)
    else:
      return collection.find(query)

  def load_metadata(self, funct):
    return mongo_driver.get_collection(self.dataset, "functions_metadata").find_one({"name": funct["name"]})

  def update_py_function_metadata(self, function_json):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name", "generated_file")
    collection.insert(function_json)

  def load_py_function_metadata(self, function_name):
    try:
      return mongo_driver.get_collection(self.dataset,
                                         FunctionStore.PY_FUNCTION_METADATA).find_one({"name": function_name})
    except Exception as e:
      LOGGER.critical("Failed to load args for function: '%s'. Returning None."
                      "\nMessage: %s" % (function_name, e.message))
      return None

  def load_py_functions_metadata(self, file_path):
    file_path = cache.get_repo_local_path(file_path)
    try:
      return mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)\
        .find({"generated_file": file_path})
    except Exception as e:
      LOGGER.critical("Failed to load args for file path: '%s'. Returning None."
                      "\nMessage: %s" % (file_path, e.message))
      return None

  def load_py_generated_functions(self):
    query = {"$or": [
      {"original_function_name": None},
      {"original_function_name": {"$exists": False}}
    ]}
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    return collection.find(query)

  def load_py_functions_from_names(self, function_names):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    return [collection.find_one({"name": func_name}) for func_name in function_names]

  def del_py_function_metadata(self, function_name):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    mongo_driver.delete_document(collection, "name", function_name)

  def del_py_functions_metadata(self, file_path):
    file_path = cache.get_repo_local_path(file_path)
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    mongo_driver.delete_document(collection, "generated_file", file_path)

  def del_all_py_functions_metadata(self):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    mongo_driver.drop_collection(collection)

  def get_generated_file(self, source_file_path):
    source_file_path = cache.get_repo_local_path(source_file_path)
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.PY_FUNCTION_METADATA)
    doc = collection.find_one({"source_file": source_file_path})
    if not doc:
      return None
    return cache.get_absolute_path(doc['generated_file'])

  def save_py_function(self, function_json):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    try:
      collection.insert(function_json)
    except Exception:
      del function_json['outputs']
      self.save_failed_py_function(function_json)

  def load_py_function(self, function_name):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name})

  def exists_py_function(self, function_name):
    return self.load_py_function(function_name) is not None

  def save_failed_py_function(self, function_json):
    collection_name = "test_py_functions_failed" if self.is_test else "py_functions_failed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    collection.insert(function_json)

  def is_invalid_py_function(self, function_name):
    collection_name = "test_py_functions_failed" if self.is_test else "py_functions_failed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name}) is not None

  def load_py_functions(self):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find()

  def del_all_py_functions(self):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return mongo_driver.drop_collection(collection)

  def save_py_metadata(self, func_json):
    collection = mongo_driver.get_collection(self.dataset, "py_functions_metadata")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    if mongo_driver.contains_document(collection, "name", func_json["name"]):
      mongo_driver.delete_document(collection, "name", func_json["name"])
    collection.insert(func_json)

  def load_py_metadata(self, function_name):
    try:
      collection = mongo_driver.get_collection(self.dataset, "py_functions_metadata")
      return collection.find_one({"name": function_name})
    except Exception:
      LOGGER.exception("Failed to metadata for function: '%s'. Returning None" % function_name)
      return None

  def get_executed_functions(self, language):
    collection = mongo_driver.get_collection(self.dataset, "language_executed_functions")
    document = collection.find_one({"language": language})
    if document is None:
      return None
    return document['names']


class PyFileMetaStore(base_store.PyFileMetaStore):
  def __init__(self, dataset, **kwargs):
    base_store.PyFileMetaStore.__init__(self, dataset,  **kwargs)

  def load_meta(self, file_name):
    sep_positions = [m.start() for m in re.finditer(os.sep, file_name)]
    if sep_positions and len(sep_positions) > 3:
      fp_regex = file_name[sep_positions[2]:]
    else:
      fp_regex = file_name
    collection = mongo_driver.get_collection(self.dataset, "py_file_meta")
    return collection.find_one({"file_path": {"$regex": fp_regex}})

  def save_meta(self, bson_dict):
    collection = mongo_driver.get_collection(self.dataset, "py_file_meta")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "file_path")
    self.del_meta(bson_dict["file_path"])
    collection.insert(bson_dict)

  def del_meta(self, file_path):
    collection = mongo_driver.get_collection(self.dataset, "py_file_meta")
    if not mongo_driver.is_collection_exists(collection):
      return
    mongo_driver.delete_document(collection, "file_path", file_path)


class ArgumentStore(base_store.ArgumentStore):
  def __init__(self, dataset, **kwargs):
    self.is_test = None
    base_store.ArgumentStore.__init__(self, dataset, **kwargs)

  def load_args(self, args_key):
    collection_name = "test_fuzzed_args" if self.is_test else "fuzzed_args"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    try:
      return collection.find_one({"key": args_key})
    except Exception:
      LOGGER.exception("Failed to load args with key: '%s'. Returning None" % args_key)
      return None


class ExecutionStore(base_store.ExecutionStore):
  def __init__(self, dataset, **kwargs):
    base_store.ExecutionStore.__init__(self, dataset, **kwargs)

  def save_language_executed_function_names(self, language, names):
    collection = mongo_driver.get_collection(self.dataset, "language_executed_functions")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "language")
    if mongo_driver.contains_document(collection, "language", language):
      mongo_driver.delete_document(collection, "language", language)
    collection.insert({
      "language": language,
      "names": names
    })

  def save_cloned_function_names(self, name, clones):
    collection = mongo_driver.get_collection(self.dataset, "cloned_functions")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "_function_name_")
    if mongo_driver.contains_document(collection, "_function_name_", name):
      mongo_driver.delete_document(collection, "_function_name_", name)
    clones["_function_name_"] = name
    collection.insert(clones)

  def load_cloned_function_names(self, name):
    collection = mongo_driver.get_collection(self.dataset, "cloned_functions")
    return mongo_driver.get_document(collection, "_function_name_", name)


class ClusterStore(base_store.ClusterStore):
  def __init__(self, dataset, **kwargs):
    base_store.ClusterStore.__init__(self, dataset,  **kwargs)

  def save_difference(self, difference, clustering_error):
    collection_name = "difference_%0.2f" % clustering_error
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key")
    collection.find_one_and_update({"key": difference["key"]}, {"$set": difference}, upsert=True)

  def load_differences(self, clustering_error):
    collection_name = "difference_%0.2f" % clustering_error
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      return []
    return collection.find()

  def count_differences(self, clustering_error):
    collection_name = "difference_%0.2f" % clustering_error
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      return 0
    return collection.count()

  def save_clusters(self, clusters, suffix):
    collection_name = "clusters_%s" % suffix
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if mongo_driver.is_collection_exists(collection):
      mongo_driver.drop_collection(collection)
    mongo_driver.create_unique_index_for_collection(collection, "cluster_id")
    for cluster_id, functions in clusters.items():
      LOGGER.info("Saving cluster to DB: '%d', with %d functions" % (cluster_id, len(functions)))
      cluster = {
        "cluster_id": cluster_id,
        "functions": [lib.to_json(f) for f in functions]
      }
      collection.insert(cluster)

  def register_completed_function(self, function_name, clustering_error):
    collection_name = "meta_cluster_completed_functions"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    key = "error_%0.2f" % clustering_error
    collection.find_one_and_update({"key": key}, {"$addToSet": {"functions": function_name}}, upsert=True)

  def get_completed_functions(self, clustering_error):
    collection_name = "meta_cluster_completed_functions"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    key = "error_%0.2f" % clustering_error
    doc = collection.find_one({"key": key})
    if doc:
      return doc["functions"]
    return []

  def get_clones(self, clustering_error, dist_lower_bound=None, dist_upper_bound=None, input_key=None):
    collection_name = "difference_%0.2f" % clustering_error
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      return []
    query = {}
    if input_key:
      query["input_key"] = input_key
    if dist_upper_bound is not None and dist_lower_bound is not None:
      query["dist"] = {
        "$gte": dist_lower_bound,
        "$lte": dist_upper_bound
      }
    elif dist_upper_bound is not None:
      query["dist"] = {"$gte": dist_lower_bound}
    elif dist_lower_bound is not None:
      query["dist"] = {"$lte": dist_upper_bound}
    if query:
      return collection.find(query)
    else:
      return collection.find()


class SystemClassStore(base_store.SystemClassStore):
  _SYSTEM_CLASS_COLLECTION = "system_classes"
  _SYSTEM_CLASS_VALIDITY_COLLECTION = "system_classes_validity"
  _SYSTEM_CLASS_STORE_CACHE = {}

  def __init__(self, dataset, **kwargs):
    base_store.SystemClassStore.__init__(self, dataset, **kwargs)

  def is_valid_class(self, project, class_key):
    collection = mongo_driver.get_collection(self.dataset, SystemClassStore._SYSTEM_CLASS_VALIDITY_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return False
    doc = collection.find_one({
      "key": class_key,
      "project": project
    })
    if doc is not None:
      return doc["isValid"]
    return False

  def get_class(self, project, class_key):
    cache_key = "%s:%s" % (project, class_key)
    if cache_key in SystemClassStore._SYSTEM_CLASS_STORE_CACHE:
      return SystemClassStore._SYSTEM_CLASS_STORE_CACHE[cache_key]
    collection = mongo_driver.get_collection(self.dataset, SystemClassStore._SYSTEM_CLASS_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return None
    doc = collection.find_one({
      "key": class_key,
      "project": project
    })
    SystemClassStore._SYSTEM_CLASS_STORE_CACHE[cache_key] = doc
    return doc


class PyClassStore(base_store.PyClassStore):
  _SYSTEM_CLASS_COLLECTION = "py_system_classes"
  _CUSTOM_CLASS_COLLECTION = "py_custom_classes"

  def __init__(self, **kwargs):
    base_store.PyClassStore.__init__(self, **kwargs)

  @staticmethod
  def _get_system_class(module, name):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), PyClassStore._SYSTEM_CLASS_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return None
    key = "%s.%s" % (module, name) if module else name
    project = properties.CONFIG.get_project_name()
    return collection.find_one({
      "key": key,
      "project": project
    })

  def is_valid_system_class(self, module, name):
    system_class = PyClassStore._get_system_class(module, name)
    return system_class and system_class.get("is_valid", False)

  def load_system_class(self, module, name):
    return PyClassStore._get_system_class(module, name)

  def save_system_class(self, system_class):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), PyClassStore._SYSTEM_CLASS_COLLECTION)
    module = system_class.module
    name = system_class.name
    key = "%s.%s" % (module, name) if module else name
    project = properties.CONFIG.get_project_name()
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key", "project")
    query = {
      "key": key,
      "project": project
    }
    system_class.is_valid = len(system_class.parameters) > 0
    LOGGER.info("Saving system class '%s' ... " % key)
    mongo_driver.upsert_document(collection, query=query, document=system_class.to_bson())

  @staticmethod
  def _get_custom_class(file_path, name):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), PyClassStore._CUSTOM_CLASS_COLLECTION)
    file_source = cache.get_repo_local_path(file_path)
    key = "%s.%s" % (file_source, name) if file_source else name
    project = properties.CONFIG.get_project_name()
    return collection.find_one({
      "key": key,
      "project": project
    })

  def load_custom_class(self, file_source, name):
    return PyClassStore._get_custom_class(file_source, name)

  def save_custom_class(self, custom_class):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), PyClassStore._CUSTOM_CLASS_COLLECTION)
    file_source = cache.get_repo_local_path(custom_class.file_source)
    name = custom_class.name
    key = "%s.%s" % (file_source, name) if file_source else name
    project = properties.CONFIG.get_project_name()
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key", "project")
    LOGGER.info("Saving custom class '%s' ... " % key)
    custom_class_bson = custom_class.to_bson()
    query = {
      "key": key,
      "project": project
    }
    mongo_driver.upsert_document(collection, query=query, document=custom_class_bson)


class TokenStore(base_store.TokenStore):
  TOKENS_COLLECTION = "py_functions_tokens"
  JAVA_TOKENS_COLLECTION = "functions_tokens"
  CONTEXT_COLLECTION = "py_functions_contexts"
  JAVA_CONTEXT_COLLECTION = "functions_contexts"

  def __init__(self, **kwargs):
    base_store.TokenStore.__init__(self, **kwargs)

  def save_tokens(self, token_json):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), TokenStore.TOKENS_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "hash_key")
    doc = collection.find_one({"hash_key": token_json["hash_key"]})
    if doc:
      mongo_driver.delete_document(collection, "hash_key", token_json["hash_key"])
      doc["names"] = list(set(doc['names'] + [token_json["name"]]))
      mongo_driver.upsert_document(collection, {"hash_key": token_json["hash_key"]}, doc)
    else:
      token_json["names"] = [token_json["name"]]
      del token_json["name"]
      collection.insert(token_json)
    # if mongo_driver.contains_document(collection, "hash_key", token_json["hash_key"]):
    #   mongo_driver.delete_document(collection, "hash_key", token_json["hash_key"])

  def save_contextual_tokens(self, context_json):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), TokenStore.CONTEXT_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "hash_key")
    doc = collection.find_one({"hash_key": context_json["hash_key"]})
    if doc:
      mongo_driver.delete_document(collection, "hash_key", context_json["hash_key"])
      doc["names"] = list(set(doc['names'] + [context_json["name"]]))
      mongo_driver.upsert_document(collection, {"hash_key": context_json["hash_key"]}, doc)
    else:
      context_json["names"] = [context_json["name"]]
      del context_json["name"]
      collection.insert(context_json)

  @staticmethod
  def _format_document(document, language):
    return {
      "names": document["names"],
      "hash_key": document["hash_key"],
      "tokens": document["tokens"],
      "language": language
    }

  def get_contextual_tokens(self, language=None):
    if language is None:
      return self.get_contextual_tokens(properties.LANGUAGE_PYTHON) \
             + self.get_contextual_tokens(properties.LANGUAGE_JAVA)
    elif language == properties.LANGUAGE_JAVA:
      collection_name = TokenStore.JAVA_CONTEXT_COLLECTION
    elif language == properties.LANGUAGE_PYTHON:
      collection_name = TokenStore.CONTEXT_COLLECTION
    else:
      raise RuntimeError("Unsupported language for contextual tokens '%s'!!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    docs = []
    for doc in collection.find():
      docs.append(TokenStore._format_document(doc, language))
    return docs

  def sample_documents(self, language, sample_size):
    if language == properties.LANGUAGE_JAVA:
      collection_name = TokenStore.JAVA_CONTEXT_COLLECTION
    elif language == properties.LANGUAGE_PYTHON:
      collection_name = TokenStore.CONTEXT_COLLECTION
    else:
      raise RuntimeError("Unsupported language for contextual tokens '%s'!!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    samples = []
    for doc in collection.aggregate([{"$sample": {"size": sample_size}}]):
      samples.append(TokenStore._format_document(doc, language))
    return samples

  def get_tokens(self, language=None):
    if language is None:
      return self.get_tokens(properties.LANGUAGE_PYTHON) \
             + self.get_tokens(properties.LANGUAGE_JAVA)
    elif language == properties.LANGUAGE_JAVA:
      collection_name = TokenStore.JAVA_TOKENS_COLLECTION
    elif language == properties.LANGUAGE_PYTHON:
      collection_name = TokenStore.TOKENS_COLLECTION
    else:
      raise RuntimeError("Unsupported language for contextual tokens '%s'!!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    samples = []
    for doc in collection.find():
      samples.append(TokenStore._format_document(doc, language))
    return samples
