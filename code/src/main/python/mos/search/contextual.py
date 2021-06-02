from __future__ import division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.helpers import ast_utils
from mos.helpers import contexter
from mos.search_store import code_store, elastic_store
from utils import cache, logger
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_elastic_store():
  return elastic_store.ContextStore(elastic_store.ContextStore.CONTEXT_INDEX)


def get_code_store():
  return code_store.CodeStore()


def tokenize_java(code):
  return contexter.tokenize_java_function(code)


def tokenize_py(code):
  return contexter.tokenize_py_function(code)


def jaccard_index(tokens_a, tokens_b):
  if not tokens_a and not tokens_b:
    return 1.0
  elif not tokens_a or not tokens_b:
    return 0.0
  else:
    return len(tokens_a.intersection(tokens_b)) / len(tokens_a.union(tokens_b))


def search(code, source_language, target_language, limit=10):
  # 1. Tokenize
  tokens = None
  if source_language == properties.LANGUAGE_PYTHON:
    tokens = tokenize_py(code)
  elif source_language == properties.LANGUAGE_JAVA:
    tokens = tokenize_java(code)
  else:
    raise RuntimeError("Unsupported language: %s" % source_language)
  # 2. Build search query
  search_query = {
    "bool": {
      "should": {
        "match": {
          "contextualTokens": " ".join(tokens)
        }
      },
      "must": {
        "match": {"language": target_language}
      }
    }
  }
  # 3. Fetch search results
  search_results = get_elastic_store().search(search_query, limit)
  # 4. return search results
  ret_results = []
  for i, hit in enumerate(search_results['hits']['hits']):
    score = hit['_score']
    code_block = get_code_store().fetch_code_block(hit["_source"]['uid'])
    result = {
      "score": score,
      "uid": hit["_source"]['uid'],
      "tokens": hit["_source"]["contextualTokens"],
      "code": code_block['code']
    }
    ret_results.append(result)
  return ret_results


def compare_tokens():
  token_folder = os.path.join(properties.CONFIG.CODE_HOME, "_rough", "context", properties.CONFIG.get_dataset())
  store = get_elastic_store()
  mongo_store = get_code_store()
  n_python = store.count({"match": {"language": properties.LANGUAGE_PYTHON}})['count']
  n_java = store.count({"match": {"language": properties.LANGUAGE_JAVA}})['count']
  python_res = store.search({"match": {"language": properties.LANGUAGE_PYTHON}}, limit=n_python)
  for i, py_hit in enumerate(python_res['hits']['hits']):
    contents = []
    file_name = os.path.join(token_folder, "py_%d.txt" % i)
    LOGGER.info("Processing %d/%d ... " % (i + 1, n_python))
    tokens = py_hit["_source"]['contextualTokens']
    if len(tokens) < 5:
      continue
    token_query = []
    for token in tokens:
      token_query.append({
        "term": {"contextualTokens": token}
      })
    java_search_query = {
      "bool": {
        "should": {
          "match": {
            "contextualTokens": " ".join(tokens)
          }
        },
        "must": {
          "match": {"language": properties.LANGUAGE_JAVA}
        }
      }
    }
    contents.append("### Py Tokens: %s \n" % ", ".join(tokens))
    contents.append("### Py functions\n")
    py_block = mongo_store.fetch_code_block(py_hit["_source"]["uid"])
    contents.append(py_block["code"])
    java_res = store.search(java_search_query, limit=10)
    for j, java_hit in enumerate(java_res['hits']['hits']):
      contents.append("*********************************\n")
      contents.append("#### Score: %0.5f\n\n" % java_hit["_score"])
      contents.append("#### Java Tokens: %s \n" % ", ".join(java_hit["_source"]['contextualTokens']))
      java_block = mongo_store.fetch_code_block(java_hit["_source"]["uid"])
      contents.append(java_block["code"])
    cache.write_file(file_name, "\n".join(contents))


def _test_java_search():
  code = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt")
  results = search(code,
                   source_language=properties.LANGUAGE_PYTHON,
                   target_language=properties.LANGUAGE_JAVA,
                   limit=5)
  print(results)


def _test_py_search():
  code = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_java_code.txt")
  results = search(code,
                   source_language=properties.LANGUAGE_JAVA,
                   target_language=properties.LANGUAGE_PYTHON,
                   limit=5)
  print(results)


def _test_java():
  code = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_java_code.txt")
  # contexter.tokenize_java_function(code)
  print(contexter.tokenize_java_function(code))


def _test():
  # fetch_tokens_for_language(properties.LANGUAGE_PYTHON)
  # fetch_tokens_for_language(properties.LANGUAGE_JAVA)
  compare_tokens()


if __name__ == "__main__":
  _test_py_search()
