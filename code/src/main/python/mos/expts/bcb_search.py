import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.expts import submission_search
from mos.search_store.code_store import CodeStore, ASTDistanceStore
from mos.search_store.elastic_store import ContextStore
from mos.search import multi_objective as mo
from utils import logger, cache
import properties

from joblib import Parallel, delayed
import re

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
UID_REGEX = r'P([0-9]+)-S[0-9]+'


def get_code_store():
  return CodeStore()


def get_ast_distance_store():
  return ASTDistanceStore()


def get_elastic_store():
  return ContextStore(index_name=ContextStore.CONTEXT_INDEX)


def get_meta_file(file_prefix):
  return os.path.join(properties.CONFIG.CODE_HOME, "meta_results",
                      properties.CONFIG.get_dataset(), "search", "%s.pkl" % file_prefix)


def get_problem_ids(search_results):
  return map(lambda s: re.match(UID_REGEX, s['uid']).group(1), search_results)


def search_submission(code_block_db, search_params=["ast", "contextualTokens", "semantic"], search_limit=1000):
  """
  :param code_block_db: Instance of code block db
  :param search_params: List of params to search. Options - [ast, contextualTokens/tfidfTokens]
  :param search_limit: Limit of search. Optional. Defaults to 1000
  :return: List of search results
  """
  defaults = {}
  mo_keys = []
  mo_betters = {}
  mo_preferences = {"ast": 1, "context": 2}
  search_results = {}
  if "ast" in search_params:
    search_results["ast"] = submission_search.ast_search(code_block_db["uid"], search_limit)
    mo_keys.append("ast")
    mo_betters["ast"] = mo.less
    defaults["ast"] = float("inf")
  if "contextualTokens" in search_params or "tfidfTokens" in search_params:
    tokens = submission_search.get_top_tokens(code_block_db["contextualTokens"])
    token_key = "contextualTokens"
    if "tfidfTokens" in search_params:
      tokens = submission_search.get_top_tokens(tokens)
      token_key = "tfidfTokens"
    search_results["context"] = submission_search.contextual_search(properties.LANGUAGE_JAVA, tokens, token_key, search_limit)
    mo_keys.append("context")
    mo_betters["context"] = mo.more
    defaults["context"] = float("-inf")
  if "semantic" in search_params:
    search_results["semantic"] = submission_search.semantic_search(code_block_db["sourceFile"],properties.LANGUAGE_JAVA, search_limit)
    mo_keys.append("semantic")
    mo_betters["ast"] = mo.more
    defaults["ast"] = float("-inf")
  clean_results, partial_results = submission_search.merge_search_results(search_results, defaults)
  results = clean_results if len(clean_results) > 0 else partial_results
  sorted_results = mo.nsga(results, keys=mo_keys, betters=mo_betters, preferences=mo_preferences)
  problem_ids = get_problem_ids(sorted_results)
  return sorted_results, problem_ids


def rank_results(query_id, search_ids):
  best_rank = None
  matches = []
  for i, search_id in enumerate(search_ids):
    if best_rank is not None and i >= 12:
      break
    if best_rank is None and search_id == query_id:
      best_rank = i + 1
    if i < 12 and search_id == query_id:
      matches.append(i + 1)
  rank_meta = {
    "best_rank": best_rank,
    "matches": matches
  }
  return rank_meta


def run_block(code_block_db, search_params, search_limit, index, n_code_blocks, save_n_top=20):
  uid = code_block_db["uid"]
  if index % 1 == 0:
    LOGGER.info("Processing document %d/%d ... " % (index + 1, n_code_blocks))
  # ast_computed_count = get_ast_distance_store().count_nodes_for_uid(uid)
  # if ast_computed_count == 0:
  #   if index % 10 == 0:
  #     LOGGER.info("@COSAL: Looks like ast comparison has not been performed for this node.!!")
  #   return None
  problem_id = code_block_db.get("problemId", None)
  if problem_id is None:
    return None
  search_results = submission_search.search_submission(code_block_db, search_params, search_limit)
  search_ids = get_problem_ids(search_results)
  rank_meta = rank_results(problem_id, search_ids)
  # if len(search_results) > save_n_top:
  #   search_results = search_results[:save_n_top]
  data_results = {
    "uid": uid,
    # "search_results": search_results,
    "rank_meta": rank_meta
  }
  return data_results


def run_serial(search_params, save_file_prefix, search_limit=1000):
  LOGGER.info("# Running submission search for python documents for search_params: '%s' .... " % ','.join(search_params))
  index = 0
  n_code_blocks = get_code_store().count_code_blocks(language=properties.LANGUAGE_JAVA)
  save_n_top = 20
  code_blocks = get_code_store().get_code_blocks(language=properties.LANGUAGE_JAVA)
  cleaned = {}
  for index, code_block_db in enumerate(code_blocks):
    node = run_block(code_block_db, search_params, search_limit, index, n_code_blocks, save_n_top)
    if node is None:
      continue
    cleaned[node["uid"]] = node
  pkl_file = get_meta_file(save_file_prefix)
  cache.save_pickle(pkl_file, cleaned)


def runner_parallel(search_params, save_file_prefix, search_limit=1000):
  LOGGER.info("# Running submission search for python documents for search_params: '%s' .... " % ','.join(search_params))
  index = 0
  n_code_blocks = get_code_store().count_code_blocks(language=properties.LANGUAGE_JAVA)
  test_limit = None  # TODO. Remove this
  save_n_top = 20
  # code_blocks = get_code_store().get_random_code_blocks(language=properties.LANGUAGE_JAVA, limit=10)
  code_blocks = get_code_store().get_code_blocks(language=properties.LANGUAGE_JAVA)
  # run_block(code_blocks.next(), search_params, search_limit, index, n_code_blocks)
  nodes = Parallel(n_jobs=-1)(delayed(run_block)(code_block_db, search_params, search_limit, index, n_code_blocks, save_n_top)
                             for index, code_block_db in enumerate(code_blocks))
  cleaned = {}
  for node in nodes:
    if node is None:
      continue
    cleaned[node["uid"]] = node
  pkl_file = get_meta_file(save_file_prefix)
  str.rindex()
  cache.save_pickle(pkl_file, cleaned)


def _analyze():
  submission_search.analyze_search_pkl("contextual")
  # submission_search.analyze_pkl("tfidf")


def _main():
  search_limit = 1000
  runner_parallel(search_params=["contextualTokens"], save_file_prefix="contextual", search_limit=search_limit)
  runner_parallel(search_params=["tfidfTokens"], save_file_prefix="tfidf", search_limit=search_limit)


if __name__ == "__main__":
  # _main()
  _analyze()
