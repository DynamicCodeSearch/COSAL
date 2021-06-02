import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O
from utils import logger
import properties

from elasticsearch import Elasticsearch

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_connection():
  # TODO: Account for remote connection
  host_urls = ["http://127.0.0.1:9200"]
  return Elasticsearch(host_urls)


class ContextStore(O):
  def __init__(self, **kwargs):
    self.index_name = "%s_%s" % (properties.CONFIG.get_dataset().lower(), "contexts")
    O.__init__(self, **kwargs)

  def create_index(self, delete_old=False):
    connection = get_connection()
    res = connection.indices.create(index=self.index_name, ignore=400)
    if res and res.get("status", None) == 400 and delete_old:
      self.delete_index()
      res = connection.indices.create(index=self.index_name, ignore=400)
    return res

  def delete_index(self):
    connection = get_connection()
    res = connection.indices.delete(index=self.index_name, ignore=404)
    return res

  def index_documents(self, docs):
    connection = get_connection()
    for i, doc in enumerate(docs):
      if i % 100 == 0:
        LOGGER.info("Indexed doc: %d/%d ... " % (i+1, len(docs)))
      connection.index(index=self.index_name, body=doc)
    connection.indices.refresh(index=self.index_name)

  def fetch_documents_for_language(self, language, limit=10):
    query = {
      "match": {
        "language": language
      }
    }
    return self.search(query, limit)

  def search(self, query, limit=10):
    search_query = {
      "query": query
    }
    return get_connection().search(index=self.index_name, body=search_query, size=limit)

  def count(self, query):
    search_query = {
      "query": query
    }
    return get_connection().count(index=self.index_name, body=search_query)


class TokenStore(O):
  def __init__(self, **kwargs):
    self.index_name = "%s_%s" % (properties.CONFIG.get_dataset().lower(), "tokens")
    O.__init__(self, **kwargs)

  def create_index(self, delete_old=False):
    connection = get_connection()
    res = connection.indices.create(index=self.index_name, ignore=400)
    if res and res.get("status", None) == 400 and delete_old:
      self.delete_index()
      res = connection.indices.create(index=self.index_name, ignore=400)
    return res

  def delete_index(self):
    connection = get_connection()
    res = connection.indices.delete(index=self.index_name, ignore=404)
    return res

  def index_documents(self, docs):
    connection = get_connection()
    for i, doc in enumerate(docs):
      tokens_str = []
      for token in doc["tokens"]:
        tokens_str.append("".join(token))
      doc["tokens"] = tokens_str
      if i % 100 == 0:
        LOGGER.info("Indexed doc: %d/%d ... " % (i+1, len(docs)))
      connection.index(index=self.index_name, body=doc)
    connection.indices.refresh(index=self.index_name)

  def fetch_documents_for_language(self, language, limit=10):
    query = {
      "match": {
        "language": language
      }
    }
    return self.search(query, limit)

  def search(self, query, limit=10):
    search_query = {
      "query": query
    }
    return get_connection().search(index=self.index_name, body=search_query, size=limit)

  def count(self, query):
    search_query = {
      "query": query
    }
    return get_connection().count(index=self.index_name, body=search_query)

def _test():
  c = ContextStore()
  print(c.delete_index())
  # print(c.create_index(delete_old=True))


if __name__ == "__main__":
  _test()
