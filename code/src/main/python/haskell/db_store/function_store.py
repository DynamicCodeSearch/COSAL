import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils.lib import O
from utils import cache
from store import mongo_driver, base_store


class FunctionStore(base_store.FunctionStore):
  HS_FUNCTION_METADATA = "hs_functions_metadata"
  HS_FUNCTION_SUCCESS = "hs_functions_executed"
  HS_FUNCTION_FAILED = "hs_functions_failed"

  def __init__(self, dataset, **kwargs):
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def save_hs_function(self, function_json):
    collection = mongo_driver.get_collection(self.dataset, collection_name=FunctionStore.HS_FUNCTION_METADATA)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_index_for_collection(collection, "name")
    if mongo_driver.contains_document(collection, "name", function_json["name"]):
      mongo_driver.delete_document(collection, "name", function_json)
    collection.insert(function_json)

  def del_hs_functions_by_file_path(self, file_path):
    file_path = cache.get_repo_local_path(file_path)
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_METADATA)
    mongo_driver.delete_documents(collection, "filePath", file_path)

  def save_failed_hs_function(self, function_json):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_FAILED)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    collection.insert(function_json)

  def save_success_hs_function(self, function_json):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_SUCCESS)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    try:
      collection.insert(function_json)
    except Exception as e:
      print(e)
      del function_json['outputs']
      self.save_failed_hs_function(function_json)

  def del_all_executed_hs_functions(self):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_SUCCESS)
    mongo_driver.drop_collection(collection)
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_FAILED)
    mongo_driver.drop_collection(collection)

  def del_executed_hs_functions_by_file_path(self, file_path):
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_SUCCESS)
    mongo_driver.delete_documents(collection, "fileName", cache.get_repo_local_path(file_path))
    collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_FAILED)
    mongo_driver.delete_documents(collection, "fileName", cache.get_repo_local_path(file_path))

  # def del_hs_functions_by_filepath(self, filepath):
  #   filepath = cache.get_repo_local_path(filepath)
  #   collection = mongo_driver.get_collection(self.dataset, FunctionStore.HS_FUNCTION_SUCCESS)