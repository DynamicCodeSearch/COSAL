import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import javalang
import re

# MULTI_COMMENT_REGEX = r'(\/\*([\S\s]+?)\*\/)'
MULTI_COMMENT_REGEX = re.compile("/\*.*?\*/", re.DOTALL)
SINGLE_COMMENT_REGEX = re.compile("//.*?\n")


def parse_java(source, wrap_class=False):
  if wrap_class:
    source = "public class TEMP_SLACC_CLASS  { %s }" % source
  return javalang.parse.parse(source)


def get_method_body(source_code):
  start = source_code.find("{")
  end = source_code.rfind("}")
  if start == -1 or end == -1:
    return source_code
  return source_code[start+1:end]


def replace_comments(source):
  source = re.sub(MULTI_COMMENT_REGEX, '', source)
  return re.sub(SINGLE_COMMENT_REGEX, '', source).strip()


def get_main_class_name(source):
  try:
    node = javalang.parse.parse(source)
    if node and node.types:
      for typ in node.types:
        if typ.modifiers and 'public' in typ.modifiers:
          return typ.name
  except Exception:
    pass
  return None
