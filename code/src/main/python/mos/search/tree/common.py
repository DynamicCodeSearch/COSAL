import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from anytree import Node as DotNode
from anytree.exporter import DotExporter
import zss
import networkx as nx

from utils.lib import O, pprint


class TYPES:
  ROOT = "root"
  FUNCTION_DEF = "function_def"
  ARGS = "args"
  ARG = "arg"
  BODY = "body"
  STATEMENT = "stmt"
  LOOP = "loop"
  CONDITIONAL = "cond"
  OPERATOR = "operator"
  ASSERT = "assert"
  ASSIGN = "assign"
  AUG_ASSIGN = "aug_assign"
  BREAK = "break"
  CONTINUE = "continue"
  CLASS_DEF = "class_def"
  DELETE = "delete"
  EXEC = "exec"
  LOOP_CONDITION = "condition"
  IF = "if"
  IF_CONDITION = "condition"
  ELSE = "else"
  IMPORT = "import"
  PASS = "pass"
  FUNCTION_CALL = "call"
  RAISE = "raise"
  RETURN = "return"
  TRY = "try"
  EXCEPT = "except"
  FINALLY = "finally"
  WITH = "with"
  ATTRIBUTE = "attribute"
  VARIABLE = "var"
  OPERATOR_EXPR = "op_expr"  # Can contain Binary and Unary operator
  ARRAY_ACCESS = "array_access"
  INDEX = "index"
  LITERAL = "literal"
  YIELD = "yield"
  SYNCHRONIZED = "sync"

  def __init__(self): pass


class OPERATORS:
  """"""
  """
  Bit
  """
  BIT_AND = "bit_and"
  BIT_OR = "bit_or"
  BIT_XOR = "bit_xor"
  LSHIFT = "lshift"
  RSHIFT = "rshift"
  RSHIFT0 = "rshift0"
  INVERT = "invert"  # ~ operator
  """
  Math
  """
  ADD = "add"
  DIV = "div"
  FLOOR_DIV = "floor_div"
  MOD = "mod"
  MULT = "mult"
  POW = "pow"
  SUB = "sub"
  INC = "inc"
  DEC = "dec"
  """
  LOGIC
  """
  AND = "and"
  OR = "or"
  NOT = "not"
  """
  Comparison
  """
  EQ = "eq"
  GT = "gt"
  GTE = "gte"
  IN = "in"
  IS = "is"
  IS_NOT = "is_not"
  LT = "lt"
  LTE = "lte"
  NOT_EQ = "not_eq"
  NOT_IN = "not_in"
  """
  Instance
  """
  INSTANCE_OF = "instance_of"

  def __init__(self): pass


class MODE:
  LOAD = "load"
  STORE = "store"
  DELETE = "delete"

  def __init__(self): pass


class LITERAL:
  STRING = "string"
  NUMERIC = "numeric"
  BOOLEAN = "boolean"
  NULL = "none"

  def __init__(self): pass


def flatten(x):
  if isinstance(x, (list, tuple, set)):
    for sub in x:
      for s in flatten(sub):
        yield s
  else:
    yield x


class Node(O):
  def __init__(self, node_type, value=None, mode=None, parent=None, **kwargs):
    self.type = node_type
    self.value = value
    self._mode = mode
    self.zkids = []
    O.__init__(self, **kwargs)
    if parent:
      parent.add_kid(self)

  def __repr__(self):
    """
    Represent as string
    :return:
    """
    return pprint(self, do_print=False, skip_None=True, skip_class=True)

  def to_dot_node(self):
    children = None
    if self.zkids:
      children = []
      for kid in self.zkids:
        children.append(kid.to_dot_node())
    return DotNode(id(self), children=children, display_name=self.to_display_name())

  def to_display_name(self):
    if self.type == "return":
      return self.type[:3]
    return self.type[:4]
    # params = []
    # if self.value: params.append("value=%s" % self.value)
    # if self._mode: params.append("mode=%s" % self._mode)
    # param_str = "(%s)" % ", ".join(params) if len(params) > 0 else ""
    # return "%s%s" % (self.type, param_str)

  def add_kid(self, kid):
    if kid:
      for k in flatten(kid):
        self.zkids.append(k)

  def prepend_kid(self, kid):
    if kid:
      for k in flatten(kid):
        self.zkids.insert(0, k)

  # For rendering

  def to_png(self, img_path):
    DotExporter(self.to_dot_node(), nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name))\
      .to_picture(img_path)

  # For networkx
  def to_networkx(self, graph=None):
    if not graph:
      graph = nx.Graph()
    graph.add_node(id(self), label=Node.get_zss_label(self))
    if self.zkids:
      # source = {"id": id(self), "label": Node.get_zss_label(self)}
      # source = (id(self), Node.get_zss_label(self))
      for kid in self.zkids:
        # target = {"id": id(kid), "label": Node.get_zss_label(kid)}
        kid.to_networkx(graph)
        graph.add_edge(id(self), id(kid))
    return graph

  @staticmethod
  def graph_edit_distance(node_a, node_b):
    g_a = node_a.to_networkx()
    g_b = node_b.to_networkx()
    return nx.graph_edit_distance(g_a, g_b, node_match=graph_eq)

  # # Zhang-Shasha Distance
  #
  # @staticmethod
  # def simple_label_comparison(a, b):
  #   return 0 if a == b else 1
  #
  # @staticmethod
  # def get_zss_label(node):
  #   return node.type
  #
  # @staticmethod
  # def get_zss_kids(node):
  #   return node.zkids
  #
  # @staticmethod
  # def zhang_shasha_distance(node_a, node_b):
  #   return zss.simple_distance(node_a, node_b, Node.get_zss_kids, Node.get_zss_label, Node.simple_label_comparison)

  def to_bson(self):
    bson = {"type": self.type}
    if self.value:
      bson["value"] = self.value
    if self._mode:
      bson["mode"] = self._mode
    if self.zkids:
      bson["kids"] = [kid.to_bson() for kid in self.zkids]
    return bson

  @staticmethod
  def from_bson(node_bson):
    if not node_bson:
      return None
    node = Node(node_bson["type"])
    node.value = node_bson.get("value", None)
    node._mode = node_bson.get("mode", None)
    if "kids" in node_bson:
      for kid_bson in node_bson["kids"]:
        node.zkids.append(Node.from_bson(kid_bson))
    return node


def graph_eq(a, b):
  return a['label'] == b['label']