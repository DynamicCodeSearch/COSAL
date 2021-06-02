import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import ast_utils
from analysis.parsers import parser
from utils import cache
from mos.search.tree.common import Node as N, TYPES, OPERATORS, MODE, LITERAL
import ast


def get_ast(source_code, extract_first_func=False):
  try:
    source_code = ast_utils.remove_comments_and_docstrings(source_code)
  except Exception:
    pass
  if extract_first_func:
    return ast_utils.parse_function(source_code, use_ast_tokens=True)
  else:
    return ast_utils.parse(source_code, use_ast_tokens=True)


def get_ctx(ctx):
  if not ctx:
    return None
  elif isinstance(ctx, ast.AugLoad):
    return MODE.LOAD
  elif isinstance(ctx, ast.AugStore):
    return MODE.STORE
  elif isinstance(ctx, ast.Del):
    return MODE.DELETE
  elif isinstance(ctx, ast.Load):
    return MODE.LOAD
  elif isinstance(ctx, ast.Store):
    return MODE.STORE
  elif isinstance(ctx, ast.Param):
    return None
  else:
    return None


class TreeVisitor(parser.Traveller):
  """
  Some relaxations:
  1. Loop and conditional conditions are not expanded
  2. Slice, index, ExtSlice etc are all marked as INDEX
  3. Dicts, Lists, Sets etc are marked as function call.
  """
  def __init__(self, tree):
    parser.Traveller.__init__(self)
    self.tree = tree
    self.vertex = None

  def parse(self):
    meta = {}
    self.vertex = self.visit(self.tree, meta)
    return self.vertex

  def visit_Module(self, node, meta):
    root_vertex = N(TYPES.ROOT)
    if node.body:
      for stmt in node.body:
        root_vertex.add_kid(self.visit(stmt, meta))
    return root_vertex

  def visit_ClassDef(self, node, meta):
    class_vertex = N(TYPES.CLASS_DEF)
    if node.body:
      body = N(TYPES.BODY)
      for stmt in node.body:
        body.add_kid(self.visit(stmt, meta))
      class_vertex.add_kid(body)
    return class_vertex

  def visit_FunctionDef(self, node, meta):
    args = N(TYPES.ARGS)
    if node.args.args:
      for arg in node.args.args:
        args.add_kid(N(TYPES.VARIABLE))
    if node.args.vararg:
      args.add_kid(N(TYPES.VARIABLE))
    if node.args.kwarg:
      args.add_kid(N(TYPES.VARIABLE))
    body = N(TYPES.BODY)
    for stmt in node.body:
      body.add_kid(self.visit(stmt, meta))
    func = N(TYPES.FUNCTION_DEF)
    func.add_kid(args)
    func.add_kid(body)
    return func

  """
  Operators
  """
  def visit_Add(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.ADD)

  def visit_BitAnd(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.BIT_AND)

  def visit_BitOr(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.OR)

  def visit_BitXor(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.BIT_XOR)

  def visit_Div(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.DIV)

  def visit_FloorDiv(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.DIV)

  def visit_LShift(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.LSHIFT)

  def visit_Mod(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.MOD)

  def visit_Mult(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.MULT)

  def visit_Pow(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.POW)

  def visit_RShift(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.RSHIFT)

  def visit_Sub(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.SUB)

  def visit_And(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.AND)

  def visit_Or(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.OR)

  def visit_Eq(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.EQ)

  def visit_Gt(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.GT)

  def visit_GtE(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.GTE)

  def visit_In(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.IN)

  def visit_Is(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.IS)

  def visit_IsNot(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.IS_NOT)

  def visit_Lt(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.LT)

  def visit_LtE(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.LTE)

  def visit_NotEq(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.NOT_EQ)

  def visit_NotIn(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.NOT_IN)

  def visit_Invert(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.INVERT)

  def visit_UAdd(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.ADD)

  def visit_USub(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.SUB)

  def visit_Not(self, node, meta):
    return N(TYPES.OPERATOR, value=OPERATORS.NOT)

  """
  Statements
  """
  def visit_Assert(self, node, meta):
    assert_vertex = N(TYPES.ASSERT)
    if node.test:
      assert_vertex.add_kid(self.visit(node.test, meta))
    if node.msg:
      assert_vertex.add_kid(self.visit(node.msg, meta))
    return assert_vertex

  def visit_Assign(self, node, meta):
    assign_vertex = N(TYPES.ASSIGN)
    if node.targets:
      # assert len(node.targets) == 1, "@COSAL: We support only single var assignment"
      for target in node.targets:
        assign_vertex.add_kid(self.visit(target))
    if node.value:
      assign_vertex.add_kid(self.visit(node.value))
    return assign_vertex

  def visit_AugAssign(self, node, meta):
    assign_vertex = N(TYPES.AUG_ASSIGN)
    if node.target:
      if isinstance(node.target, list):
        assign_vertex.add_kid(self.visit(node.target[0]))
      else:
        assign_vertex.add_kid(self.visit(node.target))
    # TODO: Consider adding node.op as well
    if node.value:
      assign_vertex.add_kid(self.visit(node.value))
    return assign_vertex

  def visit_Break(self, node, meta):
    return N(TYPES.BREAK)

  def visit_Continue(self, node, meta):
    return N(TYPES.CONTINUE)

  def visit_Delete(self, node, meta):
    return N(TYPES.DELETE)

  def visit_Exec(self, node, meta):
    return N(TYPES.EXEC)

  def visit_Expr(self, node, meta):
    if node.value:
      return self.visit(node.value, meta)
    return None

  def visit_For(self, node, meta):
    loop_vertex = N(TYPES.LOOP)
    loop_vertex.add_kid(N(TYPES.LOOP_CONDITION))
    loop_body = N(TYPES.BODY)
    if node.body:
      for stmt in node.body:
        loop_body.add_kid(self.visit(stmt, meta))
    loop_vertex.add_kid(loop_body)
    return loop_vertex

  def visit_If(self, node, meta):
    if_vertex = N(TYPES.IF)
    if node.test:
      if_vertex.add_kid(N(TYPES.IF_CONDITION))
    if_body = N(TYPES.BODY)
    if node.body:
      for stmt in node.body:
        if_body.add_kid(self.visit(stmt, meta))
    if_vertex.add_kid(if_body)
    if node.orelse:
      else_body = N(TYPES.ELSE)
      for stmt in node.orelse:
        else_body.add_kid(self.visit(stmt, meta))
      if_vertex.add_kid(else_body)
    return if_vertex

  # def visit_Import(self, node, meta):
  #   return N(TYPES.IMPORT)
  #
  # def visit_ImportFrom(self, node, meta):
  #   return N(TYPES.IMPORT)

  def visit_Pass(self, node, meta):
    return N(TYPES.PASS)

  def visit_Print(self, node, meta):
    func_vertex = N(TYPES.FUNCTION_CALL)
    func_vertex.add_kid(N(TYPES.VARIABLE))
    args = N(TYPES.ARGS)
    if node.values:
      for val in node.values:
        args.add_kid(self.visit(val, meta))
    func_vertex.add_kid(args)
    return func_vertex

  def visit_Raise(self, node, meta):
    return N(TYPES.RAISE)

  def visit_Return(self, node, meta):
    return_vertex = N(TYPES.RETURN)
    if node.value:
      return_vertex.add_kid(self.visit(node.value, meta))
    return return_vertex

  def visit_TryFinally(self, node, meta):
    try_node = N(TYPES.TRY)
    if node.body:
      body_node = N(TYPES.BODY)
      body = node.body[0].body if isinstance(node.body[0], ast.TryExcept) else node.body
      for stmt in body:
        body_node.add_kid(self.visit(stmt, meta))
      try_node.add_kid(body_node)
      if isinstance(node.body[0], ast.TryExcept) and node.body[0].handlers:
        for handler in node.body[0].handlers:
          try_node.add_kid(self.visit(handler, meta))
    if node.finalbody:
      finally_node = N(TYPES.FINALLY)
      for stmt in node.finalbody:
        finally_node.add_kid(self.visit(stmt, meta))
      try_node.add_kid(finally_node)
    return try_node

  def visit_TryExcept(self, node, meta):
    try_node = N(TYPES.TRY)
    if node.body:
      body_node = N(TYPES.BODY)
      for stmt in node.body:
        body_node.add_kid(self.visit(stmt, meta))
      try_node.add_kid(body_node)
    if node.handlers:
      for handler in node.handlers:
        try_node.add_kid(self.visit(handler, meta))
    return try_node

  def visit_While(self, node, meta):
    loop_vertex = N(TYPES.LOOP)
    loop_vertex.add_kid(N(TYPES.LOOP_CONDITION))
    loop_body = N(TYPES.BODY)
    if node.body:
      for stmt in node.body:
        loop_body.add_kid(self.visit(stmt, meta))
    loop_vertex.add_kid(loop_body)
    return loop_vertex

  def visit_With(self, node, meta):
    with_vertex = N(TYPES.WITH)
    if node.body:
      body_vertex = N(TYPES.BODY)
      for stmt in node.body:
        body_vertex.add_kid(self.visit(stmt, meta))
      with_vertex.add_kid(body_vertex)
    return with_vertex

  """
  Expressions
  """
  def visit_Attribute(self, node, meta):
    attr_vertex = N(TYPES.ATTRIBUTE, mode=get_ctx(node.ctx))
    if meta is None:
      meta = {}
    visited = self.visit(node.value, meta)
    if "inner" in meta:
      meta["inner"].add_kid(attr_vertex)
    else:
      visited.add_kid(attr_vertex)
    meta["inner"] = attr_vertex
    return visited

  def visit_BinOp(self, node, meta):
    bin_op = N(TYPES.OPERATOR_EXPR)
    bin_op.add_kid(self.visit(node.op, meta))
    if node.left:
      bin_op.add_kid(self.visit(node.left, meta))
    if node.right:
      bin_op.add_kid(self.visit(node.right, meta))
    return bin_op

  def visit_BoolOp(self, node, meta):
    bool_op = N(TYPES.OPERATOR_EXPR)
    bool_op.add_kid(self.visit(node.op, meta))
    if node.values:
      for val in node.values:
        bool_op.add_kid(self.visit(val, meta))
    return bool_op

  def visit_Call(self, node, meta):
    call_op = N(TYPES.FUNCTION_CALL)
    child_op = None
    args = N(TYPES.ARGS)
    if node.args:
      for arg in node.args:
        args.add_kid(self.visit(arg, None))
    if node.keywords:
      for kw in node.keywords:
        args.add_kid(self.visit(kw, None))
    if node.starargs:
      args.add_kid(self.visit(node.starargs, None))
    if node.starargs:
      args.add_kid(self.visit(node.kwargs, None))
    if meta is None:
      meta = {}
    visited = self.visit(node.func, meta)
    call_op.add_kid(args)
    if "inner" in meta:
      meta["inner"].add_kid(call_op)
    else:
      visited.add_kid(call_op)
    meta["inner"] = call_op
    return visited

  def visit_Subscript(self, node, meta):
    subscript_vertex = N(TYPES.ARRAY_ACCESS, mode=get_ctx(node.ctx))
    if meta is None:
      meta = {}
    visited = self.visit(node.value, meta)
    subscript_vertex.add_kid(self.visit(node.slice, None))
    if "inner" in meta:
      meta["inner"].add_kid(subscript_vertex)
    else:
      visited.add_kid(subscript_vertex)
    return visited

  def visit_Compare(self, node, meta):
    comp_op = N(TYPES.OPERATOR_EXPR)
    if node.ops:
      for op in node.ops:
        comp_op.add_kid(self.visit(op, meta))
    if node.left:
      comp_op.add_kid(self.visit(node.left, meta))
    if node.comparators:
      for n_c in node.comparators:
        comp_op.add_kid(self.visit(n_c, meta))
    return comp_op

  def visit_comprehension(self, node, meta):
    loop_vertex = N(TYPES.LOOP)
    loop_vertex.add_kid(N(TYPES.LOOP_CONDITION))
    loop_body = N(TYPES.BODY)
    base_ifs, next_ifs = None, None
    if node.ifs:
      for if_node in node.ifs:
        if_vertex = N(TYPES.IF)
        if_vertex.add_kid(N(TYPES.IF_CONDITION))
        if_body = N(TYPES.BODY)
        if base_ifs is None:
          base_ifs = if_vertex
        else:
          next_ifs.add_kid(if_vertex)
        if_vertex.add_kid(if_body)
        next_ifs = if_body
      loop_body.add_kid(base_ifs)
    if meta is not None:
      if next_ifs is not None:
        meta["append_to"] = next_ifs
      else:
        meta["append_to"] = loop_body
    loop_vertex.add_kid(loop_body)
    return loop_vertex

  def visit_Dict(self, node, meta):
    # TODO: Might need to expand this
    return N(TYPES.FUNCTION_CALL)

  def visit_DictComp(self, node, meta):
    assert len(node.generators) >= 1
    base_generators, next_generators = None, None
    for comprehension_node in node.generators:
      local_meta = {}
      comp_vertex = self.visit(comprehension_node, local_meta)
      if base_generators is None:
        base_generators = comp_vertex
      else:
        next_generators.add_kid(comp_vertex)
      assert "append_to" in local_meta
      next_generators = local_meta["append_to"]
    if node.key and node.value:
      assign_vertex = N(TYPES.ASSIGN)
      assign_vertex.add_kid(self.visit(node.key, meta))
      assign_vertex.add_kid(self.visit(node.value, meta))
      next_generators.add_kid(assign_vertex)
    return base_generators

  def visit_Ellipsis(self, node, meta):
    return N(TYPES.INDEX)

  def visit_ExceptHandler(self, node, meta):
    except_vertex = N(TYPES.EXCEPT)
    if node.name:
      except_vertex.add_kid(N(TYPES.VARIABLE))
    body = N(TYPES.BODY)
    if node.body:
      for stmt in node.body:
        body.add_kid(self.visit(stmt, meta))
    except_vertex.add_kid(body)
    return except_vertex

  def visit_Expression(self, node, meta):
    if not node.body:
      return None
    if len(node.body) == 1:
      return self.visit(node.body[0], meta)
    else:
      body_vertex = N(TYPES.BODY)
      for stmt in node.body:
        body_vertex.add_kid(self.visit(stmt, meta))
      return body_vertex

  def visit_ExtSlice(self, node, meta):
    return N(TYPES.INDEX)

  def visit_GeneratorExp(self, node, meta):
    assert len(node.generators) >= 1
    base_generators, next_generators = None, None
    for comprehension_node in node.generators:
      local_meta = {}
      comp_vertex = self.visit(comprehension_node, local_meta)
      if base_generators is None:
        base_generators = comp_vertex
      else:
        next_generators.add_kid(comp_vertex)
      assert "append_to" in local_meta
      next_generators = local_meta["append_to"]
    if node.elt:
      next_generators.add_kid(self.visit(node.elt, meta))
    return base_generators

  def visit_IfExp(self, node, meta):
    if_vertex = N(TYPES.IF)
    if node.test:
      if_vertex.add_kid(N(TYPES.IF_CONDITION))
    if_body = N(TYPES.BODY)
    if node.body:
      if_body.add_kid(self.visit(node.body, meta))
    if_vertex.add_kid(if_body)
    if node.orelse:
      else_body = N(TYPES.ELSE)
      else_body.add_kid(self.visit(node.orelse, meta))
      if_vertex.add_kid(else_body)
    return if_vertex

  def visit_Index(self, node, meta):
    return N(TYPES.INDEX)

  def visit_keyword(self, node, meta):
    kw_vertex = N(TYPES.ASSIGN)
    kw_vertex.add_kid(N(TYPES.VARIABLE))
    if node.value:
      kw_vertex.add_kid(self.visit(node.value, meta))
    return kw_vertex

  def visit_Lambda(self, node, meta):
    args = N(TYPES.ARGS)
    if node.args.args:
      for arg in node.args.args:
        args.add_kid(N(TYPES.VARIABLE))
    if node.args.vararg:
      args.add_kid(N(TYPES.VARIABLE))
    if node.args.kwarg:
      args.add_kid(N(TYPES.VARIABLE))
    body = N(TYPES.BODY)
    if node.body:
      body.add_kid(self.visit(node.body, meta))
    func = N(TYPES.FUNCTION_DEF)
    func.add_kid(args)
    func.add_kid(body)
    return func

  def visit_List(self, node, meta):
    # TODO: Might need to expand this
    return N(TYPES.FUNCTION_CALL)

  def visit_ListComp(self, node, meta):
    return self.visit_GeneratorExp(node, meta)

  def visit_Name(self, node, meta):
    if node.id == "True" or node.id == "False":
      return N(TYPES.LITERAL, value=LITERAL.BOOLEAN)
    elif node.id == "None":
      return N(TYPES.LITERAL, value=LITERAL.NULL)
    return N(TYPES.VARIABLE, mode=get_ctx(node.ctx))

  def visit_Num(self, node, meta):
    return N(TYPES.LITERAL, value=LITERAL.NUMERIC)

  def visit_Set(self, node, meta):
    # TODO: Might need to expand this
    return N(TYPES.FUNCTION_CALL)

  def visit_SetComp(self, node, meta):
    return self.visit_GeneratorExp(node, meta)

  def visit_Slice(self, node, meta):
    return N(TYPES.INDEX)

  def visit_Str(self, node, meta):
    return N(TYPES.LITERAL, value=LITERAL.STRING)

  def visit_Tuple(self, node, meta):
    # TODO: Might need to expand this
    return N(TYPES.FUNCTION_CALL)

  def visit_UnaryOp(self, node, meta):
    unary_op = N(TYPES.OPERATOR_EXPR)
    if node.op:
      unary_op.add_kid(self.visit(node.op, meta))
    if node.operand:
      unary_op.add_kid(self.visit(node.operand, meta))
    return unary_op

  def visit_Yield(self, node, meta):
    yield_op = N(TYPES.YIELD)
    if node.value:
      yield_op.add_kid(self.visit(node.value, meta))
    return yield_op


def get_py_tree(source_code, extract_first_func=False):
  """
  Generate Python Tree
  :param source_code: Python Source code
  :param extract_first_func: if true returns only the first function
  :return: an instance of mos.search.tree.common.Node
  """
  tree = get_ast(source_code, extract_first_func=extract_first_func)
  if not tree:
    return None
  visitor = TreeVisitor(tree)
  return visitor.parse()


def test():
  file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/py/get_evens.txt"
  contents = cache.read_file(file_path)
  tree = get_ast(contents, extract_first_func=True)
  if not tree:
    return
  ast_utils.pretty_print(tree)
  visitor = TreeVisitor(tree)
  vertex = visitor.parse()
  vertex.to_png("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/py/tmp.png")
  # bson = vertex.to_bson()
  # reconstructed = N.from_bson(bson)
  # print(reconstructed == vertex)
  # # img_path = "%s.png" % file_path.rsplit(".")[0]
  # vertex.to_png(img_path)


if __name__ == "__main__":
  test()
