import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from mos.search_store import code_store, elastic_store
from utils import logger, cache
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def preprocess_code(code):
  # No preprocessing at the moment
  return code


def index_files(language=None, delete_old_index=False):
  store = code_store.CodeStore()
  fields = ["uid", "code", "language"]
  n_code_blocks = store.count_code_blocks(language, isMethod=True)
  code_blocks = store.get_code_blocks(language=language, fields=fields, isMethod=True)
  docs = []
  for cb in code_blocks:
    if len(docs) % 1000 == 0:
      LOGGER.info("Processing '%s' code block %d/%d .... " % (language, len(docs) + 1, n_code_blocks))
    doc = {
      "uid": cb["uid"],
      "language": cb["language"],
      "code": preprocess_code(cb["code"])
    }
    docs.append(doc)
  index_store = elastic_store.ContextStore(index_name=elastic_store.ContextStore.BASELINE_INDEX)
  index_store.create_index(delete_old=delete_old_index)
  index_store.index_documents(docs)


if __name__ == "__main__":
  index_files(language=properties.LANGUAGE_JAVA, delete_old_index=True)
  index_files(language=properties.LANGUAGE_PYTHON, delete_old_index=False)
