import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

import ast
import textwrap
from analysis.blocks import types
from pytype import config
from pytype.tools.annotate_ast import annotate_ast
from pytype.pytd import pytd

import properties

__author__ = "COSAL"

PYTHON_VERSION = (2, 7)


def clone_data_types(data_types):
    return [dt.clone() for dt in data_types]


def get_data_types_from_value(val):
    module, class_name = type(val).__module__, type(val).__name__
    if types.PrimitiveType.is_primitive(class_name, module):
        return [types.PrimitiveType(class_name)]
    elif module == "__builtin__" and class_name == "list":
        list_types = get_data_types_from_value(val[0])
        var_types = []
        for l_t in list_types:
            var_type = types.ListType()
            var_type.types = [l_t]
            var_types.append(var_type)
        return var_types
    else:
        raise RuntimeError("Unsupported type '%s.%s' and value '%s'" % (module, class_name, str(val)))


def load_default_types():
    if properties.CONFIG.get_default_values() is not None:
        default_types = []
        for val in properties.CONFIG.get_default_values():
            default_types += get_data_types_from_value(val)
        if default_types:
            return default_types
    return None


def get_data_types(py_class_type):
    py_class_type_type = type(py_class_type)
    if py_class_type is None:
        return None
    if py_class_type_type == pytd.AnythingType:
        return load_default_types()
    elif py_class_type_type == pytd.NothingType:
        return None
    elif py_class_type_type == pytd.NamedType:
        raise RuntimeError("@COSAL: Unsupported class type: %s" % py_class_type)
    elif py_class_type_type == pytd.ClassType:
        splits = str(py_class_type).rsplit(".")
        name = splits[-1]
        module = splits[0] if len(splits) == 2 else None
        if types.PrimitiveType.is_primitive(name, module):
            var_type = types.PrimitiveType(name)
        elif types.FileType.is_file_type(name, module):
            var_type = types.FileType(name, module)
        else:
            try:
                constructor = py_class_type.cls.Lookup("__init__")
            except KeyError:
                return None
            if not constructor:
                return None
            # Class constructor
            var_type = types.BaseType(name, module)
        return [var_type]
    elif py_class_type_type == pytd.TupleType:
        if not py_class_type.parameters:
            return None
        var_types = [types.TupleType()]
        for tup_param_type in py_class_type.parameters:
            tup_param_var_types = get_data_types(tup_param_type)
            if not tup_param_var_types:
                return None
            cloned_var_types = clone_data_types(var_types)
            new_var_types = []
            for tup_param_var_type in tup_param_var_types:
                if tup_param_var_type and tup_param_var_type.is_valid:
                    for var_type in cloned_var_types:
                        var_type.types.append(tup_param_var_type)
                        new_var_types.append(var_type)
            if not new_var_types:
                return None
            var_types = new_var_types
        return var_types
    elif py_class_type_type == pytd.GenericType:
        base_type = py_class_type.base_type
        if not py_class_type.parameters:
            return None
        if str(base_type.name) == "__builtin__.list":
            list_types = get_data_types(py_class_type.parameters[0])
            if not list_types:
                return None
            var_types = []
            for l_t in list_types:
                var_type = types.ListType()
                var_type.types = [l_t]
                var_types.append(var_type)
            return var_types
        elif str(base_type.name) == "__builtin__.dict":
            var_type = types.DictType()
            key_types = get_data_types(py_class_type.parameters[0])
            if not key_types:
                return None
            var_type.key_types = key_types if isinstance(key_types, list) else [key_types]
            val_types = get_data_types(py_class_type.parameters[1])
            if not val_types:
                return None
            var_type.val_types = val_types if isinstance(val_types, list) else [val_types]
            return [var_type]
        elif str(base_type.name) == "__builtin__.set":
            var_types = []
            set_types = get_data_types(py_class_type.parameters[0])
            if not set_types:
                return None
            for s_t in set_types:
                var_type = types.SetType()
                var_type.types = [s_t]
                var_types.append(var_type)
            return var_types
        else:
            # TODO May need to handle case for custom classes here
            splits = str(base_type).rsplit(".")
            name = splits[-1]
            module = splits[0] if len(splits) == 2 else None
            var_type = types.SystemType(name, module)
            if not py_class_type.parameters:
                return None
            parameters = []
            for param_type in py_class_type.parameters:
                var_type_parameter = get_data_types(param_type)
                if var_type_parameter:
                    parameters.append(set(var_type_parameter))
            if not parameters:
                return None
            var_type.parameters = parameters
            return [var_type]
    elif py_class_type_type == pytd.UnionType:
        var_types = []
        for union_element in py_class_type.type_list:
            union_element_var_types = get_data_types(union_element)
            if not union_element_var_types:
                return None
            var_types += union_element_var_types
        return var_types
    else:
        # TODO: Implement rest
        raise RuntimeError("@COSAL: Unsupported class type: %s" % str(py_class_type))


def annotate(src):
    source = textwrap.dedent(src.lstrip('\n'))
    ast_factory = lambda unused_options: ast
    pytype_options = config.Options.create(python_version=PYTHON_VERSION)
    return annotate_ast.annotate_source(source, ast_factory, pytype_options)


def test_annotation():
    src = """
    def sum(x):
        x = 5 
        x += 2
        y = x[:5]
        return x ** 2
    
    """
    source = textwrap.dedent(src.lstrip('\n'))
    ast_factory = lambda unused_options: ast
    pytype_options = config.Options.create(python_version=PYTHON_VERSION)
    # annotate_ast.infer_types(source, pytype_options)
    print_node(annotate_ast.annotate_source(source, ast_factory, pytype_options))


def print_node(node, annotate_fields=True, include_attributes=True):
    print(dump(node, annotate_fields, include_attributes))


def dump(node, annotate_fields=True, include_attributes=True):
    def _format(node):
        if isinstance(node, ast.AST):
            fields = [(a, _format(b)) for a, b in ast.iter_fields(node)]
            if isinstance(node, ast.Name):
                fields.append(("resolved_type", getattr(node, "resolved_type", None)))
                fields.append(("resolved_annotation", getattr(node, "resolved_annotation", None)))
            rv = '%s(%s' % (node.__class__.__name__, ', '.join(
                ('%s=%s' % field for field in fields)
                if annotate_fields else
                (b for a, b in fields)
            ))
            if include_attributes and node._attributes:
                rv += fields and ', ' or ' '
                rv += ', '.join('%s=%s' % (a, _format(getattr(node, a)))
                                for a in node._attributes)
            return rv + ')'
        elif isinstance(node, list):
            return '[%s]' % ', '.join(_format(x) for x in node)
        return repr(node)
    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    return _format(node)


if __name__ == "__main__":
    # test_annotation()
    print(get_data_types_from_value("Hello"))