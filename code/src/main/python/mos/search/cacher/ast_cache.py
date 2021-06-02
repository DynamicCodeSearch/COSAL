import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.tree import distances
from mos.search_store.code_store import CodeStore, ASTDistanceStore, MetaStore
from mos.blocks import code_block, ast_distance_node
from utils import logger
import properties

from joblib import Parallel, delayed
import time
import random


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_code_store():
  return CodeStore()


def get_ast_distance_store():
  return ASTDistanceStore()


def is_code_block_too_big(cb):
  lang = cb["language"]
  size = cb["contestMeta"]["codeSize"]
  return (lang == properties.LANGUAGE_PYTHON and size > 613) or \
         (lang == properties.LANGUAGE_JAVA and size > 3082.3)


def group_by_problems(code_blocks):
  groups = {}
  for cb in code_blocks:
    if cb is None:
      continue
    key = cb.contest_meta.make_key()
    if key in groups:
      groups[key].append(cb)
    else:
      groups[key] = [cb]
  return groups


def get_competitive_group(code_blocks, key, only_negatives=False):
  positive_blocks = code_blocks[key]
  negative_blocks = []
  for k, block in code_blocks.items():
    if k == key:
      continue
    negative_blocks += block
  sample_size = min(max(10, 2*len(positive_blocks)), len(negative_blocks))
  negative_blocks = random.sample(negative_blocks, sample_size)
  if only_negatives:
    return negative_blocks
  return positive_blocks + negative_blocks


def compute_ast_distance_node(one, two, index, total, lang):
  if index % 200 == 0:
    LOGGER.info("#### Processed %d/%d %s nodes" % (index, total, lang))
  node = ast_distance_node.ASTDistanceNode()
  node.uid1 = one.uid
  node.uid2 = two.uid
  node.distance = distances.apted_distance(one.ast, two.ast)
  return node


def compute_distances(force=False):
  meta_store = MetaStore()
  start = time.time()
  py_blocks = []
  # test_limit = 100
  test_limit = None
  for py_block_db in get_code_store().get_code_blocks(language=properties.LANGUAGE_PYTHON, limit=test_limit):
    if py_block_db.get('ast', None) and not is_code_block_too_big(py_block_db):
      py_block = code_block.CodeBlock.from_bson(py_block_db)
      if py_block.ast:
        py_blocks.append(py_block)
  LOGGER.info("Time for fetching '%d' python documents: %0.4f" % (len(py_blocks), time.time()-start))
  java_blocks = []
  for java_block_db in get_code_store().get_code_blocks(language=properties.LANGUAGE_JAVA, limit=test_limit):
    if not java_block_db.get('ast', None) and is_code_block_too_big(java_block_db):
      continue
    java_block = code_block.CodeBlock.from_bson(java_block_db)
    if java_block.ast:
      java_blocks.append(java_block)
  LOGGER.info("Time for fetching '%d' java documents: %0.4f" % (len(java_blocks), time.time()-start))
  py_groups = group_by_problems(py_blocks)
  java_groups = group_by_problems(java_blocks)
  for g, (key, py_group) in enumerate(py_groups.items()):
    if not force and meta_store.is_project_ast_cached(key):
      LOGGER.info("## Processed Py group %d / %d with key '%s' ... " % (g + 1, len(py_groups), key))
      continue
    LOGGER.info("## Processing Py group %d / %d" % (g + 1, len(py_groups)))
    competitive_group = get_competitive_group(java_groups, key)
    for p, py_block in enumerate(py_group):
      computed = get_ast_distance_store().get_computed_uids(py_block.uid)
      if len(computed) >= len(competitive_group):
        # LOGGER.info("### Already processed for py node with UID: '%s'. Moving on ..." % py_block.uid)
        continue
      LOGGER.info("### Computing for py-node %d/%d. Group %d/%d .... " % (p + 1, len(py_group), g + 1, len(py_groups)))
      unprocessed_java_blocks = []
      for j, java_block in enumerate(competitive_group):
        if java_block.uid in computed:
          continue
        unprocessed_java_blocks.append((java_block, j, len(competitive_group)))
      if not unprocessed_java_blocks:
        continue
      ast_distance_nodes = Parallel(n_jobs=-1)(delayed(compute_ast_distance_node)(py_block, java_block, index, total, java_block.language)
                                               for java_block, index, total in unprocessed_java_blocks)
      LOGGER.info("Writing to DB")
      get_ast_distance_store().save_ast_distances(ast_distance_nodes)
    LOGGER.info("Updating Meta-store with project_id '%s'" % key)
    meta_store.update_ast_cache_project(key)


def compute_within_language_distances(language, force=False):
  meta_store = MetaStore()
  start = time.time()
  lang_blocks = []
  test_limit = None
  LOGGER.info("Loading code blocks ... ")
  index = 0
  n_cb = get_code_store().count_code_blocks(language=language)
  for lang_block_db in get_code_store().get_code_blocks(language=language, limit=test_limit):
    if index % 1000 == 0:
      LOGGER.info("Fetching codeblock %d/%d ... " % (index + 1, n_cb))
    if lang_block_db.get('ast', None):
      lang_block = code_block.CodeBlock.from_bson(lang_block_db)
      if lang_block.ast:
        lang_blocks.append(lang_block)
    index += 1
  LOGGER.info("Time for fetching %d '%s' documents: %0.4f" % (len(lang_blocks), language, time.time()-start))
  lang_groups = group_by_problems(lang_blocks)
  for g, (key, lang_group) in enumerate(lang_groups.items()):
    if not force and meta_store.is_project_ast_cached(key, language=language):
      LOGGER.info("## Already processed '%s' group %d / %d with key '%s'." % (language, g + 1, len(lang_groups), key))
      continue
    LOGGER.info("## Processing '%s' group %d / %d with key '%s' ... " % (language, g + 1, len(lang_groups), key))
    negative_group = get_competitive_group(lang_groups, key, only_negatives=True)
    group_size = len(lang_group)
    for i in range(group_size - 1):
      lang_block = lang_group[i]
      positive_blocks = lang_group[i+1: group_size]
      competitive_group = positive_blocks + negative_group
      computed = get_ast_distance_store().get_computed_uids(lang_block.uid, language=language)
      if len(computed) >= len(competitive_group):
        # LOGGER.info("### Already processed for py node with UID: '%s'. Moving on ..." % py_block.uid)
        continue
      LOGGER.info("### Computing for %s-node %d/%d. Group %d/%d .... " %
                  (language, i + 1, group_size, g + 1, len(lang_groups)))
      unprocessed_blocks = []
      for j, comp_block in enumerate(competitive_group):
        if comp_block.uid in computed:
          continue
        unprocessed_blocks.append((comp_block, j, len(competitive_group)))
      if not unprocessed_blocks:
        continue
      ast_distance_nodes = Parallel(n_jobs=-1)(delayed(compute_ast_distance_node)(lang_block, comp_block, index, total, language)
                                               for comp_block, index, total in unprocessed_blocks)
      LOGGER.info("Writing to DB")
      get_ast_distance_store().save_ast_distances(ast_distance_nodes, language=language)
    LOGGER.info("Updating Meta-store with project_id '%s'" % key)
    meta_store.update_ast_cache_project(key, language=language)


def save_computed_projects():
  meta_store = MetaStore()
  start = time.time()
  py_blocks = []
  # test_limit = 100
  test_limit = None
  for py_block_db in get_code_store().get_code_blocks(language=properties.LANGUAGE_PYTHON, limit=test_limit):
    if py_block_db.get('ast', None) and not is_code_block_too_big(py_block_db):
      py_block = code_block.CodeBlock.from_bson(py_block_db)
      if py_block.ast:
        py_blocks.append(py_block)
  LOGGER.info("Time for fetching '%d' python documents: %0.4f" % (len(py_blocks), time.time()-start))
  java_blocks = []
  for java_block_db in get_code_store().get_code_blocks(language=properties.LANGUAGE_JAVA, limit=test_limit):
    if not java_block_db.get('ast', None) and is_code_block_too_big(java_block_db):
      continue
    java_block = code_block.CodeBlock.from_bson(java_block_db)
    if java_block.ast:
      java_blocks.append(java_block)
  LOGGER.info("Time for fetching '%d' java documents: %0.4f" % (len(java_blocks), time.time()-start))
  py_groups = group_by_problems(py_blocks)
  java_groups = group_by_problems(java_blocks)
  for g, (key, py_group) in enumerate(py_groups.items()):
    LOGGER.info("## Processing Py group %d / %d" % (g + 1, len(py_groups)))
    competitive_group = get_competitive_group(java_groups, key)
    for p, py_block in enumerate(py_group):
      computed = get_ast_distance_store().get_computed_uids(py_block.uid)
      if len(computed) < len(competitive_group):
        LOGGER.info("### Found the threshold. Stopping now")
        return
    meta_store.update_ast_cache_project(key)


def _test():
  store = CodeStore()
  recs = store.get_code_blocks(fields=["language", "contestMeta.codeSize"])
  records = []
  javas, pys = [], []
  for rec in recs:
    if rec["language"] == properties.LANGUAGE_JAVA:
      javas.append(rec["contestMeta"]["codeSize"])
    elif rec["language"] == properties.LANGUAGE_PYTHON:
      pys.append(rec["contestMeta"]["codeSize"])
  import numpy as np
  print(np.percentile(javas, [1, 10, 25, 50, 75, 90, 99]))
  print(np.percentile(pys, [1, 10, 25, 50, 75, 90, 99]))
  # print(records)


if __name__ == "__main__":
  # _test()
  # compute_distances()
  compute_within_language_distances(properties.LANGUAGE_JAVA)
  # save_computed_projects()
