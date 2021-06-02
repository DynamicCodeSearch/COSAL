import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.search.tree import java_tree, py_tree
from utils import cache, logger
import properties

from mos.search.tree.common import Node as N
from mos.search.tree.distances import apted_distance
from anytree import Node as DN
from anytree.exporter import DotExporter


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_tree(code, language, is_function=False):
  if language == properties.LANGUAGE_PYTHON:
    return py_tree.get_py_tree(code, extract_first_func=is_function)
  elif language == properties.LANGUAGE_JAVA:
    return java_tree.get_java_tree(code, wrap_class=is_function)
  else:
    raise RuntimeError("Unsupported language: %s" % language)


def render(folder_path, language):
  for file_path in cache.list_files(folder_path, is_absolute=True, extension=".txt"):
    file_name = cache.get_file_name(file_path)
    LOGGER.info("Rendering '%s' file: %s" % (language, file_name))
    content = cache.read_file(file_path)
    tree = get_tree(content, language, is_function=True)
    img_path = os.path.join(folder_path, "%s.png" % file_name)
    cache.mkdir(cache.get_parent_folder(img_path))
    tree.to_png(img_path)


def dot_java_filter_out_odds():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")
  body1 = DN("body1", parent=func1, label="body")
  ret1 = DN("ret1", parent=body1, label="ret")
  var2 = DN("var2", parent=ret1, label="var")
  call1 = DN("call1", parent=var2, label="call")
  args2 = DN("args2", parent=call1, label="args")
  call2 = DN("call2", parent=call1, label="call")
  args3 = DN("args3", parent=call2, label="args")
  func2 = DN("func2", parent=args3, label="func")
  args4 = DN("args4", parent=func2, label="args")
  var3 = DN("var3", parent=args4, label="var")
  body2 = DN("body2", parent=func2, label="body")
  expr1 = DN("expr1", parent=body2, label="expr")
  op1 = DN("op1", parent=expr1, label="op")
  expr2 = DN("expr2", parent=expr1, label="expr")
  op2 = DN("op2", parent=expr2, label="op")
  var5 = DN("var5", parent=expr2, label="var")
  lit2 = DN("lit2", parent=expr2, label="lit")
  lit1 = DN("lit1", parent=expr1, label="lit")
  call3 = DN("call3", parent=call2, label="call")
  args5 = DN("args5", parent=call3, label="args")
  return func1


def dot_java_func():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")

  body1 = DN("body1", parent=func1, label="body")
  assign1 = DN("assign1", parent=body1, label="assign")
  var2 = DN("var2", parent=assign1, label="var")
  var3 = DN("var3", parent=assign1, label="var")
  call1 = DN("call1", parent=var3, label="call")
  args2 = DN("args2", parent=call1, label="args")
  lit1 = DN("lit", parent=args2, label="lit")
  var4 = DN("var4", parent=args2, label="var")
  call2 = DN("call2", parent=call1, label="call")
  args3 = DN("args3", parent=call2, label="args")

  assign2 = DN("assign2", parent=body1, label="assign")
  var5 = DN("var5", parent=assign2, label="var")
  call3 = DN("call3", parent=assign2, label="call")
  args4 = DN("args4", parent=call3, label="args")

  loop1 = DN("loop1", parent=body1, label="loop")
  cond1 = DN("cond1", parent=loop1, label="cond")
  body2 = DN("body2", parent=loop1, label="body")
  if1 = DN("if", parent=body2, label="if")
  cond2 = DN("cond", parent=if1, label="cond")
  body3 = DN("body3", parent=if1, label="body")
  var6 = DN("var6", parent=body3, label="var")
  call4 = DN("call4", parent=var6, label="call")
  args5 = DN("args5", parent=call4, label="args")
  var7 = DN("var7", parent=args5, label="var")
  call5 = DN("call5", parent=var7, label="call")
  args6 = DN("args6", parent=call5, label="args")
  var8 = DN("var8", parent=args6, label="var")

  ret1 = DN("ret1", parent=body1, label="ret")
  var9 = DN("var9", parent=ret1, label="var")
  call6 = DN("call6", parent=var9, label="call")
  args7 = DN("args7", parent=call6, label="args")

  return func1


def dot_java_getEvens():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")

  body1 = DN("body1", parent=func1, label="body")
  assign1 = DN("assign1", parent=body1, label="assign")
  var5 = DN("var5", parent=assign1, label="var")
  call1 = DN("call1", parent=assign1, label="call")
  args2 = DN("args2", parent=call1, label="args")
  loop1 = DN("loop1", parent=body1, label="loop")
  cond1 = DN("cond1", parent=loop1, label="cond")
  body2 = DN("body2", parent=loop1, label="body")
  if1 = DN("if1", parent=body2, label="if")
  cond2 = DN("cond2", parent=if1, label="cond")
  body3 = DN("body3", parent=cond2, label="body")
  var3 = DN("var3", parent=body3, label="var")
  call2 = DN("call2", parent=var3, label="call")
  args3 = DN("args3", parent=call2, label="args")
  var4 = DN("var4", parent=args3, label="var")
  ret1 = DN("ret1", parent=body1, label="ret")
  var6 = DN("var6", parent=ret1, label="var")
  return func1


def dot_py_all_odds():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")

  body1 = DN("body1", parent=func1, label="body")
  assign1 = DN("assign1", parent=body1, label="assign")
  var5 = DN("var5", parent=assign1, label="var")
  call1 = DN("call1", parent=assign1, label="call")
  loop1 = DN("loop1", parent=body1, label="loop")
  cond1 = DN("cond1", parent=loop1, label="cond")
  body2 = DN("body2", parent=loop1, label="body")
  if1 = DN("if1", parent=body2, label="if")
  cond2 = DN("cond2", parent=if1, label="cond")
  body3 = DN("body3", parent=cond2, label="body")
  var3 = DN("var3", parent=body3, label="var")
  call2 = DN("call2", parent=var3, label="call")
  args3 = DN("args3", parent=call2, label="args")
  var4 = DN("var4", parent=args3, label="var")
  ret1 = DN("ret1", parent=body1, label="ret")
  var6 = DN("var6", parent=ret1, label="var")
  return func1


def dot_py_even_nums():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")
  body1 = DN("body1", parent=func1, label="body")
  assign1 = DN("assign1", parent=body1, label="assign")
  var4 = DN("var4", parent=assign1, label="var")
  call1 = DN("call1", parent=assign1, label="call")
  args2 = DN("args2", parent=call1, label="args")
  var6 = DN("var6", parent=args2, label="var")
  ret1 = DN("ret1", parent=body1, label="ret")
  loop1 = DN("loop1", parent=ret1, label="loop")
  cond1 = DN("cond1", parent=loop1, label="cond")
  body2 = DN("body2", parent=loop1, label="body")
  if1 = DN("if1", parent=body2, label="if")
  cond2 = DN("cond2", parent=if1, label="cond")
  body3 = DN("body3", parent=cond2, label="body")
  var3 = DN("var3", parent=body3, label="var")
  return func1


def dot_py_get_evens():
  func1 = DN("func1", label="func")
  args1 = DN("args1", parent=func1, label="args")
  var1 = DN("var1", parent=args1, label="var")
  body1 = DN("body1", parent=func1, label="body")
  ret1 = DN("ret1", parent=body1, label="ret")
  var2 = DN("var2", parent=ret1, label="var")
  call1 = DN("call1", parent=var2, label="call")
  args2 = DN("args2", parent=call1, label="args")
  func2 = DN("func2", parent=args2, label="func")
  args3 = DN("args3", parent=func2, label="args")
  var3 = DN("var3", parent=args3, label="var")
  body1 = DN("body2", parent=func2, label="body")
  expr1 = DN("expr1", parent=body1, label="expr")
  op1 = DN("op1", parent=expr1, label="op")
  var4 = DN("var4", parent=expr1, label="var")
  lit1 = DN("lit1", parent=expr1, label="lit")
  var5 = DN("var5", parent=args2, label="var")
  call2 = DN("call2", parent=var5, label="call")
  args4 = DN("args4", parent=call2, label="args")
  var6 = DN("var6", parent=args4, label="var")
  return func1


def render_dot(root, file_name):
  DotExporter(root, options=["rankdir=LR;"],
              nodeattrfunc=lambda node: 'shape=none, margin=0, pad=0, fontsize=22, label="{}"'.format(node.label),
              edgeattrfunc=lambda node, child: 'arrowsize=0.5, margin=0, width=0.5, minlen=1').to_picture(file_name)


def render_pptree(node):
  import pptree
  pptree.print_tree(node, nameattr='label')


def render_variable_normalization():
  assign1 = DN("assign1", label="assign")
  var1 = DN("var1", parent=assign1, label="var")
  expr1 = DN("expr1", parent=assign1, label="expr")
  op1 = DN("op1", parent=expr1, label="op")
  expr2 = DN("expr2", parent=expr1, label="expr")
  op2 = DN("op2", parent=expr2, label="op")
  lit1 = DN("lit1", parent=expr2, label="lit")
  lit2 = DN("lit2", parent=expr2, label="lit")
  var2 = DN("var2", parent=expr1, label="var")
  folder_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/common"
  cache.mkdir(folder_path)
  file_name = os.path.join(folder_path, "dot_var_norm.png")
  render_dot(assign1, file_name)


def java_getEvens():
  func1 = N("func", label="func")
  args1 = N("args", parent=func1, label="args")
  var1 = N("var", parent=args1, label="var")
  body1 = N("body", parent=func1, label="body")
  assign1 = N("assign", parent=body1, label="assign")
  var5 = N("var", parent=assign1, label="var")
  call1 = N("call", parent=assign1, label="call")
  args2 = N("args", parent=call1, label="args")
  loop1 = N("loop", parent=body1, label="loop")
  cond1 = N("cond", parent=loop1, label="cond")
  body2 = N("body", parent=loop1, label="body")
  if1 = N("if", parent=body2, label="if")
  cond2 = N("cond", parent=if1, label="cond")
  body3 = N("body", parent=cond2, label="body")
  var3 = N("var", parent=body3, label="var")
  call2 = N("call", parent=var3, label="call")
  args3 = N("args", parent=call2, label="args")
  var4 = N("var", parent=args3, label="var")
  ret1 = N("ret", parent=body1, label="ret")
  var6 = N("var", parent=ret1, label="var")
  return func1


def java_filter_out_odds():
  func1 = N("func", label="func")
  args1 = N("args", parent=func1, label="args")
  var1 = N("var", parent=args1, label="var")
  body1 = N("body", parent=func1, label="body")
  ret1 = N("ret", parent=body1, label="ret")
  var2 = N("var", parent=ret1, label="var")
  call1 = N("call", parent=var2, label="call")
  args2 = N("args", parent=call1, label="args")
  call2 = N("call", parent=call1, label="call")
  args3 = N("args", parent=call2, label="args")
  func2 = N("func", parent=args3, label="func")
  args4 = N("args", parent=func2, label="args")
  var3 = N("var", parent=args4, label="var")
  body2 = N("body", parent=func2, label="body")
  expr1 = N("expr", parent=body2, label="expr")
  op1 = N("op", parent=expr1, label="op")
  expr2 = N("expr", parent=expr1, label="expr")
  op2 = N("op", parent=expr2, label="op")
  var5 = N("var", parent=expr2, label="var")
  lit2 = N("lit", parent=expr2, label="lit")
  lit1 = N("lit", parent=expr1, label="lit")
  call3 = N("call", parent=call2, label="call")
  args5 = N("args", parent=call3, label="args")
  return func1


def java_func():
  func1 = N("func", label="func")
  args1 = N("args", parent=func1, label="args")
  var1 = N("var", parent=args1, label="var")
  body1 = N("body", parent=func1, label="body")
  assign1 = N("assign", parent=body1, label="assign")
  var2 = N("var", parent=assign1, label="var")
  var3 = N("var", parent=assign1, label="var")
  call1 = N("call", parent=var3, label="call")
  args2 = N("args", parent=call1, label="args")
  lit1 = N("lit", parent=args2, label="lit")
  var4 = N("var", parent=args2, label="var")
  call2 = N("call", parent=call1, label="call")
  args3 = N("args", parent=call2, label="args")
  assign2 = N("assign", parent=body1, label="assign")
  var5 = N("var", parent=assign2, label="var")
  call3 = N("call", parent=assign2, label="call")
  args4 = N("args", parent=call3, label="args")
  loop1 = N("loop", parent=body1, label="loop")
  cond1 = N("cond", parent=loop1, label="cond")
  body2 = N("body", parent=loop1, label="body")
  if1 = N("if", parent=body2, label="if")
  cond2 = N("cond", parent=if1, label="cond")
  body3 = N("body", parent=if1, label="body")
  var6 = N("var", parent=body3, label="var")
  call4 = N("call", parent=var6, label="call")
  args5 = N("args", parent=call4, label="args")
  var7 = N("var", parent=args5, label="var")
  call5 = N("call", parent=var7, label="call")
  args6 = N("args", parent=call5, label="args")
  var8 = N("var", parent=args6, label="var")
  ret1 = N("ret", parent=body1, label="ret")
  var9 = N("var", parent=ret1, label="var")
  call6 = N("call", parent=var9, label="call")
  args7 = N("args", parent=call6, label="args")
  return func1


def py_all_odds():
  func1 = N("func", label="func")
  args1 = N("args", parent=func1, label="args")
  var1 = N("var", parent=args1, label="var")

  body1 = N("body", parent=func1, label="body")
  assign1 = N("assign", parent=body1, label="assign")
  var5 = N("var", parent=assign1, label="var")
  call1 = N("call", parent=assign1, label="call")
  loop1 = N("loop", parent=body1, label="loop")
  cond1 = N("cond", parent=loop1, label="cond")
  body2 = N("body", parent=loop1, label="body")
  if1 = N("if", parent=body2, label="if")
  cond2 = N("cond", parent=if1, label="cond")
  body3 = N("body", parent=cond2, label="body")
  var3 = N("var", parent=body3, label="var")
  call2 = N("call", parent=var3, label="call")
  args3 = N("args", parent=call2, label="args")
  var4 = N("var", parent=args3, label="var")
  ret1 = N("ret", parent=body1, label="ret")
  var6 = N("var", parent=ret1, label="var")
  return func1


def py_even_nums():
  func1 = N("func", label="func")
  args1 = N("args", parent=func1, label="args")
  var1 = N("var", parent=args1, label="var")
  body1 = N("body", parent=func1, label="body")
  assign1 = N("assign", parent=body1, label="assign")
  var4 = N("var", parent=assign1, label="var")
  call1 = N("call", parent=assign1, label="call")
  args2 = N("args", parent=call1, label="args")
  var6 = N("var", parent=args2, label="var")
  ret1 = N("ret", parent=body1, label="ret")
  loop1 = N("loop", parent=ret1, label="loop")
  cond1 = N("cond", parent=loop1, label="cond")
  body2 = N("body", parent=loop1, label="body")
  if1 = N("if", parent=body2, label="if")
  cond2 = N("cond", parent=if1, label="cond")
  body3 = N("body", parent=cond2, label="body")
  var3 = N("var", parent=body3, label="var")
  return func1


def py_get_evens():
  DN = N
  func1 = DN("func", label="func")
  args1 = DN("args", parent=func1, label="args")
  var1 = DN("var", parent=args1, label="var")
  body1 = DN("body", parent=func1, label="body")
  ret1 = DN("ret", parent=body1, label="ret")
  var2 = DN("var", parent=ret1, label="var")
  call1 = DN("call", parent=var2, label="call")
  args2 = DN("args", parent=call1, label="args")
  func2 = DN("func", parent=args2, label="func")
  args3 = DN("args", parent=func2, label="args")
  var3 = DN("var", parent=args3, label="var")
  body1 = DN("body", parent=func2, label="body")
  expr1 = DN("expr", parent=body1, label="expr")
  op1 = DN("op", parent=expr1, label="op")
  var4 = DN("var", parent=expr1, label="var")
  lit1 = DN("lit", parent=expr1, label="lit")
  var5 = DN("var", parent=args2, label="var")
  call2 = DN("call", parent=var5, label="call")
  args4 = DN("args", parent=call2, label="args")
  var6 = DN("var", parent=args4, label="var")
  return func1


def tree_comp():
  trees = {
    "a": java_getEvens(),
    "b": py_all_odds(),
    "c": java_filter_out_odds(),
    "d": java_func(),
    "e": py_get_evens(),
    "f": py_even_nums()
  }
  keys = sorted(trees.keys())
  for i in range(len(keys) - 1):
    for j in range(i+1, len(keys)):
      k_i = keys[i]
      k_j = keys[j]
      dist_a = apted_distance(trees[k_i], trees[k_j])
      dist_b = apted_distance(trees[k_j], trees[k_i])
      print(k_i, k_j, dist_a, dist_b)


def _main():
  # render("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/java", properties.LANGUAGE_JAVA)
  # render("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/py", properties.LANGUAGE_PYTHON)
  folder_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper"
  render_dot(dot_java_filter_out_odds(), os.path.join(folder_path, "java", "dot_filterOutOdds.png"))
  render_dot(dot_java_func(), os.path.join(folder_path, "java", "dot_func.png"))
  render_dot(dot_java_getEvens(), os.path.join(folder_path, "java", "dot_getEvens.png"))
  render_dot(dot_py_all_odds(), os.path.join(folder_path, "py", "dot_py_all_odds.png"))
  render_dot(dot_py_even_nums(), os.path.join(folder_path, "py", "dot_py_even_nums.png"))
  render_dot(dot_py_get_evens(), os.path.join(folder_path, "py", "dot_py_get_evens.png"))


if __name__ == "__main__":
  render_pptree(dot_java_filter_out_odds())
  # tree_comp()
  # render_variable_normalization()
