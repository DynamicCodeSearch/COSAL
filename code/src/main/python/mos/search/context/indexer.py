import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search_store import code_store, elastic_store
from mos.search.cacher import tfidf_cache
from utils import logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_code_store():
  return code_store.CodeStore()


def index_context_tokens():
  mongo_store = get_code_store()
  n_code_blocks = mongo_store.count_code_blocks()
  fields = ["uid", "contextualTokens", "language"]
  code_blocks = mongo_store.get_code_blocks(language=None, fields=fields)
  index = 0
  docs = []
  top_tfidf_tokens = tfidf_cache.load_top_tfidf_tokens()
  for cb in code_blocks:
    index += 1
    if not cb.get("contextualTokens", None):
      continue
    if index % 1000 == 0:
      LOGGER.info("Processing document %d/%d ... " % (index, n_code_blocks))
    del cb["_id"]
    top_tokens = list(top_tfidf_tokens.intersection(set(cb["contextualTokens"])))
    cb["tfidfTokens"] = top_tokens
    docs.append(cb)
  index_store = elastic_store.ContextStore(index_name=elastic_store.ContextStore.CONTEXT_INDEX)
  index_store.create_index(delete_old=True)
  index_store.index_documents(docs)


if __name__ == "__main__":
  index_context_tokens()
