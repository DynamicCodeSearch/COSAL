import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


import zss
import networkx as nx
from apted import APTED, Config


def get_kids(node):
  return node.zkids


def get_label(node):
  return node.type


def simple_comparison(a, b):
  return 0 if a == b else 1


def zhang_shasha_distance(node_a, node_b):
  return zss.simple_distance(node_a, node_b, get_kids, get_label, simple_comparison)


class AptedNodeConfig(Config):
  def children(self, node):
    if node.zkids:
      return node.zkids
    return []

  def rename(self, a, b):
    return 0 if get_label(a) == get_label(b) else 1


def apted_distance(a, b):
  apted = APTED(a, b, AptedNodeConfig())
  return apted.compute_edit_distance()
