import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


import ast
import astor
import astpretty
import asttokens
import keyword
import textwrap
import tokenize

from io import StringIO


__KEYWORDS = None
IGNORE_TERMS = {"init", "args", "kwargs", "kwds", "self"}


def get_keywords():
  global __KEYWORDS, IGNORE_TERMS
  if __KEYWORDS is None:
    __KEYWORDS = set(keyword.kwlist).union(IGNORE_TERMS)
  return __KEYWORDS


def get_future_import_str():
  return "from __future__ import print_function"


def parse(source_code, use_ast_tokens=False):
  try:
    tree = ast.parse(source_code)
  except SyntaxError:
    source_code = "%s\n%s" % (get_future_import_str(), source_code)
    try:
      tree = ast.parse(source_code)
    except SyntaxError as e:
      return None
  if use_ast_tokens:
    ast_tokenized = asttokens.ASTTokens(source_code, tree=tree)
    ast_tokenized.tree.asttokens_obj = ast_tokenized
    return ast_tokenized.tree
  return tree


def parse_function(source_code, use_ast_tokens=False):
  """
  Convert source code to node
  :param source_code: Source code as string
  :param use_ast_tokens: If true use `asttokens` library to parse code.
  :return: Return instance of `ast.FunctionDef`
  """
  parsed = parse(source_code, use_ast_tokens=use_ast_tokens)
  if parsed and len(parsed.body) > 0:
    for node in parsed.body:
      if isinstance(node, ast.FunctionDef):
        return node
  return None


def update_function_name(func_node, name):
  """
  Update name of function AST
  :param func_node: instance of `ast.FunctionDef`
  :param name: New name of function
  :return: New function node with new name
  """
  return ast.FunctionDef(
    name=name,
    args=func_node.args,
    body=func_node.body,
    decorator_list=func_node.decorator_list if hasattr(func_node, 'decorator_list') else []
  )


def convert_ast_to_code(node, asttokens_obj=None):
  """
  Convert ast to source code
  :param node: Instance of `ast.Node`
  :param asttokens_obj: Instance of `asttokens.ASTTokens`
  :return: Instance of source code
  """
  if asttokens_obj:
    return asttokens_obj.get_text(node)
  return astor.to_source(node)


def get_func_node(func_obj, use_ast_tokens=False):
  """
  Convert function string as `ast.FunctionDef` if its not and instance
  :param func_obj: Instance of `ast.FunctionDef` or a string
  :param use_ast_tokens: If true use `asttokens` library to parse code.
  :return: Instance of `ast.FunctionDef`
  """
  if type(func_obj) == ast.FunctionDef:
    return func_obj
  elif type(func_obj) in [str, unicode]:
    return parse_function(func_obj, use_ast_tokens=use_ast_tokens)
  else:
    raise RuntimeError("@COSAL: Unsupported function type for function '%s'!!" % type(func_obj).__name__)


def get_function_body_as_str(func_obj, as_lst=False, use_ast_tokens=False):
  """
  Get body of function as str
  :param func_obj: Instance of `ast.FunctionDef` or a string
  :param as_lst: True / False
  :param use_ast_tokens: If true use `asttokens` library to parse code.
  :return: Body of function as list or str
  """
  func_node = get_func_node(func_obj, use_ast_tokens=use_ast_tokens)
  if not func_node or not func_node.body:
    return None
  body = []
  for stmt in func_node.body:
    body.append(convert_ast_to_code(stmt))
  if as_lst:
    return body
  return "".join(body).strip()


def get_func_name(func_obj, use_ast_tokens=False):
  """
  Get name of function
  :param func_obj: Instance of `ast.FunctionDef` or a string
  :param use_ast_tokens: If true use `asttokens` library to parse code.
  :return: name of the function
  """
  func_node = get_func_node(func_obj, use_ast_tokens=use_ast_tokens)
  if not func_node:
    return None
  return func_node.name


def get_arg_names(func_obj, use_ast_tokens=False):
  """
  Get names of function arguments
  :param func_obj: Instance of `ast.FunctionDef` or a string
  :param use_ast_tokens: If true use `asttokens` library to parse code.
  :return: List of names of args
  """
  func_node = get_func_node(func_obj)
  if func_node.args and func_node.args.args:
    return [arg.id for arg in func_node.args.args]
  return None


def pretty_print(node, indent=' '*2, show_offsets=False):
  """
  Pretty print node
  :param node: Instance of `ast.Node`
  :param indent: Number of spaces to indent
  :param show_offsets: Show offsets. Boolean
  :return:
  """
  astpretty.pprint(node, indent=indent, show_offsets=show_offsets)


def parse_print(node, annotate_fields=True, include_attributes=True):
  """
  Print node
  :param node: instance of `ast.Node`
  :param annotate_fields: If true, prints fields
  :param include_attributes:
  """
  print(ast.dump(node, annotate_fields, include_attributes))


def has_return_statement(func_obj):
  """
  Check if the function has a return statement
  :param func_obj: Instance of function object
  :return: True / False
  """
  func_node = get_func_node(func_obj)
  return any(isinstance(node, ast.Return) for node in ast.walk(func_node))


def create_function(name, args, body):
  """
  Create a function node
  :param name: Name of the functions
  :param args: Arguments of the function
  :param body: Body of the function
  :return: Instance of `ast.FunctionDef`
  """
  return ast.FunctionDef(name=name, args=args, body=body, decorator_list=[])


def create_return_statement(var_name=None):
  """
  Create a return statement node
  :param var_name: Name of variable to be returned
  :return: Instance of `ast.Return`
  """
  if var_name:
    return ast.Return(value=ast.Name(id=var_name))
  else:
    return ast.Return()


def remove_comments_and_docstrings(source):
  """
  Returns 'source' minus comments and docstrings.
  """
  io_obj = StringIO(source.encode("utf-8"))
  out = ""
  prev_toktype = tokenize.INDENT
  last_lineno = -1
  last_col = 0
  for tok in tokenize.generate_tokens(io_obj.readline):
    token_type = tok[0]
    token_string = tok[1]
    start_line, start_col = tok[2]
    end_line, end_col = tok[3]
    ltext = tok[4]
    # The following two conditionals preserve indentation.
    # This is necessary because we' re not using tokenize.untokenize()
    # (because it spits out code with copious amounts of oddly-placed
    # whitespace).
    if start_line > last_lineno:
      last_col = 0
    if start_col > last_col:
      out += (" " * (start_col - last_col))
    # Remove comments:
    if token_type == tokenize.COMMENT:
      pass
    # This series of conditionals removes docstrings:
    elif token_type == tokenize.STRING:
      if prev_toktype != tokenize.INDENT:
        # This is likely a docstring; double-check we're not inside an operator:
        if prev_toktype != tokenize.NEWLINE:
          # Note regarding NEWLINE vs NL: The tokenize module
          # differentiates between newlines that start a new statement
          # and newlines inside of operators such as parens, brackes,
          # and curly braces.  Newlines inside of operators are
          # NEWLINE and newlines that start new code are NL.
          # Catch whole-module docstrings:
          if start_col > 0:
            # Unlabelled indentation means we're inside an operator
            out += token_string
          # Note regarding the INDENT token: The tokenize module does
          # not label indentation inside of an operator (parens,
          # brackets, and curly braces) as actual indentation.
          # For example:
          # def foo():
          #     "The spaces before this docstring are tokenize.INDENT"
          #     test = [
          #         "The spaces before this string do not get a token"
          #     ]
    else:
      out += token_string
    prev_toktype = token_type
    last_col = end_col
    last_lineno = end_line
  return out


def get_comments(source_code):
  """
  :param source_code: Source code as text
  :return: Comments in source code as a list
  """
  io_obj = StringIO(source_code.encode("utf-8"))
  comments = []
  for tok in tokenize.generate_tokens(io_obj.readline):
    token_type = tok[0]
    token_string = tok[1]
    if token_type == tokenize.COMMENT:
      comments.append(token_string.replace("#", " ").strip())
  return comments


def get_docstring(node):
  """
  Return the docstring for the given node or None if no docstring can be found.
  :param node: Instance of java node
  :return: Doc String
  """
  try:
    return ast.get_docstring(node)
  except TypeError:
    return None


def format_code(source_code):
  """
  Format source code
  :param source_code: Source code as str
  :return: Formatted source code as str
  """
  return textwrap.dedent(source_code)