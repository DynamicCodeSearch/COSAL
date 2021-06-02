import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from mos.helpers import contexter
from mos.search_store.code_store import CodeStore
from utils import cache, logger
from sklearn.feature_extraction.text import TfidfVectorizer
import properties

import nltk
import numpy as np
from matplotlib import pyplot as plt


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))

TFIDF_TOP_WORDS_PKL = os.path.join(properties.CONFIG.CODE_HOME, "resources", "tfidf", "%s.pkl"
                                   % properties.CONFIG.get_dataset())
N_TOP_WORDS = 300  # Arrived at by plotting TFIDF scores for each word

_TOP_TFIDF_TOKENS = None


def get_code_store():
  return CodeStore()


def compute_tfidf(docs):
  tfidf = TfidfVectorizer(stop_words='english')
  tfidf_result = tfidf.fit_transform(docs)
  scores = zip(tfidf.get_feature_names(), np.asarray(tfidf_result.sum(axis=0)).ravel())
  sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
  words, scores = [], []
  for k, score in sorted_scores:
    words.append(k)
    scores.append(score)
  # for item in sorted_scores:
  #   print("{0:50} Score: {1}".format(item[0], item[1]))
  return words, scores


def load_top_tfidf_tokens():
  global _TOP_TFIDF_TOKENS
  if _TOP_TFIDF_TOKENS is None:
    if cache.file_exists(TFIDF_TOP_WORDS_PKL):
      return set(cache.load_pickle(TFIDF_TOP_WORDS_PKL))
    _TOP_TFIDF_TOKENS = save_top_tfidf_tokens()
  return _TOP_TFIDF_TOKENS


def save_top_tfidf_tokens():
  docs = []
  n_code_blocks = get_code_store().count_code_blocks(language=None)
  index = 0
  for code_block_db in get_code_store().get_code_blocks(fields=["contextualTokens"]):
    index += 1
    if index % 1000 == 0:
      LOGGER.info("Processing document %d/%d ... " % (index, n_code_blocks))
    tokens = code_block_db["contextualTokens"]
    # tokens = []
    # for word in nltk.word_tokenize(source_code):
    #   tokens += contexter.get_tokens(word, lang)
    if tokens:
      docs.append(" ".join(tokens))
  LOGGER.info("Computing TFIDF .... ")
  tokens, scores = compute_tfidf(docs)
  cache.save_pickle(TFIDF_TOP_WORDS_PKL, tokens[:N_TOP_WORDS])
  return set(tokens)


def process():
  java_docs, py_docs = [], []
  index = 0
  n_code_blocks = get_code_store().count_code_blocks(language=None)
  index = 0
  for code_block_db in get_code_store().get_code_blocks():
    index += 1
    if index % 100 == 0:
      LOGGER.info("Processing document %d/%d ... " % (index, n_code_blocks))
    uid = code_block_db["uid"]
    source_code = code_block_db["code"]
    lang = code_block_db["language"]
    tokens = []
    for word in nltk.word_tokenize(source_code):
      tokens += contexter.get_tokens(word, lang)
    tokens = " ".join(tokens)
    if lang == properties.LANGUAGE_PYTHON:
      py_docs.append(tokens)
    elif lang == properties.LANGUAGE_JAVA:
      java_docs.append(tokens)
  LOGGER.info("Computing TFIDF for java .... ")
  _, java_scores = compute_tfidf(java_docs)
  plt.semilogy(range(0, len(java_scores)), java_scores)
  LOGGER.info("Computing TFIDF for python .... ")
  _, py_scores = compute_tfidf(py_docs)
  plt.semilogy(range(0, len(py_scores)), py_scores)
  LOGGER.info("Computing TFIDF for java + python .... ")
  _, all_scores = compute_tfidf(java_docs + py_docs)
  plt.semilogy(range(0, len(all_scores)), all_scores)
  plt.legend(['java', 'py', 'java+py'], loc='upper right')
  base_folder = os.path.join(properties.CONFIG.CODE_HOME, "_rough", "tfidf")
  cache.mkdir(base_folder)
  plt.savefig(os.path.join(base_folder, "%s.png" % properties.CONFIG.get_dataset()))


if __name__ == "__main__":
  save_top_tfidf_tokens()
  # process()
  # print(load_top_tfidf_tokens())
