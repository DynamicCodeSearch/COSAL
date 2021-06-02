import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.helpers import java_parse_utils, ast_utils
from store import mongo_store
from utils import cache, logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
BASE_SEARCH_FOLDER = os.path.join(properties.CONFIG.CODESEER_HOME, "google-search")


def load_function_store():
  return mongo_store.FunctionStore(properties.CONFIG.get_dataset())


def get_python_body(content):
  return ast_utils.get_function_body_as_str(ast_utils.remove_comments_and_docstrings(content)).strip()


def get_java_body(content):
  return java_parse_utils.get_method_body(java_parse_utils.replace_comments(content)).strip()


def save_files_for_index(language=None):
  if not language:
    LOGGER.info("Saving files for all languages ... ")
    save_files_for_index(language=properties.LANGUAGE_PYTHON)
    save_files_for_index(language=properties.LANGUAGE_JAVA)
    return
  elif language == properties.LANGUAGE_PYTHON:
    body_parser = get_python_body
    docs = load_function_store().load_py_generated_functions()
  elif language == properties.LANGUAGE_JAVA:
    body_parser = get_java_body
    docs = load_function_store().load_java_generated_functions()
  else:
    raise RuntimeError("@COSAL: Unsupported language: %s!" % language)
  LOGGER.info("Saving files for language: '%s' .... " % language)
  cleaned_hashes = {}
  folder = os.path.join(BASE_SEARCH_FOLDER, properties.CONFIG.get_dataset(), language)
  count = 0
  for doc in docs:
    file_name = doc["name"]
    code_body = body_parser(doc["body"])
    hashed = hash(code_body)
    if hashed in cleaned_hashes:
      continue
    file_path = os.path.join(folder, "%s.txt" % file_name)
    cache.write_file(file_path, code_body)
    count += 1
  LOGGER.info("Saved '%d' files for language '%s'!" % (count, language))


if __name__ == "__main__":
  save_files_for_index()
