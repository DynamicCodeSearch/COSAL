import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import contextlib
from javalang.tree import Node


def _is_sub_node(node):
  return not isinstance(node, Node)


def _is_leaf(node):
  if isinstance(node, Node) and isinstance(node.attrs, list):
    for field in node.attrs:
      attr = getattr(node, field)
      if _is_sub_node(attr):
        return False
      elif isinstance(attr, (list, tuple)):
        for val in attr:
          if _is_sub_node(val):
            return False
  else:
    return True


def _attrs(n):
  return n.attrs


def _leaf(node):
  if isinstance(node, Node):
    return '{}({})'.format(
      type(node).__name__,
      ', '.join(
        '{}={}'.format(
          field,
          _leaf(getattr(node, field)),
        )
        for field in _attrs(node)
      ),
    )
  elif isinstance(node, list):
    return '[{}]'.format(
      ', '.join(_leaf(x) for x in node),
    )
  else:
    return repr(node)


def pformat(node, indent='    ', _indent=0):
  if node is None:  # pragma: no cover (py35+ unpacking in literals)
    return repr(node)
  elif isinstance(node, str):  # pragma: no cover (ast27 typed-ast args)
    return repr(node)
  elif _is_leaf(node):
    return _leaf(node)
  else:
    class state:
      indent = _indent

    @contextlib.contextmanager
    def indented():
      state.indent += 1
      yield
      state.indent -= 1

    def indentstr():
      return state.indent * indent

    def _pformat(el, _indent=0):
      return pformat(
        el, indent=indent,
        _indent=_indent,
      )

    out = type(node).__name__ + '(\n'
    with indented():
      for field in _attrs(node):
        attr = getattr(node, field)
        if attr is []:
          representation = '[]'
        elif (
                isinstance(attr, list) and
                len(attr) == 1 and
                isinstance(attr[0], Node) and
                _is_leaf(attr[0])
        ):
          representation = '[{}]'.format(_pformat(attr[0]))
        elif isinstance(attr, list):
          representation = '[\n'
          with indented():
            for el in attr:
              representation += '{}{},\n'.format(
                indentstr(), _pformat(el, state.indent),
              )
          representation += indentstr() + ']'
        elif isinstance(attr, Node):
          representation = _pformat(attr, state.indent)
        else:
          representation = repr(attr)
        out += '{}{}={},\n'.format(indentstr(), field, representation)
    out += indentstr() + ')'
    return out


def pprint(*args, **kwargs):
  print(pformat(*args, **kwargs))

