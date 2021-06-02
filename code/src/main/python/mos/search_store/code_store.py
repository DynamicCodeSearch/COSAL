import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils.lib import O
from utils import cache, logger
from store import mongo_driver
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))

class CodeStore(O):

  # PY_CODE_STORE_COLLECTION = "py_code_store"
  # JAVA_CODE_STORE_COLLECTION = "java_code_store"
  CODE_STORE_COLLECTION = "code_store"

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def drop_code_blocks(self):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    if mongo_driver.is_collection_exists(collection):
      mongo_driver.drop_collection(collection)

  def save_code_block(self, code_block):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "uid", "language")
    doc = code_block.to_bson()
    uid = doc["uid"]
    if mongo_driver.contains_document(collection, "uid", uid):
      mongo_driver.delete_document(collection, "uid", uid)
    collection.insert(doc)

  def delete_code_blocks_from_file(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return
    file_path = cache.get_repo_local_path(file_path)
    collection.delete_many({"sourceFile": file_path})

  def get_code_blocks(self, language=None, fields=None, limit=None, **additional_queries):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {}
    if language:
      query = {
        "language": language
      }
    if additional_queries:
      query.update(**additional_queries)
    fetch_results = collection.find(filter=query, projection=fields)
    if limit is not None:
      fetch_results = fetch_results.limit(limit)
    return fetch_results

  def get_random_code_blocks(self, language=None, fields=None, limit=20, **additional_queries):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {}
    if language:
      query = {
        "language": language
      }
    if additional_queries:
      query.update(**additional_queries)
    return collection.aggregate([
      {"$sample": {"size": limit}},
      {"$match": query}
    ])

  def count_code_blocks(self, language=None, **additional_queries):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {}
    if language:
      query = {
        "language": language
      }
    if additional_queries:
      query.update(**additional_queries)
    return collection.count(query)

  def fetch_code_block(self, uid, projections=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {"uid": uid}
    if projections:
      return collection.find_one(query, projections)
    else:
      return collection.find_one(query)

  def update_code_block(self, uid, updates):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {"uid": uid}
    collection.find_one_and_update(query, {
      "$set": updates
    })

  def get_code_block_id(self, file_path, language=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    query = {
      "sourceFile": cache.get_repo_local_path(file_path)
    }
    if language:
      query["language"] = language
    cb = collection.find_one(query)
    if cb:
      return cb["uid"]
    return None

  def is_code_block_exists(self, uid):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), CodeStore.CODE_STORE_COLLECTION)
    return mongo_driver.contains_document(collection, "uid", uid)


class ASTDistanceStore(O):
  AST_DISTANCE_COLLECTION = "ast_distance_store"

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def get_collection(self, language=None):
    name = "%s_%s" % (language, ASTDistanceStore.AST_DISTANCE_COLLECTION) if language else ASTDistanceStore.AST_DISTANCE_COLLECTION
    return mongo_driver.get_collection(properties.CONFIG.get_dataset(), name)

  def save_ast_distance(self, node, language=None):
    node_bson = node.to_bson()
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key", "uid1", "uid2")
    collection.insert(node_bson)

  def save_ast_distances(self, nodes, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key", "uid1", "uid2")
    collection.insert_many([node.to_bson() for node in nodes], ordered=False, bypass_document_validation=True)

  def get_ast_node(self, key, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      return None
    return collection.find_one({"key": key})

  def get_all_nodes(self, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      return None
    collection.find()

  def get_nodes_for_uid(self, uid, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      return None
    query = {"$or": [{"uid1": uid}, {"uid2": uid}]}
    return collection.find(query)

  def get_most_similar_nodes(self, uid, search_limit, language=None):
    nodes = self.get_nodes_for_uid(uid, language)
    if nodes is None:
      return None
    sorted_nodes = nodes.sort("distance")
    if search_limit is not None:
      return sorted_nodes.limit(search_limit)
    return sorted_nodes

  def count_nodes_for_uid(self, uid, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      return 0
    query = {"$or": [{"uid1": uid}, {"uid2": uid}]}
    return collection.count(query)

  def get_computed_uids(self, uid, language=None):
    collection = self.get_collection(language)
    if not mongo_driver.is_collection_exists(collection):
      return set()
    computed = set()
    for node in self.get_nodes_for_uid(uid, language):
      uid1, uid2 = node['uid1'], node['uid2']
      if uid1 != uid:
        computed.add(uid1)
      elif uid2 != uid:
        computed.add(uid2)
    return computed


class FileStore(O):
  FILE_STORE_COLLECTION = "file_store"

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def save_file_block(self, code_block):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "uid", "sourceFile")
    doc = code_block.to_bson()
    source_file = doc["uid"]
    if mongo_driver.contains_document(collection, "sourceFile", source_file):
      mongo_driver.delete_document(collection, "sourceFile", source_file)
    collection.insert(doc)

  def delete_all_file_blocks(self, language=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "uid", "sourceFile")
    query = {}
    if language:
      query = {
        "language": language
      }
    collection.delete_many(query)

  def get_file_block(self, sourceFilePath):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return None
    query = {"sourceFile": cache.get_repo_local_path(sourceFilePath)}
    return collection.find_one(query)

  def get_file_blocks(self, language=None, fields=None, limit=None, **additional_queries):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    query = {}
    if language:
      query = {
        "language": language
      }
    if additional_queries:
      query.update(**additional_queries)
    fetch_results = collection.find(filter=query, projection=fields)
    if limit is not None:
      fetch_results = fetch_results.limit(limit)
    return fetch_results

  def count_file_blocks(self, language=None, **additional_queries):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    query = {}
    if language:
      query = {
        "language": language
      }
    if additional_queries:
      query.update(**additional_queries)
    return collection.count(query)

  def update_file_block(self, uid, updates):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), FileStore.FILE_STORE_COLLECTION)
    query = {"uid": uid}
    collection.find_one_and_update(query, {
      "$set": updates
    })


class MetaStore(O):
  META_STORE_COLLECTION = "meta_store"
  PROJECTS_CACHED = "projects_cached"
  PY_FILES_EXECUTED = "py_files_executed"
  PY_FILES_EXEC_DISTANCE_COMPUTED = "py_files_executed_distance"

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)

  def update_ast_cache_project(self, project_id, language=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key")
    key = "%s_%s" % (language, MetaStore.PROJECTS_CACHED) if language else MetaStore.PROJECTS_CACHED
    query = {"key": key}
    doc = collection.find_one(query)
    if doc is None:
      doc = {
        "key": key,
        "value": [project_id]
      }
    else:
      if project_id not in doc["value"]:
        doc["value"].append(project_id)
    mongo_driver.upsert_document(collection, query, doc)

  def get_ast_cache_projects(self, language=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return set()
    key = "%s_%s" % (language, MetaStore.PROJECTS_CACHED) if language else MetaStore.PROJECTS_CACHED
    query = {"key": key}
    doc = collection.find_one(query)
    if doc is None:
      return set()
    return set(doc["value"])

  def is_project_ast_cached(self, project_id, language=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return False
    key = "%s_%s" % (language, MetaStore.PROJECTS_CACHED) if language else MetaStore.PROJECTS_CACHED
    query = {"key": key}
    doc = collection.find_one(query)
    if doc is None:
      return False
    return project_id in doc["value"]

  def update_py_file_processed(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key")
    query = {"key": MetaStore.PY_FILES_EXECUTED}
    file_path = cache.get_repo_local_path(file_path)
    collection.update(query, {"$addToSet": {"value": file_path}}, upsert=True)

  def is_py_file_processed(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return False
    query = {"key": MetaStore.PY_FILES_EXECUTED}
    file_path = cache.get_repo_local_path(file_path)
    doc = collection.find_one(query)
    if doc is None:
      return False
    return file_path in doc["value"]

  def update_py_file_exec_distance_computed(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "key")
    query = {"key": MetaStore.PY_FILES_EXEC_DISTANCE_COMPUTED}
    file_path = cache.get_repo_local_path(file_path)
    collection.update(query, {"$addToSet": {"value": file_path}}, upsert=True)

  def is_py_file_exec_distance_computed(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), MetaStore.META_STORE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return False
    query = {"key": MetaStore.PY_FILES_EXEC_DISTANCE_COMPUTED}
    file_path = cache.get_repo_local_path(file_path)
    doc = collection.find_one(query)
    if doc is None:
      return False
    return file_path in doc["value"]


class ExecStore(O):
  FUNCTION_METADATA_COLLECTION = "py_functions_metadata"
  FUNCTIONS_EXECUTED_COLLECTION = "py_functions_executed"
  FUNCTIONS_FAILED_COLLECTION = "py_functions_failed"
  JAVA_FUNCTIONS_EXECUTED_COLLECTION = "functions_executed"
  JAVA_FUNCTIONS_METADATA_COLLECTION = "functions_metadata"
  EXEC_DISTANCE_STORE = "exec_distance_store"

  def save_class_function_meta(self, function_meta_bson):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.FUNCTION_METADATA_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_index_for_collection(collection, "originalFunctionName")
      mongo_driver.create_index_for_collection(collection, "filePath")
    collection.insert(function_meta_bson)

  def delete_class_function_meta(self, file_path, original_function_name=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.FUNCTION_METADATA_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      return
    query = {"filePath": cache.get_repo_local_path(file_path)}
    if original_function_name:
      query["originalFunctionName"] = original_function_name
    doc = collection.find_one(query)
    if doc:
      collection.delete_many(query)

  def update_class_function_result(self, function_json):
    try:
      collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.FUNCTIONS_EXECUTED_COLLECTION)
      if not mongo_driver.is_collection_exists(collection):
        mongo_driver.create_index_for_collection(collection, "originalFunctionName")
        mongo_driver.create_index_for_collection(collection, "filePath")
      function_json["filePath"] = cache.get_repo_local_path(function_json["filePath"])
      collection.insert(function_json)
    except Exception as e:
      LOGGER.info("Failed to save function result. Message: %s" % e.message)

  def delete_class_function_result(self, file_path, original_function_name=None):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.FUNCTIONS_EXECUTED_COLLECTION)
    query = {"filePath": cache.get_repo_local_path(file_path)}
    if original_function_name:
      query["originalFunctionName"] = original_function_name
    doc = collection.find_one(query)
    if doc:
      collection.delete_many(query)

  def get_functions_executed(self, language, **additional_queries):
    if language == properties.LANGUAGE_PYTHON:
      collection_name = ExecStore.FUNCTIONS_EXECUTED_COLLECTION
    elif language == properties.LANGUAGE_JAVA:
      collection_name = ExecStore.JAVA_FUNCTIONS_EXECUTED_COLLECTION
    else:
      raise RuntimeError("Unsupported language: %s!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    query = {}
    if additional_queries:
      query.update(**additional_queries)
    return collection.find(query)

  def count_functions_executed(self, language, **additional_queries):
    if language == properties.LANGUAGE_PYTHON:
      collection_name = ExecStore.FUNCTIONS_EXECUTED_COLLECTION
    elif language == properties.LANGUAGE_JAVA:
      collection_name = ExecStore.JAVA_FUNCTIONS_EXECUTED_COLLECTION
    else:
      raise RuntimeError("Unsupported language: %s!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    query = {}
    if additional_queries:
      query.update(**additional_queries)
    return collection.count(query)

  def get_function_meta(self, language, file_path, original_function_name):
    if language == properties.LANGUAGE_PYTHON:
      collection_name = ExecStore.FUNCTION_METADATA_COLLECTION
    elif language == properties.LANGUAGE_JAVA:
      collection_name = ExecStore.JAVA_FUNCTIONS_METADATA_COLLECTION
    else:
      raise RuntimeError("Unsupported language: %s!" % language)
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), collection_name)
    query = {"filePath": file_path, "originalFunctionName": original_function_name}
    return collection.find_one(query)

  def save_exec_distance(self, exec_data):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.EXEC_DISTANCE_STORE)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_index_for_collection(collection, "file1")
      mongo_driver.create_index_for_collection(collection, "file2")
    exec_data["file1"] = cache.get_repo_local_path(exec_data["file1"])
    exec_data["file2"] = cache.get_repo_local_path(exec_data["file2"])
    collection.insert(exec_data)

  def get_exec_distances_for_file(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.EXEC_DISTANCE_STORE)
    if not mongo_driver.is_collection_exists(collection):
      return None
    file_path = cache.get_repo_local_path(file_path)
    query = {"$or": [{"file1": file_path}, {"file2": file_path}]}
    return collection.find(query)

  def count_exec_distances_for_file(self, file_path):
    collection = mongo_driver.get_collection(properties.CONFIG.get_dataset(), ExecStore.EXEC_DISTANCE_STORE)
    if not mongo_driver.is_collection_exists(collection):
      return None
    file_path = cache.get_repo_local_path(file_path)
    query = {"$or": [{"file1": file_path}, {"file2": file_path}]}
    return collection.count(query)


def _test():
  store = CodeStore()
  blocks = store.get_code_blocks(language=properties.LANGUAGE_PYTHON, fields=["uid", "contextualTokens"])
  for block in blocks:
    print(block)


if __name__ == "__main__":
  _test()
