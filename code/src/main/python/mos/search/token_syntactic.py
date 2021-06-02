import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from store import elastic_store, mongo_store
from utils import cache, logger
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_token_store():
  if properties.STORE == "mongo":
    return mongo_store.TokenStore()
  raise RuntimeError("Not supported for '%s'" % properties.STORE)


def get_elastic_store():
  return elastic_store.TokenStore()


def compare_tokens():
  token_folder = os.path.join(properties.CONFIG.CODE_HOME, "_rough", "syntactic", properties.CONFIG.get_dataset())
  store = elastic_store.TokenStore()
  function_store = mongo_store.FunctionStore(properties.CONFIG.get_dataset())
  n_python = store.count({"match": {"language": properties.LANGUAGE_PYTHON}})['count']
  n_java = store.count({"match": {"language": properties.LANGUAGE_JAVA}})['count']
  python_res = store.search({"match": {"language": properties.LANGUAGE_PYTHON}}, limit=n_python)
  for i, py_hit in enumerate(python_res['hits']['hits']):
    contents = []
    file_name = os.path.join(token_folder, "py_%d.txt" % i)
    LOGGER.info("Processing %d/%d ... " % (i + 1, n_python))
    tokens = py_hit["_source"]['tokens']
    # if len(tokens) < 5:
    #   continue
    token_query = []
    for token in tokens:
      token_query.append({
        "term": {"tokens": token}
      })
    java_search_query = {
      "bool": {
        "should": {
          "match": {
            "tokens": " ".join(tokens)
          }
        },
        "must": {
          "match": {"language": properties.LANGUAGE_JAVA}
        }
      }
    }
    # contents.append("### Py Tokens: %s \n" % ", ".join(tokens))
    contents.append("### Py functions\n")
    py_func_names = py_hit["_source"]['names']
    for func in function_store.load_py_functions_from_names(py_func_names)[:5]:
      contents.append(func['body'])

    # print("Num Py functions: %d" % len(py_func_names))
    # py_function_bodies = [func['body'] for func in function_store.load_py_functions_from_names(py_func_names)[:5]]
    # # python_funcs = py_function_store.load_functions(function_names=py_func_names)
    # print(py_func_names)
    # print(function_bodies)
    # exit()
    java_res = store.search(java_search_query, limit=10)
    for j, java_hit in enumerate(java_res['hits']['hits']):
      contents.append("*********************************\n")
      contents.append("#### Score: %0.5f\n\n" % java_hit["_score"])
      # contents.append("#### Java Tokens: %s \n" % ", ".join(java_hit["_source"]['tokens']))
      java_func_names = java_hit["_source"]['names']
      for j_func_name in java_func_names[:3]:
        j_func = function_store.load_metadata({"name": j_func_name})
        contents.append(j_func["body"])
        # print("%d. # Functions = %d" % (j, len(java_hit["_source"]['names'])))
    # print(tokens)
    # print(java_res)
    # exit()
    cache.write_file(file_name, "\n".join(contents))


def _test():
  compare_tokens()


if __name__ == "__main__":
  _test()
