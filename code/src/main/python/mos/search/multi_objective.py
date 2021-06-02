import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils import logger, cache
from utils.lib import O
from mos.helpers import contexter
from mos.search_store import code_store
from mos.search import contextual
from mos.search.tree import java_tree, py_tree, common, distances as tree_dist
from mos.blocks.code_block import CodeBlock
import properties
import random


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_code_store():
  return code_store.CodeStore()


def get_tree(code, language, is_function=False):
  if language == properties.LANGUAGE_PYTHON:
    return py_tree.get_py_tree(code, extract_first_func=is_function)
  elif language == properties.LANGUAGE_JAVA:
    return java_tree.get_java_tree(code, wrap_class=is_function)
  else:
    raise RuntimeError("Unsupported language: %s" % language)


def get_contextual_tokens(code, language):
  if language == properties.LANGUAGE_PYTHON:
    return contexter.tokenize_py_function(code)
  elif language == properties.LANGUAGE_JAVA:
    return contexter.tokenize_java_function(code)
  else:
    raise RuntimeError("Unsupported language: '%s'" % language)


def load_results(code, source_language, target_language, limit=None, is_function=False):
  source_code_tree = get_tree(code, source_language, is_function=is_function)
  source_tokens = get_contextual_tokens(code, source_language)
  code_blocks_db = get_code_store().get_code_blocks(language=target_language)
  scores = {}
  index = 0
  for code_block_db in code_blocks_db:
    index += 1
    LOGGER.info("Processing %d record ... " % index)
    code_block = CodeBlock.from_bson(code_block_db)
    score = {
      "uid": code_block.uid,
      # "code": code_block.code,
    }
    # score["ast"] = random.randint(10, 100)
    # import time
    # start = time.time()
    # a = tree_dist.zhang_shasha_distance(source_code_tree, code_block.ast)
    # print(time.time() - start, a)
    # start = time.time()
    # b = tree_dist.apted_distance(code_block.ast, source_code_tree)
    # print(time.time() - start, b)
    # exit()
    if code_block.ast:
      score["ast"] = tree_dist.apted_distance(source_code_tree, code_block.ast)
      # score["ast"] = common.Node.graph_edit_distance(source_code_tree, code_block.ast)
      # score["ast"] = common.Node.zhang_shasha_distance(source_code_tree, code_block.ast)
    else:
      score["ast"] = float("Inf")
    if code_block.contextual_tokens:
      score["contextual"] = contextual.jaccard_index(source_tokens, code_block.contextual_tokens)
    else:
      score["contextual"] = 0.0
    scores[score["uid"]] = score
    if len(scores) == 5:
      break
  # TODO: 2. Rank results
  return scores


def less(a, b):
  if a < b:
    return 1
  elif a > b:
    return -1
  else:
    return 0


def more(a, b):
  return less(b, a)


class Point(O):
  def __init__(self, uid, **kwargs):
    O.__init__(self, **kwargs)
    self.uid = uid
    self.dominated = []
    self.dominating = 0
    self.rank = None


def loo(pts):
  for i in xrange(len(pts)):
    yield pts[i], pts[:i] + pts[i+1:]


def better(one, two, keys=["ast", "contextual"], betters={"ast": less, "contextual": more}, preferences={"ast": 1, "contextual": 2}):
  one_at_least_once = False
  two_at_least_once = False
  for i, k in enumerate(keys):
    status = betters[k](one[k], two[k])
    if status == -1:
      two_at_least_once = True
    elif status == 1:
      one_at_least_once = True
    if one_at_least_once and two_at_least_once:
      break
  if one_at_least_once == two_at_least_once:
    if not preferences:
      return 0
    sorted_keys = sorted(preferences.keys(), key=lambda x: preferences[x])
    for sorted_k in sorted_keys:
      if sorted_k not in betters:
        continue
      status = betters[sorted_k](one[sorted_k], two[sorted_k])
      if status == -1:
        return 2
      elif status == 1:
        return 1
    return 0
  elif one_at_least_once:
    return 1
  elif two_at_least_once:
    return 2
  else:
    raise RuntimeError("WTF!!")


def nsga(scores, keys, betters, preferences):
  points = {score["uid"]: Point(score["uid"]) for score in scores.values()}
  frontiers = []
  front1 = []
  score_vals = scores.values()
  for one, rest in loo(score_vals):
    for two in rest:
      dom_status = better(one, two, keys, betters, preferences)
      if dom_status == 1:
        points[one["uid"]].dominated.append(points[two["uid"]])
      elif dom_status == 2:
        points[one["uid"]].dominating += 1
    if points[one["uid"]].dominating == 0:
      points[one["uid"]].rank = 1
      front1.append(points[one["uid"]])
  current_rank = 1
  frontiers.append(front1)
  while True:
    front2 = []
    for one in front1:
      for two in one.dominated:
        two.dominating -= 1
        if two.dominating == 0:
          two.rank = current_rank + 1
          front2.append(two)
    current_rank += 1
    if len(front2) == 0:
      break
    else:
      frontiers.append(front2)
      front1 = front2
  sorted_scores = []
  for front in frontiers:
    random.shuffle(front)
    for one in front:
      sorted_scores.append(scores[one["uid"]])
  return sorted_scores


def _test():
  code = cache.read_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_py_code.txt")
  res = load_results(code, source_language=properties.LANGUAGE_PYTHON, target_language=properties.LANGUAGE_JAVA)
  sorted_res = nsga(res, keys=["ast", "contextual"], betters={"ast": less, "contextual": more}, preferences={"ast": 1, "contextual": 2})
  for r in sorted_res:
    print(r)

if __name__ == "__main__":
  _test()