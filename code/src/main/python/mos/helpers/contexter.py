
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import ast_utils
from utils import cache
import properties

import javalang
import re
import io
import tokenize
import nltk


__STOPWORDS = None
STRING_REGEX = re.compile("^[a-zA-Z][a-zA-Z0-9]+$")


"""
Python
"""


def get_stopwords():
  global __STOPWORDS
  if __STOPWORDS is None:
    sw_path = os.path.join(properties.CONFIG.CODE_HOME, "src", "main", "resources", "stopwords_english.txt")
    __STOPWORDS = set(cache.read_file(sw_path).strip().split("\n"))
  return __STOPWORDS


def is_legit_token(token):
  tl = token.lower().strip()
  return (len(tl) >= properties.MIN_CONTEXT_TOKEN_SIZE) and STRING_REGEX.match(tl) \
      and (token not in ast_utils.get_keywords()) and (tl not in get_stopwords())


def split_on_non_letters(token):
  return re.split('[^a-zA-Z0-9]+', token)


def split_on_camel_case(token):
  matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', token)
  return [m.group(0) for m in matches]


def tokenize_string(token):
  if len(token) > 1 and token[0] == token[-1] and token[0] in ['"', '\'']:
    token = token[1:-1]
  tokenized = set()
  splits = re.split('\s+', token)
  for split in splits:
    if is_legit_token(split):
      tokenized.add(split.lower().strip())
    underscore_replaced = split.replace("_", "")
    if is_legit_token(underscore_replaced):
      tokenized.add(underscore_replaced.lower().strip())
    letter_splits = split_on_non_letters(split)
    for letter_split in letter_splits:
      if is_legit_token(letter_split):
        tokenized.add(letter_split.lower().strip())
      camel_case_splits = split_on_camel_case(letter_split)
      for camel_case_split in camel_case_splits:
        if is_legit_token(camel_case_split):
          tokenized.add(camel_case_split.lower().strip())
  return tokenized


def tokenize_func_body(func_body):
  token_generator = tokenize.generate_tokens(io.StringIO(func_body).readline)
  tokens = set()
  try:
    for token_num, token, start, end, line in token_generator:
      legit_tokens = tokenize_string(token)
      if legit_tokens:
        tokens = tokens.union(legit_tokens)
    return tokens
  except IndentationError:
    return tokens


def tokenize_py_function(code):
  ast_node = ast_utils.parse(code, use_ast_tokens=True)
  comments = None
  if ast_node:
    comments = ast_utils.get_comments(code)
    doc_string = ast_utils.get_docstring(ast_node)
    if doc_string:
      comments.append(doc_string)
  code = ast_utils.remove_comments_and_docstrings(code)
  tokens = tokenize_func_body(code)
  if comments and len(comments) > 0:
    for comment in comments:
      tokens = tokens.union(tokenize_string(comment))
  return tokens


"""
Java
"""

_KEYWORDS = None


def get_java_keywords():
  global _KEYWORDS
  if _KEYWORDS is None:
    _KEYWORDS = javalang.tokenizer.Keyword.VALUES.union({"null", "true", "false"})
  return _KEYWORDS


def is_legit_java_token(token):
  tl = token.lower().strip()
  return (len(tl) >= properties.MIN_CONTEXT_TOKEN_SIZE) and STRING_REGEX.match(tl) \
      and (token not in get_java_keywords()) and (tl not in get_stopwords())


def tokenize_java_string(token):
  if len(token) > 1 and token[0] == token[-1] and token[0] in ['"', '\'']:
    token = token[1:-1]
  tokenized = set()
  splits = re.split('\s+', token)
  for split in splits:
    if is_legit_java_token(split):
      tokenized.add(split.lower().strip())
    underscore_replaced = split.replace("_", "")
    if is_legit_java_token(underscore_replaced):
      tokenized.add(underscore_replaced.lower().strip())
    letter_splits = split_on_non_letters(split)
    for letter_split in letter_splits:
      if is_legit_java_token(letter_split):
        tokenized.add(letter_split.lower().strip())
      camel_case_splits = split_on_camel_case(letter_split)
      for camel_case_split in camel_case_splits:
        if is_legit_java_token(camel_case_split):
          tokenized.add(camel_case_split.lower().strip())
  return tokenized


def tokenize_java_function(func_body):
  tokens = set()
  for token in nltk.word_tokenize(func_body):
    legit_tokens = tokenize_java_string(token)
    if legit_tokens:
      tokens = tokens.union(legit_tokens)
  return tokens


def get_tokens(token, lang):
  if len(token) > 1 and token[0] == token[-1] and token[0] in ['"', '\'']:
    token = token[1:-1]
  tokenized = []
  is_valid = is_legit_token if lang == properties.LANGUAGE_PYTHON else is_legit_java_token
  splits = re.split('\s+', token)
  for split in splits:
    letter_splits = split_on_non_letters(split)
    for letter_split in letter_splits:
      camel_case_splits = split_on_camel_case(letter_split)
      if is_valid(letter_split):
        tokenized.append(letter_split.lower().strip())
      if len(camel_case_splits) > 1:
        for camel_case_split in camel_case_splits:
          if is_valid(camel_case_split):
            tokenized.append(camel_case_split.lower().strip())
  cleaned_token = token.replace("_", "").lower().strip()
  if cleaned_token != token and is_valid(cleaned_token):
    tokenized.append(cleaned_token)
  return tokenized
