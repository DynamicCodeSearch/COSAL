import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search_store import code_store
from utils import logger, cache
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_base_folder(language):
  return os.path.join(properties.CONFIG.CODESEER_HOME, "github-search", properties.CONFIG.get_dataset(), language)


def index_files(language):
  store = code_store.CodeStore()
  fields = ["uid", "code", "language"]
  n_code_blocks = store.count_code_blocks(language, isMethod=True)
  code_blocks = store.get_code_blocks(language=language, fields=fields, isMethod=True)
  index = 0
  base_folder = get_base_folder(language)
  for cb in code_blocks:
    file_path = os.path.join(base_folder, "%s.txt" % cb["uid"])
    if index % 1000 == 0:
      LOGGER.info("Saving '%s' code block %d/%d .... " % (language, index + 1, n_code_blocks))
    cache.write_file(file_path, cb["code"].encode('utf-8'))
    index += 1


def search(code):
  # TODO: Implement search.
  raise NotImplementedError("Implement this !")


if __name__ == "__main__":
  index_files(properties.LANGUAGE_PYTHON)
  index_files(properties.LANGUAGE_JAVA)
