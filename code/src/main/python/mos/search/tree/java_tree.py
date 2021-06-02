import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils import cache
from mos.search.tree.java_utils.java_tree_formatter import pprint
from mos.search.tree.common import Node as N, TYPES, OPERATORS, MODE, LITERAL
from analysis.parsers import parser

import traceback
import javalang
from javalang import tree as jtree


def parse_java(source, wrap_class=False):
  if wrap_class:
    source = "public class TEMP_SLACC_CLASS  { %s }" % source
  try:
    return javalang.parse.parse(source)
  except javalang.parser.JavaSyntaxError:
    return None


def is_numeric(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


class MethodVisitor(parser.JavaTraveller):
  def __init__(self, source_code):
    parser.JavaTraveller.__init__(self)
    self.tree = parse_java(source_code, wrap_class=False)
    self.method_count = 0

  def visit_MethodDeclaration(self, node, meta):
    self.method_count += 1
    return None

  def parse(self):
    self.visit(self.tree)
    return self.method_count



class TreeVisitor(parser.JavaTraveller):
  def __init__(self, source_code, wrap_class=False):
    parser.JavaTraveller.__init__(self)
    if wrap_class:
      self.tree = TreeVisitor.get_first_method_node(parse_java(source_code, wrap_class=wrap_class))
    else:
      self.tree = parse_java(source_code, wrap_class=wrap_class)
    self.vertex = None

  @staticmethod
  def get_first_method_node(compilation_unit):
    if compilation_unit and compilation_unit.types and compilation_unit.types[0].body:
      if isinstance(compilation_unit.types[0].body[0], jtree.MethodDeclaration) or isinstance(compilation_unit.types[0].body[0], jtree.ConstructorDeclaration):
        return compilation_unit.types[0].body[0]
    return None

  @staticmethod
  def get_qualifier_nodes(qualifier_name):
    base_qual, inner_qual = None, None
    for qual in qualifier_name.split("."):
      if base_qual is None:
        base_qual = inner_qual = N(TYPES.VARIABLE, mode=MODE.LOAD)
      else:
        kid = N(TYPES.VARIABLE, mode=MODE.LOAD)
        inner_qual.add_kid(kid)
        inner_qual = kid
    return base_qual, inner_qual

  @staticmethod
  def get_operator_node(op):
    op = str(op)
    # Math
    if op == '+':
      return N(TYPES.OPERATOR, value=OPERATORS.ADD)
    elif op == '-':
      return N(TYPES.OPERATOR, value=OPERATORS.SUB)
    elif op == "*":
      return N(TYPES.OPERATOR, value=OPERATORS.MULT)
    elif op == "/":
      return N(TYPES.OPERATOR, value=OPERATORS.DIV)
    elif op == "%":
      return N(TYPES.OPERATOR, value=OPERATORS.MOD)
    elif op == "++":
      return N(TYPES.OPERATOR, value=OPERATORS.INC)
    elif op == "--":
      return N(TYPES.OPERATOR, value=OPERATORS.DEC)
    # Comparison
    elif op == "==":
      return N(TYPES.OPERATOR, value=OPERATORS.EQ)
    elif op == "!=":
      return N(TYPES.OPERATOR, value=OPERATORS.NOT_EQ)
    elif op == ">":
      return N(TYPES.OPERATOR, value=OPERATORS.GT)
    elif op == ">=":
      return N(TYPES.OPERATOR, value=OPERATORS.GTE)
    elif op == "<":
      return N(TYPES.OPERATOR, value=OPERATORS.LT)
    elif op == "<=":
      return N(TYPES.OPERATOR, value=OPERATORS.LTE)
    # Logical
    elif op == "&&":
      return N(TYPES.OPERATOR, value=OPERATORS.AND)
    elif op == "||":
      return N(TYPES.OPERATOR, value=OPERATORS.OR)
    elif op == "!":
      return N(TYPES.OPERATOR, value=OPERATORS.NOT)
    # Bit
    elif op == "&":
      return N(TYPES.OPERATOR, value=OPERATORS.BIT_AND)
    elif op == "|":
      return N(TYPES.OPERATOR, value=OPERATORS.BIT_OR)
    elif op == "~":
      return N(TYPES.OPERATOR, value=OPERATORS.INVERT)
    elif op == "^":
      return N(TYPES.OPERATOR, value=OPERATORS.BIT_XOR)
    elif op == "<<":
      return N(TYPES.OPERATOR, value=OPERATORS.LSHIFT)
    elif op == ">>":
      return N(TYPES.OPERATOR, value=OPERATORS.RSHIFT)
    elif op == ">>>":
      return N(TYPES.OPERATOR, value=OPERATORS.RSHIFT0)
    elif op == "instanceof":
      return N(TYPES.OPERATOR, value=OPERATORS.INSTANCE_OF)
    else:
      raise RuntimeError("Unknown operator: %s" % op)

  def parse(self):
    if self.tree:
      self.vertex = self.visit(self.tree, None)
    return self.vertex

  """
  Class declaration
  """

  def visit_CompilationUnit(self, node, meta):
    root_vertex = N(TYPES.ROOT)
    if node.types:
      for typ in node.types:
        root_vertex.add_kid(self.visit(typ, meta))
    return root_vertex

  def visit_InterfaceDeclaration(self, node, meta):
    return None

  def visit_ClassDeclaration(self, node, meta):
    if node.modifiers and 'abstract' in node.modifiers:
      return None
    class_vertex = N(TYPES.CLASS_DEF)
    if node.body:
      body = N(TYPES.BODY)
      for stmt in node.body:
        visited = self.visit(stmt, meta)
        body.add_kid(visited)
      class_vertex.add_kid(body)
    return class_vertex

  def visit_InnerClassCreator(self, node, meta):
    class_vertex = N(TYPES.CLASS_DEF)
    if node.arguments:
      args = N(TYPES.ARGS)
      for arg in node.arguments:
        args.add_kid(self.visit(arg, meta))
    if node.body:
      body = N(TYPES.BODY)
      for stmt in node.body:
        body.add_kid(self.visit(stmt, meta))
      class_vertex.add_kid(body)
    return class_vertex

  """
  Member declaration
  """

  def visit_MethodDeclaration(self, node, meta):
    args = N(TYPES.ARGS)
    for parameter in node.parameters:
      args.add_kid(N(TYPES.VARIABLE))
    # print(node)
    body = N(TYPES.BODY)
    if node.body:
      for stmt in node.body:
        body.add_kid(self.visit(stmt, meta))
    func = N(TYPES.FUNCTION_DEF)
    func.add_kid(args)
    func.add_kid(body)
    return func

  def visit_FieldDeclaration(self, node, meta):
    kids = []
    for declarator in node.declarators:
      kids.append(self.visit(declarator, meta))
    return kids

  def visit_ConstructorDeclaration(self, node, meta):
    return self.visit_MethodDeclaration(node, meta)

  def visit_ConstantDeclaration(self, node, meta):
    return self.visit_FieldDeclaration(node, meta)

  """
  Start TYPES
  """

  def visit_BasicType(self, node, meta):
    return N(TYPES.VARIABLE)

  def visit_ReferenceType(self, node, meta):
    return N(TYPES.VARIABLE)

  """
  End TYPES
  """

  def visit_LocalVariableDeclaration(self, node, meta):
    return self.visit_FieldDeclaration(node, meta)

  def visit_VariableDeclarator(self, node, meta):
    assign_vertex = N(TYPES.ASSIGN)
    if node.name:
      assign_vertex.add_kid(N(TYPES.VARIABLE, mode=MODE.STORE))
    if node.initializer:
      initialized_node = self.visit(node.initializer, meta)
      if initialized_node:
        assign_vertex.add_kid(initialized_node)
      else:
        assign_vertex.add_kid(N(TYPES.LITERAL, value=LITERAL.NULL))
    else:
      assign_vertex.add_kid(N(TYPES.LITERAL, value=LITERAL.NULL))
    return assign_vertex

  def visit_ClassCreator(self, node, meta):
    class_creator_vertex = N(TYPES.FUNCTION_CALL)
    if node.type:
      class_creator_vertex.add_kid(self.visit(node.type, meta))
    args = N(TYPES.ARGS)
    for arg in node.arguments:
      args.add_kid(self.visit(arg, meta))
    class_creator_vertex.add_kid(args)
    if node.body:
      body = N(TYPES.BODY)
      for stmt in node.body:
        body.add_kid(self.visit(stmt, meta))
      class_creator_vertex.add_kid(body)
    return class_creator_vertex

  def visit_ArrayCreator(self, node, meta):
    return N(TYPES.FUNCTION_CALL)

  def visit_ArrayInitializer(self, node, meta):
    return N(TYPES.FUNCTION_CALL)

  """
  Start Expressions 
  """
  def visit_StatementExpression(self, node, meta):
    if node.expression:
      return self.visit(node.expression, meta)
    return None

  def visit_Assignment(self, node, meta):
    assign_vertex = N(TYPES.ASSIGN) if node.type == "=" else N(TYPES.AUG_ASSIGN)
    if node.expressionl:
      assign_vertex.add_kid(self.visit(node.expressionl, None))
    if node.value:
      assign_vertex.add_kid(self.visit(node.value, None))
    return assign_vertex

  def visit_This(self, node, meta):
    return self.visit_MemberReference(node, None)

  def visit_Literal(self, node, meta):
    val = node.value
    if val == "null":
      return N(TYPES.LITERAL, value=LITERAL.NULL)
    elif val == "true" or val == "false":
      return N(TYPES.LITERAL, value=LITERAL.BOOLEAN)
    elif is_numeric(val):
      return N(TYPES.LITERAL, value=LITERAL.NUMERIC)
    else:
      return N(TYPES.LITERAL, value=LITERAL.STRING)

  def visit_MethodInvocation(self, node, meta):
    method_call = N(TYPES.FUNCTION_CALL)
    qual_node, inner_qual_node = None, None
    if node.qualifier:
      qual_node, inner_qual_node = TreeVisitor.get_qualifier_nodes(node.qualifier)
    member = self.visit(node.member) if "member" in node and isinstance(node.member, jtree.Node) else N(TYPES.ATTRIBUTE)
    args = N(TYPES.ARGS)
    if node.arguments:
      for arg in node.arguments:
        args.add_kid(self.visit(arg, None))
    member.add_kid(method_call)
    method_call.add_kid(args)
    prior_vertex = method_call
    if node.selectors:
      for selector in node.selectors:
        select_vertex = self.visit(selector)
        prior_vertex.add_kid(select_vertex)
        if select_vertex:
          if isinstance(selector, jtree.MethodInvocation) and len(select_vertex.zkids) > 0:
            prior_vertex = select_vertex.zkids[0]
          else:
            prior_vertex = select_vertex
    if qual_node and inner_qual_node:
      inner_qual_node.add_kid(member)
      return qual_node
    else:
      return member

  def visit_SuperMethodInvocation(self, node, meta):
    return self.visit_MethodInvocation(node, meta)

  def visit_ExplicitConstructorInvocation(self, node, meta):
    return self.visit_MethodInvocation(node, meta)

  def visit_SuperConstructorInvocation(self, node, meta):
    return self.visit_MethodInvocation(node, meta)

  def visit_MemberReference(self, node, meta):
    qual_node, inner_qual_node = None, None
    if node.qualifier:
      qual_node, inner_qual_node = TreeVisitor.get_qualifier_nodes(node.qualifier)
    member = self.visit(node.member) if "member" in node and isinstance(node.member, jtree.Node) else N(TYPES.ATTRIBUTE)
    prior_vertex = member
    if node.selectors:
      for selector in node.selectors:
        select_vertex = self.visit(selector)
        prior_vertex.add_kid(select_vertex)
        if select_vertex:
          if isinstance(selector, jtree.MethodInvocation) and len(select_vertex.zkids) > 0:
            prior_vertex = select_vertex.zkids[0]
          else:
            prior_vertex = select_vertex
    if qual_node and inner_qual_node:
      inner_qual_node.add_kid(member)
      return qual_node
    else:
      return member

  def visit_SuperMemberReference(self, node, meta):
    return self.visit_MemberReference(node, meta)

  def visit_ArraySelector(self, node, meta):
    subscript_vertex = N(TYPES.ARRAY_ACCESS)
    if node.index:
      subscript_vertex.add_kid(N(TYPES.INDEX))
    return subscript_vertex

  def visit_BinaryOperation(self, node, meta):
    bin_op = N(TYPES.OPERATOR_EXPR)
    bin_op.add_kid(TreeVisitor.get_operator_node(node.operator))
    if node.operandl:
      bin_op.add_kid(self.visit(node.operandl, None))
    if node.operandr:
      bin_op.add_kid(self.visit(node.operandr, None))
    return bin_op

  def visit_TernaryExpression(self, node, meta):
    if_vertex = N(TYPES.IF)
    if node.condition:
      if_vertex.add_kid(N(TYPES.IF_CONDITION))
    if_body = N(TYPES.BODY)
    if node.if_true:
      if_body.add_kid(self.visit(node.if_true, None))
    if_vertex.add_kid(if_body)
    if node.if_false:
      else_body = N(TYPES.ELSE)
      else_body.add_kid(self.visit(node.if_false, None))
      if_vertex.add_kid(else_body)
    return if_vertex

  def visit_LambdaExpression(self, node, meta):
    args = N(TYPES.ARGS)
    for param in node.parameters:
      args.add_kid(N(TYPES.VARIABLE))
    body = N(TYPES.BODY)
    if node.body:
      if isinstance(node.body, list):
        for stmt in node.body:
          body.add_kid(self.visit(stmt, None))
      else:
        body.add_kid(self.visit(node.body, None))
    func = N(TYPES.FUNCTION_DEF)
    func.add_kid(args)
    func.add_kid(body)
    return func

  """
  End Expressions 
  """

  """
  Start Statements
  """
  def visit_IfStatement(self, node, meta):
    if_vertex = N(TYPES.IF)
    if node.condition:
      if_vertex.add_kid(N(TYPES.IF_CONDITION))
    if node.then_statement:
      if isinstance(node.then_statement, jtree.BlockStatement):
        if_vertex.add_kid(self.visit(node.then_statement))
      else:
        body_vertex = N(TYPES.BODY)
        body_vertex.add_kid(self.visit(node.then_statement))
        if_vertex.add_kid(body_vertex)
    if node.else_statement:
      else_body = N(TYPES.ELSE)
      if isinstance(node.else_statement, jtree.BlockStatement) and node.else_statement.statements:
        for stmt in node.else_statement.statements:
          else_body.add_kid(self.visit(stmt, meta))
      else:
        else_body.add_kid(self.visit(node.else_statement, meta))
      if_vertex.add_kid(else_body)
    return if_vertex

  def visit_BlockStatement(self, node, meta):
    body = N(TYPES.BODY)
    if node.statements:
      for stmt in node.statements:
        body.add_kid(self.visit(stmt, meta))
    return body

  def visit_BreakStatement(self, node, meta):
    return N(TYPES.BREAK)

  def visit_ContinueStatement(self, node, meta):
    return N(TYPES.CONTINUE)

  def visit_ReturnStatement(self, node, meta):
    return_vertex = N(TYPES.RETURN)
    if node.expression:
      return_vertex.add_kid(self.visit(node.expression, meta))
    return return_vertex

  def visit_ForStatement(self, node, meta):
    loop_vertex = N(TYPES.LOOP)
    loop_vertex.add_kid(N(TYPES.LOOP_CONDITION))
    if node.body:
      if isinstance(node.body, jtree.BlockStatement):
        loop_vertex.add_kid(self.visit(node.body))
      else:
        body_vertex = N(TYPES.BODY)
        body_vertex.add_kid(self.visit(node.body))
        loop_vertex.add_kid(body_vertex)
    return loop_vertex

  def visit_WhileStatement(self, node, meta):
    return self.visit_ForStatement(node, meta)

  def visit_DoStatement(self, node, meta):
    return self.visit_ForStatement(node, meta)

  def visit_ForControl(self, node, meta):
    return N(TYPES.LOOP_CONDITION)

  def visit_EnhancedForControl(self, node, meta):
    return N(TYPES.LOOP_CONDITION)

  def visit_AssertStatement(self, node, meta):
    assert_vertex = N(TYPES.ASSERT)
    if node.condition:
      assert_vertex.add_kid(self.visit(node.condition, meta))
    if node.value:
      assert_vertex.add_kid(self.visit(node.value, meta))
    return assert_vertex

  def visit_ThrowStatement(self, node, meta):
    return N(TYPES.RAISE)

  def visit_TryStatement(self, node, meta):
    try_node = N(TYPES.TRY)
    if node.block:
      body_node = N(TYPES.BODY)
      for stmt in node.block:
        body_node.add_kid(self.visit(stmt, meta))
      try_node.add_kid(body_node)
    if node.catches:
      for catch in node.catches:
        try_node.add_kid(self.visit(catch, meta))
    if node.finally_block:
      finally_node = N(TYPES.FINALLY)
      for stmt in node.finally_block:
        finally_node.add_kid(self.visit(stmt, meta))
      try_node.add_kid(finally_node)
    return try_node

  def visit_CatchClause(self, node, meta):
    except_vertex = N(TYPES.EXCEPT)
    if node.parameter:
      except_vertex.add_kid(N(TYPES.VARIABLE))
    body = N(TYPES.BODY)
    if node.block:
      for stmt in node.block:
        body.add_kid(self.visit(stmt, meta))
    except_vertex.add_kid(body)
    return except_vertex

  def visit_SynchronizedStatement(self, node, meta):
    sync_vertex = N(TYPES.SYNCHRONIZED)
    if node.block:
      body_node = N(TYPES.BODY)
      for stmt in node.block:
        body_node.add_kid(self.visit(stmt, meta))
      sync_vertex.add_kid(body_node)
    return sync_vertex

  """
  End Statements
  """


def get_java_tree(source_code, wrap_class=False):
  """
  Generate Java Tree
  :param source_code: Java Source code
  :param wrap_class: Wrap code in a temporary class
  :return: an instance of mos.search.tree.common.Node
  """
  visitor = TreeVisitor(source_code, wrap_class=wrap_class)
  return visitor.parse()


def parse_file(file_path, override_output=False, wrap_class=True):
  try:
    contents = cache.read_file(file_path)
    visitor = TreeVisitor(contents, wrap_class=wrap_class)
    vertex = visitor.parse()
    parsed = vertex.to_bson()
    if override_output:
      cache.write_file(file_path, str(parsed))
  except Exception:
    if override_output:
      error_content = "Error: \n%s" % traceback.format_exc()
      cache.write_file(file_path, error_content)


def parse_content(code):
  visitor = TreeVisitor(code, wrap_class=True)
  vertex = visitor.parse()
  return vertex.to_bson()


def test():
  file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/java/filterOutOdds.txt"
  contents = cache.read_file(file_path)
  visitor = TreeVisitor(contents, wrap_class=True)
  # print(visitor.tree)
  pprint(visitor.tree)
  vertex = visitor.parse()
  vertex.to_png("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_paper/java/tmp.png")
  exit()
  print(vertex.to_bson())
  # print(vertex)
  # img_path = "%s.png" % file_path.rsplit(".")[0]
  # vertex.to_png(img_path)


def _main():
  args = sys.argv
  message = """
    python mos/search/tree/java_tree.py <path to java source code> <? override output>
    """
  if len(args) < 2:
    print("Error!")
    print(message)
    exit(0)
  file_path = args[1]
  override_output = len(args) > 2 and args[2].lower().strip() == "true"
  parse_file(file_path, override_output, wrap_class=True)


if __name__ == "__main__":
  # test()
  _main()
