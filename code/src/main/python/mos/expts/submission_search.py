from __future__ import division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.cacher import tfidf_cache
from mos.search_store.code_store import CodeStore, ASTDistanceStore, ExecStore
from mos.search_store.elastic_store import ContextStore
from mos.blocks.contest_meta_block import ContestMeta
from mos.search import multi_objective as mo
from utils import logger, cache, stat

from joblib import Parallel, delayed
import multiprocessing
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_code_store():
  return CodeStore()


def get_ast_distance_store():
  return ASTDistanceStore()


def get_exec_store():
  return ExecStore()


def get_elastic_store():
  return ContextStore(index_name=ContextStore.CONTEXT_INDEX)


def make_search_query(language, tokens, token_key):
  return {
    "bool": {
      "should": {
        "match": {
          token_key: " ".join(tokens)
        }
      },
      "must": {
        "match": {"language": language}
      }
    }
  }


def contextual_search(language, tokens, token_key, search_limit):
  search_query = make_search_query(language, tokens, token_key)
  search_results = {}
  for i, hit in enumerate(get_elastic_store().search(search_query, search_limit)["hits"]["hits"]):
    search_results[hit["_source"]["uid"]] = {
      "uid": hit["_source"]["uid"],
      "tokens": hit["_source"][token_key],
      "score": hit["_score"],
    }
  return search_results


def ast_search(source_uid, search_limit):
  search_results = {}
  similar_nodes = get_ast_distance_store().get_most_similar_nodes(source_uid, search_limit)
  if not similar_nodes:
    return search_results
  for node in similar_nodes:
    target_uid = node["uid2"] if node["uid1"] == source_uid else node["uid1"]
    search_results[target_uid] = {
      "uid": target_uid,
      "score": node["distance"]
    }
  return search_results


def semantic_search(source_file_path, language, search_limit):
  search_results = {}
  exec_store = get_exec_store()
  n_similar_nodes = exec_store.count_exec_distances_for_file(source_file_path)
  if n_similar_nodes == 0:
    return search_results
  similar_nodes = exec_store.get_exec_distances_for_file(source_file_path)
  source_file_path = cache.get_repo_local_path(source_file_path)
  query_snippets = {}
  result_files = {}
  for similar_node in similar_nodes:
    if similar_node["file1"] == source_file_path:
      q_snippet = similar_node["method1"]
      file_result = result_files.get(similar_node["file2"], {})
      if q_snippet not in file_result or file_result[q_snippet]["score"] < similar_node["score"]:
        file_result[q_snippet] = similar_node
      result_files[similar_node["file2"]] = file_result
    elif similar_node["file2"] == source_file_path:
      q_snippet = similar_node["method2"]
      file_result = result_files.get(similar_node["file1"], {})
      if q_snippet not in file_result or file_result[q_snippet]["score"] < similar_node["score"]:
        file_result[q_snippet] = similar_node
      result_files[similar_node["file1"]] = file_result
  search_results = {}
  for target_file, file_result in result_files.items():
    target_id = get_code_store().get_code_block_id(target_file, language)
    if not target_id:
      continue
    score = 0.0
    for q_snippet, similar_node in file_result.items():
      score += similar_node["score"]
    search_results[target_id] = {
      "uid": target_id,
      "score": score
    }
  return search_results


def merge_search_results(search_results, defaults):
  search_fields = search_results.keys()
  all_keys = set()
  for field in search_fields:
    all_keys = all_keys.union(search_results[field].keys())
  clean_results = {}
  partial_results = {}
  for uid in all_keys:
    result = {"uid": uid}
    all_present = True
    for field in search_fields:
      if uid in search_results[field]:
        result[field] = search_results[field][uid]["score"]
      else:
        all_present = False
        result[field] = defaults[field]
    if all_present:
      clean_results[uid] = result
    else:
      partial_results[uid] = result
  return clean_results, partial_results


def get_top_tokens(tokens):
  all_top_tokens = tfidf_cache.load_top_tfidf_tokens()
  return list(set(tokens).intersection(all_top_tokens))


def get_contest_details(uid):
  cb = get_code_store().fetch_code_block(uid)
  contest_meta = cb.get("contestMeta", None)
  if contest_meta:
    return ContestMeta.from_bson(contest_meta)
  return None


def get_contest_meta(search_results):
  contests_meta = []
  for search_result in search_results:
    contests_meta.append(get_contest_details(search_result["uid"]))
  return contests_meta


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
    search_results["ast"] = ast_search(code_block_db["uid"], search_limit)
    mo_keys.append("ast")
    mo_betters["ast"] = mo.less
    defaults["ast"] = float("inf")
  if "contextualTokens" in search_params or "tfidfTokens" in search_params:
    tokens = get_top_tokens(code_block_db["contextualTokens"])
    token_key = "contextualTokens"
    if "tfidfTokens" in search_params:
      tokens = get_top_tokens(tokens)
      token_key = "tfidfTokens"
    search_results["context"] = contextual_search(properties.LANGUAGE_JAVA, tokens, token_key, search_limit)
    mo_keys.append("context")
    mo_betters["context"] = mo.more
    defaults["context"] = float("-inf")
  if "semantic" in search_params:
    search_results["semantic"] = semantic_search(code_block_db["sourceFile"], properties.LANGUAGE_JAVA, search_limit)
    mo_keys.append("semantic")
    mo_betters["ast"] = mo.more
    defaults["ast"] = float("-inf")
  clean_results, partial_results = merge_search_results(search_results, defaults)
  results = clean_results if len(clean_results) > 0 else partial_results
  sorted_results = mo.nsga(results, keys=mo_keys, betters=mo_betters, preferences=mo_preferences)
  return sorted_results


def rank_results(query_contest_meta, contests_meta):
  query_contest_key = query_contest_meta.make_key()
  best_rank = None
  matches = []
  for i, contest_meta in enumerate(contests_meta):
    if best_rank is not None and i >= 12:
      break
    result_contest_key = contest_meta.make_key()
    if best_rank is None and query_contest_key == result_contest_key:
      best_rank = i + 1
    if i < 12 and query_contest_key == result_contest_key:
      matches.append(i + 1)
  rank_meta = {
    "best_rank": best_rank,
    "matches": matches
  }
  return rank_meta


def get_meta_file(file_prefix):
  return os.path.join(properties.CONFIG.CODE_HOME, "meta_results",
                      properties.CONFIG.get_dataset(), "search", "%s.pkl" % file_prefix)


def run_block(code_block_db, search_params, search_limit, index, n_code_blocks, save_n_top=20):
  uid = code_block_db["uid"]
  if index % 1 == 0:
    LOGGER.info("Processing document %d/%d ... " % (index + 1, n_code_blocks))
  ast_computed_count = get_ast_distance_store().count_nodes_for_uid(uid)
  if ast_computed_count == 0:
    if index % 10 == 0:
      LOGGER.info("@COSAL: Looks like ast comparison has not been performed for this node.!!")
    return None
  if code_block_db.get("contestMeta", None) is None:
    return None
  query_contest_meta = ContestMeta.from_bson(code_block_db["contestMeta"])
  search_results = search_submission(code_block_db, search_params, search_limit)
  contests_meta = get_contest_meta(search_results)
  rank_meta = rank_results(query_contest_meta, contests_meta)
  # if len(search_results) > save_n_top:
  #   search_results = search_results[:save_n_top]
  data_results = {
    "uid": uid,
    # "search_results": search_results,
    "rank_meta": rank_meta
  }
  return data_results


def runner_parallel(search_params, save_file_prefix, search_limit=1000):
  LOGGER.info("# Running submission search for python documents for search_params: '%s' .... " % ','.join(search_params))
  index = 0
  n_code_blocks = get_code_store().count_code_blocks(language=properties.LANGUAGE_PYTHON)
  test_limit = None  # TODO. Remove this
  save_n_top = 20
  code_blocks = get_code_store().get_random_code_blocks(language=properties.LANGUAGE_PYTHON, limit=30)
  # cleaned = {}
  # for index, code_block_db in enumerate(code_blocks):
  #   node = run_block(code_block_db, search_params, search_limit, n_code_blocks, save_n_top)
  #   print(123)
  #   if node is None:
  #     print(456)
  #     continue
  #   print(789)
  #   cleaned[node["uid"]] = node
  nodes = Parallel(n_jobs=8)(delayed(run_block)(code_block_db, search_params, search_limit, index, n_code_blocks, save_n_top)
                              for index, code_block_db in enumerate(code_blocks))
  cleaned = {}
  for node in nodes:
    if node is None:
      continue
    cleaned[node["uid"]] = node
  pkl_file = get_meta_file(save_file_prefix)
  cache.save_pickle(pkl_file, cleaned)


# def runner(search_params, search_limit=1000, file_prefix="ast_context"):
#   index = 0
#   n_code_blocks = get_code_store().count_code_blocks(language=properties.LANGUAGE_PYTHON)
#   data_results = {}
#   for code_block_db in get_code_store().get_code_blocks(properties.LANGUAGE_PYTHON):
#   # for code_block_db in [get_code_store().fetch_code_block("e466d35a4a8e4403b027ba840053ea56")]:
#     uid = code_block_db["uid"]
#     index += 1
#     if index % 1 == 0:
#       LOGGER.info("Processing document %d/%d ... " % (index, n_code_blocks))
#     ast_computed_count = get_ast_distance_store().count_nodes_for_uid(uid)
#     if ast_computed_count == 0:
#       LOGGER.info("@COSAL: Looks like ast comparison has not been performed for this node.!!")
#       continue
#     if code_block_db.get("contestMeta", None) is None:
#       continue
#     query_contest_meta = ContestMeta.from_bson(code_block_db["contestMeta"])
#     search_results = search_submission(code_block_db, search_params, search_limit)
#     rank_meta = rank_results(query_contest_meta, search_results)
#     data_results[uid] = {
#       "search_results": search_results,
#       "rank_meta": rank_meta
#     }
#     if len(data_results) == 1000:
#       break
#   pkl_file = get_meta_file(file_prefix)
#   cache.save_pickle(pkl_file, data_results)

def get_problem_counts(db_code_blocks):
  pc = {}
  for cb in db_code_blocks:
    key = ContestMeta.from_bson(cb["contestMeta"]).make_key()
    if key not in pc:
      pc[key] = 1
    else:
      pc[key] += 1
  return pc


def analyze_pkl(file_prefix):
  meta_data = cache.load_pickle(get_meta_file(file_prefix))
  best_ranks = []
  all_matches_in_top_10 = []
  n_top_10 = 0
  tp, fp, fn = 0, 0, 0
  py_seen, java_seen = set(), set()
  for uid, data_result in meta_data.items():
    res_key = ContestMeta.from_bson(get_code_store().fetch_code_block(uid)["contestMeta"]).make_key()
    py_seen.add(res_key)
    rank_meta = data_result["rank_meta"]
    best_rank = rank_meta["best_rank"]
    if best_rank == 1:
      java_seen.add(res_key)
    if best_rank <= 1:
      # Predicted rank as 1
      tp += 1
    elif best_rank <= 10:
      # Predicted rank in top 10
      fp += 1
    elif best_rank > 10:
      # Not predicted in top 10 hence failed to rank
      fn += 1
    best_ranks.append(rank_meta["best_rank"])
    matches_in_top_10 = rank_meta["matches_in_top_10"]
    if matches_in_top_10 > 0:
      n_top_10 += 1
    all_matches_in_top_10.append(matches_in_top_10)
  prec = tp / (tp + fp)
  print("Precision : %.4f" % prec)
  ## Recall
  java_cbs = get_code_store().get_code_blocks(language=properties.LANGUAGE_JAVA)
  java_problem_counts = get_problem_counts(java_cbs)
  r_total = 0
  r_fn = 0
  for key in py_seen:
    r_total += java_problem_counts[key]
  for key in py_seen - java_seen:
    r_fn += java_problem_counts[key]
  rec = (r_total - r_fn) / r_total
  print("Recall : %.4f" % rec)
  f1 = 2 * prec * rec / (prec + rec)
  print("F1 : %.4f" % f1)
  # print("## N top 10 ratio: %d/%d " % (n_top_10, len(meta_data)))
  # print("### Best Rank Summary:")
  # best_rank_stats = stat.Stat(best_ranks)
  # print(best_rank_stats.report())
  # print("### All Matches in top-10 Summary:")
  # all_matches_in_top_10_stats = stat.Stat(all_matches_in_top_10)
  # print(all_matches_in_top_10_stats.report())


def analyze_search_pkl(file_prefix):
  print("# Processing %s ... " % file_prefix)

  def ranks_less_than_k(ranks, k):
    cnt = 0
    for r in ranks:
      if r <= k:
        cnt += 1
      else:
        break
    return cnt

  meta_data = cache.load_pickle(get_meta_file(file_prefix))
  n = len(meta_data)
  rr = []
  p_1, p_3, p_5, p_10 = [], [], [], []
  r_1, r_3, r_5, r_10 = [], [], [], []
  for uid, data_result in meta_data.items():
    rank_meta = data_result["rank_meta"]
    best_rank = rank_meta["best_rank"]
    matches = sorted(rank_meta["matches"])
    if matches:
      rr.append(1/matches[0])
    else:
      rr.append(0)
    r_1.append(1 if matches and matches[0] <= 1 else 0)
    r_3.append(1 if matches and matches[0] <= 3 else 0)
    r_5.append(1 if matches and matches[0] <= 5 else 0)
    r_10.append(1 if matches and matches[0] <= 10 else 0)
    p_1.append(ranks_less_than_k(matches, 1) / 1)
    p_3.append(ranks_less_than_k(matches, 3) / 3)
    p_5.append(ranks_less_than_k(matches, 5) / 5)
    p_10.append(ranks_less_than_k(matches, 10) / 10)
  print("```")
  print("MRR         : %0.4f\n" % (sum(rr) / n))
  print("Precision@1 : %0.4f" % (sum(p_1) / n))
  print("Precision@3 : %0.4f" % (sum(p_3) / n))
  print("Precision@5 : %0.4f" % (sum(p_5) / n))
  print("Precision@10: %0.4f\n" % (sum(p_10) / n))
  print("Recall@1    : %0.4f" % (sum(r_1) / n))
  print("Recall@3    : %0.4f" % (sum(r_3) / n))
  print("Recall@5    : %0.4f" % (sum(r_5) / n))
  print("Recall@10   : %0.4f" % (sum(r_10) / n))
  print("```")


def _test():
  uid = "d81c69b2d20e46a7bb133935f11c1f5f"
  code_block_db = get_code_store().fetch_code_block(uid)
  data_results = run_block(code_block_db, search_params=["ast", "contextualTokens", "semantic"], search_limit=1000, index=0, n_code_blocks=1)
  print(data_results)
  # file_path = "CodeSeer/subjects/atcoder/src/main/python/C66/P3/1398083.py"
  # res = semantic_search(file_path, properties.LANGUAGE_JAVA, 1000)
  # print(res)
  # exit()


def _runners(search_limit):
  runner_parallel(search_params=["ast"], save_file_prefix="ast", search_limit=search_limit)
  runner_parallel(search_params=["contextualTokens"], save_file_prefix="contextual", search_limit=search_limit)
  runner_parallel(search_params=["slacc"], save_file_prefix="slacc", search_limit=search_limit)
  # runner_parallel(search_params=["tfidfTokens"], save_file_prefix="tfidf", search_limit=search_limit)
  runner_parallel(search_params=["ast", "contextualTokens"], save_file_prefix="ast_contextual", search_limit=search_limit)
  runner_parallel(search_params=["ast", "contextual", "slacc"], save_file_prefix="ast_contextual_slacc", search_limit=search_limit)
  # runner_parallel(search_params=["ast", "tfidfTokens"], save_file_prefix="ast_tfidf", search_limit=search_limit)


def _analyze():
  args = sys.argv
  if len(args) < 2:
    exit()
  arg = sys.argv[1]
  analyze_search_pkl(arg)


def _main():
  args = sys.argv
  if len(args) < 2:
    exit()
  arg = sys.argv[1]
  search_limit = 1000
  if arg == "ast":
    runner_parallel(search_params=["ast"], save_file_prefix="ast", search_limit=search_limit)
  elif arg == "contextual":
    runner_parallel(search_params=["contextualTokens"], save_file_prefix="contextual", search_limit=search_limit)
  elif arg == "tfidf":
    runner_parallel(search_params=["tfidfTokens"], save_file_prefix="tfidf", search_limit=search_limit)
  elif arg == "tfidf":
    runner_parallel(search_params=["slacc"], save_file_prefix="slacc", search_limit=search_limit)
  elif arg == "ast_contextual":
    runner_parallel(search_params=["ast", "contextualTokens"], save_file_prefix="ast_contextual", search_limit=search_limit)
  elif arg == "ast_tfidf":
    runner_parallel(search_params=["ast", "tfidfTokens"], save_file_prefix="ast_tfidf", search_limit=search_limit)
  elif arg == "ast_contextual_slacc":
    runner_parallel(search_params=["ast", "contextual", "slacc"], save_file_prefix="ast_contextual_slacc", search_limit=search_limit)
  else:
    print("Running all!!!")
    _runners(search_limit)
    # print("Unknown parameter '%s'" % arg)


if __name__ == "__main__":
  # _test()
  # _main()
  _analyze()
  # _runners()
  # runner_parallel(search_params=["ast"], save_file_prefix="ast", search_limit=1000)
  # runner_parallel(search_params=["ast", "tfidfTokens"], save_file_prefix="ast_tfidf", search_limit=1000)
  # print(cache.load_pickle(get_meta_file("ast_tfidf")))
  # runner(search_limit=10)
