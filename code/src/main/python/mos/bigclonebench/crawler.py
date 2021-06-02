
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.bigclonebench.bcb_code_block import  BCBCodeBlock
from mos.search.tree import java_tree
from mos.helpers import contexter
from mos.search_store import code_store
from utils import cache, logger
import properties

import re

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
META_REGEX = re.compile("{split}([0-9]+){split}([a-zA-Z0-9_\-]+){split}([a-zA-Z0-9_\-]+)\.java".format(split=os.path.sep))
INVALID_SUBMISSION_TYPES = {"sample"}
# INVALID_SUBMISSION_TYPES = {"sample", "selected"}


def get_data_store():
  return code_store.CodeStore()


def get_project_meta_from_file_path(file_path):
  meta_str = file_path.split(properties.CONFIG.get_projects_home())[-1]
  matches = re.search(META_REGEX, meta_str)
  if matches:
    return {
      "problem_id": matches.group(1),
      "submission_type": matches.group(2),
      "submission_id": matches.group(3)
    }
  return None


def count_file_lines(file_path):
  return sum(1 for line in open(file_path))


def load_java_meta():
  files = cache.list_files(properties.CONFIG.get_projects_home(), check_nest=True, is_absolute=True, extension=".java")
  total_methods = 0
  n_files = 0
  total_lines = 0
  for i, file_path in enumerate(files):
    n_lines = count_file_lines(file_path)
    n_files += 1
    contents = cache.read_file(file_path)
    try:
      visitor = java_tree.MethodVisitor(contents)
      method_count = visitor.parse()
    except Exception:
      continue
    contents.split("\n")
    total_methods += method_count
    total_lines += n_lines
    if i % 10 == 0:
      print(i, method_count, n_lines)
  print("Total: %d", n_files)
  print("Methods: %d", total_methods)
  print("Lines: %d", total_lines)


def load_java_files(from_db=False, clear_db=False):
  store = get_data_store()
  if from_db:
    LOGGER.info("Loading from DB .... ")
    code_blocks = []
    i = 0
    for cb in store.get_code_blocks(language=properties.LANGUAGE_JAVA):
      if i % 100 == 0:
        LOGGER.info("Processing %d ... " % (i + 1))
      code_blocks.append(BCBCodeBlock.from_bson(cb))
      i += 1
    return code_blocks
  else:
    LOGGER.info("Loading from File System .... ")
    files = cache.list_files(properties.CONFIG.get_projects_home(), check_nest=True, is_absolute=True, extension=".java")
    code_blocks = []
    n = len(files)
    if clear_db:
      store.drop_code_blocks()
    for i, file_path in enumerate(files):
      if i % 100 == 0:
        LOGGER.info("Processing %d/%d ... " % (i + 1, n))
      project_meta = get_project_meta_from_file_path(file_path)
      uid = "P%s-S%s" % (project_meta["problem_id"], project_meta["submission_id"])
      if not project_meta or project_meta["submission_type"] in INVALID_SUBMISSION_TYPES:
        continue
      if store.is_code_block_exists(uid):
        # if i % 100 == 0:
        #   LOGGER.info("Submission '%s' (%d/%d) exists. Moving on ... " % (uid, i + 1, n))
        continue
      code_block = BCBCodeBlock()
      code_block.uid = uid
      code_block.problem_id = project_meta["problem_id"]
      code_block.submission_type = project_meta["submission_type"]
      code_block.submission_id = project_meta["submission_id"]
      code_block.source_file = file_path
      # code_block.code = cache.read_file(file_path, mode='rb').decode('utf-8', errors='replace').strip()
      code_block.code = cache.read_file(file_path, mode='rb').decode('utf-8', errors='replace')
      try:
        code_block.ast = java_tree.get_java_tree(code_block.code, wrap_class=False)
      except Exception as e:
        continue
      code_block.contextual_tokens = contexter.tokenize_java_function(code_block.code)
      try:
        code_block.contextual_tokens = contexter.tokenize_java_function(code_block.code)
      except Exception as e:
        continue
      # try:
      #   code_block.contextual_tokens = contexter.tokenize_java_function(code_block.code)
      # except Exception:
      #   code_block.contextual_tokens = None
      code_blocks.append(code_block)
      store.save_code_block(code_block)
      # try:
      #   store.save_code_block(code_block)
      # except Exception as e:
      #   LOGGER.error(e.message)
  return code_blocks


def parse_java_file(file_path):
  contents = cache.read_file(file_path)
  visitor = java_tree.TreeVisitor(contents, wrap_class=False)
  vertex = visitor.parse()
  parsed = vertex.to_bson()
  return parsed


def _test_file_stat():
  load_java_meta()


def _test():
  # file_path = os.path.join(properties.CONFIG.get_projects_home(), "2", "default", "101.java")
  # parse_java_file(file_path)
  print(len(load_java_files(from_db=True, clear_db=False)))


if __name__ == "__main__":
  _test_file_stat()
