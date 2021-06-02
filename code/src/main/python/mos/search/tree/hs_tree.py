import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O
from utils import cache

from mos.search.tree.common import Node as N, TYPES, OPERATORS, MODE, LITERAL


class HaskellNode(O):
  def __init__(self, name=None, attrs=[], **updates):
    O.__init__(self, **updates)
    self.is_terminal = False
    self.name = name
    self.type = None
    self.text = None
    self.attrs = []

  @staticmethod
  def from_json(json_map):
    if "type" in json_map and "text" in json_map:
      node = HaskellNode()
      node.is_terminal = True
      node.type = json_map.get("type", None)
      node.text = json_map.get("text", None)
      return node
    else:
      assert len(json_map.keys()) == 1
      name = json_map.keys()[0]
      node = HaskellNode(name=name)
      for val in json_map[name]:
        node.attrs.append(HaskellNode.from_json(val))
      return node

  def get_child_nodes(self, child_key):
    if not self.attrs:
      return []
    child_nodes = []
    for attr in self.attrs:
      if attr.name == child_key:
        child_nodes.append(attr)
      else:
        child_nodes += attr.get_child_nodes(child_key)
    return child_nodes

  def get_text(self):
    text = ""
    if self.text:
      return self.text
    elif self.attrs:
      for node in self.attrs:
        text += node.get_text()
    return text


class HaskellTraveller(object):
  def __init__(self, defaults=None, caller=None):
    self.defaults = set(defaults) if defaults else set()
    self.caller = caller

  def visit(self, node, meta=None):
    node_name = node.name if node.name else "terminal_node"
    if self.caller and node_name in self.defaults:
      return self.caller(node, meta)
    method = 'visit_' + node_name
    default_method = self.generic_visit
    visitor = getattr(self, method, default_method)
    return visitor(node, meta)

  def visit_terminal_node(self, node, meta=None):
    print(node.text)
    return node.text

  def generic_visit(self, node, meta=None):
    for attr in node.attrs:
      if isinstance(attr, HaskellNode):
        self.visit(attr, meta)
    return None


class TreeVisitor(HaskellTraveller):
  def __init__(self, tree):
    HaskellTraveller.__init__(self)
    self.tree = tree
    self.vertex = None

  def parse(self):
    if self.tree:
      self.vertex = self.visit(self.tree, None)
    return self.vertex

  def visit_decl_no_th(self, node, meta=None):
    def is_simple_function():
      return len(node.attrs) >= 2 and node.attrs[0].name == "infixexp" and node.attrs[-1].name == "rhs"
    if is_simple_function():
      func = N(TYPES.FUNCTION_DEF)
      fexps = node.get_child_nodes("fexp")
      if not fexps:
        raise RuntimeError("Invalid format for function exp")
      aexps = fexps[0].get_child_nodes("aexp")
      assert len(aexps) >= 1
      args = N(TYPES.ARGS)
      for _ in aexps[1:]:
        args.add_kid(N(TYPES.VARIABLE))
      func.add_kid(args)
      # TODO: handle simple function
      rhses = node.get_child_nodes("rhs")
      if rhses:
        body_node = self.visit(rhses[0], meta=None)
        func.add_kid(body_node)
      return func
    else:
      raise RuntimeError("Complex functions not handled yet!")

  def visit_rhs(self, node, meta=None):
    if not node.attrs:
      return None
    if node.attrs[0].get_text() == "=":
      print(node.attrs[1].get_text())
      print("Coming soon!")
    exit()
    # print(node.name)
    # print(node.attrs[0].name)
    # print(node.attrs[-1].name)



def test():
  json_data = cache.load_json("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/mos/search/tree/hs_tree.json")
  node = HaskellNode.from_json(json_data)
  visitor = TreeVisitor(node)
  print(visitor.parse())


if __name__ == "__main__":
  test()
