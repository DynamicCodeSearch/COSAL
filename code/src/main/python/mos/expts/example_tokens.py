from __future__ import division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.helpers import contexter
from utils import cache, logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_tokens(code, language):
  if language == properties.LANGUAGE_JAVA:
    tokens = contexter.tokenize_java_function(code)
  elif language == properties.LANGUAGE_PYTHON:
    tokens = contexter.tokenize_py_function(code)
  else:
    raise RuntimeError("Unsupported language: '%s'" % language)
  return tokens


def tokenize(folder_path, language):
  for file_path in cache.list_files(folder_path, is_absolute=True, extension=".txt"):
    file_name = cache.get_file_name(file_path)
    LOGGER.info("Generating '%s' file: %s" % (language, file_name))
    content = cache.read_file(file_path)
    tokens = get_tokens(content, language)
    print("### Tokens")
    print(file_name)
    print(tokens)


def jaccard(a, b):
  a = set(a)
  b = set(b)
  return len(a.intersection(b)) / len(a.union(b))


def compute_jaccard():
  tokens = {
    "3a-getEvens": "getevens, get, max, arraylist, list, add, integer, array, evens".split(", "),
    "3b-all_odds": "allodds, xrange, odds, append".split(", "),
    "3c-removeOdds": "filter, collect, removeOdds, stream, nums, integer, remove, odds, list".split(", "),
    "3d-func": "func, intstream, stream, range, toarray, array, list, integer, arraylist, length, add".split(", "),
    "3e-get_evens": "ifilter, filter, range, getevens, get, max, functools, evens, odds".split(", "),
    "3f-even_nums": "even, evennums, nums, max, val, maxval, range".split(", ")
  }
  keys = sorted(tokens.keys())
  for i in range(len(keys) - 1):
    for j in range(i+1, len(keys)):
      print(keys[i], keys[j], jaccard(tokens[keys[i]], tokens[keys[j]]))


def _main():
  # tokenize("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/java", properties.LANGUAGE_JAVA)
  # tokenize("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/py", properties.LANGUAGE_PYTHON)
  compute_jaccard()


if __name__ == "__main__":
  _main()
