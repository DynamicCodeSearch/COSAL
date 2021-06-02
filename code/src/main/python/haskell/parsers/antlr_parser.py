import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from antlr4 import *
from haskell.parsers.antlr.HaskellParser import HaskellParser
from haskell.parsers.antlr.HaskellLexer import HaskellLexer
from haskell.parsers.antlr.HaskellParserListener import HaskellParserListener


txt = """
in_range min max x = x >= min && x <= max
"""

def test():
  lexer = HaskellLexer(txt)
  stream = CommonTokenStream(lexer)
  parser = HaskellParser(stream)
  tree = parser.module()
  print(tree.toStringTree(parser))


if __name__ == "__main__":
  test()
