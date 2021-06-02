import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.tree import common


class TYPES(common.TYPES):
  def __init__(self):
    common.TYPES.__init__(self)


class OPERATORS(common.OPERATORS):
  def __init__(self):
    common.OPERATORS.__init__(self)

