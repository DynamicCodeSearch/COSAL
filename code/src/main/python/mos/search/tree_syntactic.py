import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.tree import java_tree, py_tree
from mos.search.tree.common import Node
from mos.search_store import code_store
from utils import cache
import properties

import ast


def get_code_store():
  return code_store.CodeStore()


def get_java_tree(code):
  return java_tree.get_java_tree(code, wrap_class=True)


def get_py_tree(code):
  return py_tree.get_py_tree(code, extract_first_func=True)


def to_json(ast_str):
  return ast.literal_eval(ast_str)


def search(code, source_language, target_language, limit=10):
  source_code_tree = None
  if source_language == properties.LANGUAGE_PYTHON:
    source_code_tree = get_py_tree(code)
  elif source_language == properties.LANGUAGE_JAVA:
    source_code_tree = get_java_tree(code)
  else:
    raise RuntimeError("Unsupported language: %s" % source_language)
  code_blocks_db = get_code_store().get_code_blocks(language=target_language)
  code_blocks = []
  for code_block_db in code_blocks_db:
    if 'ast' not in code_block_db:
      continue
    code_ast = Node.from_bson(to_json(code_block_db['ast']))
    code_score = Node.zhang_shasha_distance(source_code_tree, code_ast)
    code_block = {
      "score": code_score,
      "uid": code_block_db['uid'],
      "code": code_block_db['code']
    }
    code_blocks.append(code_block)
  code_blocks = sorted(code_blocks, key=lambda cb: cb['score'])
  if limit is not None and limit >= 0:
    return code_blocks[:limit]
  return code_blocks


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


def _test():
  # java_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_java_code.txt"
  # contents = cache.read_file(java_path)
  # java_node = java_tree.get_java_tree(contents, wrap_class=True)
  # python_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt"
  # contents = cache.read_file(python_path)
  # python_node = py_tree.get_py_tree(contents, extract_first_func=False)
  # print(Node.zhang_shasha_distance(java_node, python_node))
  print("def solve():\n    S = input()\n    A, B, C, D = map(int, input().split())\n\n    print(S[:A] + '\"' + S[A:B] + '\"' + S[B:C] + '\"' + S[C:D] + '\"' + S[D:])\n\n\nif __name__ == '__main__':\n    solve()\n")

if __name__ == "__main__":
  _test()
  # _test_py_search()
