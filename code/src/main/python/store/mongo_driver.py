import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


import pymongo
import multiprocessing

from utils import cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
MAX_POOL_SIZE=10000
__MONGO_CLIENTS = {}


def get_default_hostname():
  # return socket.gethostname()
  return 'localhost'


def get_hostname():
  mongo_home = os.environ.get("MONGO_HOME", None)
  if mongo_home:
    file_name = os.path.join(mongo_home, "host_machine.txt")
    if cache.file_exists(file_name):
      return cache.read_file(file_name).strip()
  return get_default_hostname()


def get_client():
  global __MONGO_CLIENTS
  process_id = multiprocessing.current_process().ident
  if process_id not in __MONGO_CLIENTS:
    __MONGO_CLIENTS[process_id] = pymongo.MongoClient(host=get_hostname(), maxPoolSize=MAX_POOL_SIZE)
  __MONGO_CLIENT = __MONGO_CLIENTS[process_id]
  try:
    assert __MONGO_CLIENT.address
    return __MONGO_CLIENT
  except Exception:
    __MONGO_CLIENT.close()
    __MONGO_CLIENT = None
    del __MONGO_CLIENTS[process_id]
    raise RuntimeError("Looks like client is down")


def get_dataset_db(dataset):
  if not dataset:
    raise RuntimeError("Dataset is empty")
  try:
    return get_client().get_database(dataset)
  except Exception as e:
    LOGGER.warn("Dataset '%s' does not exist. Creating this mongo manually and rerun "
                "the application. Don't forget to insert dummy record" % dataset)
    raise RuntimeError(e)


def get_collection(dataset, collection_name):
  return get_dataset_db(dataset).get_collection(collection_name)


def is_collection_exists(collection):
  return collection.estimated_document_count() > 0


def create_unique_index_for_collection(collection, *fields):
  indices = []
  for field in fields:
    indices.append((field, pymongo.ASCENDING))
  collection.create_index(indices, unique=True)


def create_index_for_collection(collection, field, order=pymongo.ASCENDING):
  if does_index_exist(collection, field):
    # LOGGER.info("Index: '%s' exists for collection: '%s'. Not creating ..." % (field, collection.name))
    return
  # LOGGER.info("Creating index: '%s' for collection: '%s' ..." % (field, collection.name))
  collection.create_index([(field, order)])


def does_index_exist(collection, field):
  index_info = collection.index_information()
  if not index_info:
    return False
  for key, info in index_info.items():
    for row in info['key']:
      if row[0] == field:
        return True
  return False


def get_document(collection, key, value):
  if collection is None:
    return None
  return collection.find_one({key: value})


def contains_document(collection, key, value):
  if collection is None:
    return False
  return collection.find_one({key: value}, {"_id": 1})


def upsert_document(collection, query, document):
  collection.update_one(
    query,
    {"$set": document},
    upsert=True
  )


def delete_document(collection, key, value):
  collection.delete_one({key: value})


def delete_document_with_query(collection, query):
  collection.delete_one(query)


def delete_documents(collection, key, value):
  collection.delete_many({key: value})


def delete_documents_with_query(collection, query):
  collection.delete_many(query)


def drop_collection(collection):
  collection.drop()


def _test_index_info():
  print(does_index_exist(get_collection("Misconceptions", "differences"), "d_jaroq"))


if __name__ == "__main__":
  # print(get_dataset_db("codejam"))
  _test_index_info()
