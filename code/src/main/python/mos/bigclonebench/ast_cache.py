import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.bigclonebench.bcb_code_block import BCBCodeBlock
from mos.blocks.ast_distance_node import ASTDistanceNode
from mos.search_store.code_store import CodeStore, ASTDistanceStore, MetaStore
from mos.search.tree import distances
from utils import logger, cache
import properties

from joblib import Parallel, delayed
import time
import random


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
MAX_POSITIVE_BLOCK_SIZE = 10


def get_code_store():
  return CodeStore()


def get_ast_distance_store():
  return ASTDistanceStore()


def group_by_problems(code_blocks):
  groups = {}
  for cb in code_blocks:
    if cb is None:
      continue
    key = cb.problem_id
    if key in groups:
      groups[key].append(cb)
    else:
      groups[key] = [cb]
  return groups


def get_competitive_group(code_groups, key, uid, only_negatives=False):
  assert uid is not None
  positive_blocks = filter(lambda cb: cb.uid != uid, code_groups[key])
  if len(positive_blocks) > MAX_POSITIVE_BLOCK_SIZE:
    positive_blocks = random.sample(positive_blocks, MAX_POSITIVE_BLOCK_SIZE)
  negative_blocks = []
  for k, block in code_groups.items():
    if k == key:
      continue
    negative_blocks += block
  sample_size = min(max(10, 3*len(positive_blocks)), len(negative_blocks))
  negative_blocks = random.sample(negative_blocks, sample_size)
  if only_negatives:
    return negative_blocks
  return positive_blocks + negative_blocks


def compute_ast_distance_node(one, two, index, total):
  if index % MAX_POSITIVE_BLOCK_SIZE == 0:
    LOGGER.info("#### Processed %d/%d nodes" % (index, total))
  node = ASTDistanceNode()
  node.uid1 = one.uid
  node.uid2 = two.uid
  node.distance = distances.apted_distance(one.ast, two.ast)
  return node


def make_code_block_parallel(code_block_db, index, total):
  if index % 200 == 0:
    LOGGER.info("#### Processed %d/%d nodes" % (index, total))
  code_block = BCBCodeBlock.from_bson(code_block_db)
  return code_block


def compute_distances(force=False):
  language = properties.LANGUAGE_JAVA
  meta_store = MetaStore()
  start = time.time()
  code_blocks = []
  # test_limit = 1000
  test_limit = None
  index = 0
  n_cb = get_code_store().count_code_blocks()
  code_block_dbs = []
  for code_block_db in get_code_store().get_code_blocks(fields=["uid", "ast", "submissionId", "problemId"], limit=test_limit):
    if index % 1000 == 0:
      LOGGER.info("Fetching codeblock %d/%d ... " % (index + 1, n_cb))
    index += 1
    if code_block_db.get('ast', None):
      code_block_dbs.append(code_block_db)
      # code_block = BCBCodeBlock.from_bson(code_block_db)
      # if code_block.ast:
      #   code_blocks.append(code_block)
  code_blocks = Parallel(n_jobs=-1)(delayed(make_code_block_parallel)(cb_db, index, len(code_block_dbs)) for index, cb_db in enumerate(code_block_dbs))
  code_blocks = filter(lambda cb: cb.ast is not None, code_blocks)
  LOGGER.info("Time for fetching '%d' documents: %0.4f" % (len(code_blocks), time.time()-start))
  code_groups = group_by_problems(code_blocks)
  for g, (key, code_group) in enumerate(code_groups.items()):
    if not force and meta_store.is_project_ast_cached(key, language=language):
      LOGGER.info("## Already processed group %d / %d with key '%s'." % (g + 1, len(code_groups), key))
      continue
    LOGGER.info("## Processing group %d / %d with key '%s' ... " % (g + 1, len(code_groups), key))
    group_size = len(code_group)
    for i in range(group_size - 1):
      code_block = code_group[i]
      competitive_group = get_competitive_group(code_groups, key, code_block.uid, only_negatives=False)
      computed = get_ast_distance_store().get_computed_uids(code_block.uid, language=language)
      if len(computed) >= len(competitive_group):
        continue
      LOGGER.info("### Computing for node %d/%d. Group %d/%d .... " %
                  (i + 1, group_size, g + 1, len(code_groups)))
      unprocessed_blocks = []
      for j, comp_block in enumerate(competitive_group):
        if comp_block.uid in computed:
          continue
        unprocessed_blocks.append((comp_block, j, len(competitive_group)))
      if not unprocessed_blocks:
        continue
      ast_distance_nodes = Parallel(n_jobs=-1)(delayed(compute_ast_distance_node)(code_block, comp_block, index, total)
                                               for comp_block, index, total in unprocessed_blocks)
      LOGGER.info("Writing to DB")
      get_ast_distance_store().save_ast_distances(ast_distance_nodes, language=language)
    LOGGER.info("Updating meta-store with project_id '%s'" % key)
    meta_store.update_ast_cache_project(key, language=language)


if __name__ == "__main__":
  compute_distances(force=False)
