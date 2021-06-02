import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import asttokens

from analysis import arguments as arg_analysis
from analysis.helpers import helper, ast_utils
from analysis.parsers import parser
from analysis.blocks.method import GeneratedFunction
from utils import cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class MethodVisitor(parser.Traveller):
  def __init__(self, file_path, dataset):
      parser.Traveller.__init__(self)
      parent_folder = cache.get_parent_folder(file_path)
      self.file_path = file_path
      self.dataset = dataset
      self.generated_file_path = os.path.join(parent_folder, "%s.py" % helper.generate_py_file_name())
      self.methods = []

  def parse(self):
      source_code = cache.read_file(self.file_path)
      ast_tokenized = asttokens.ASTTokens(source_code, parse=True)
      self.visit(ast_tokenized.tree, None)
      return self.methods

  def visit_ClassDef(self, node, meta):
      class_name = node.name
      meta = {"class_name": class_name}
      super(MethodVisitor, self).generic_visit(node, meta)

  def visit_FunctionDef(self, node, meta):
      generated_function = GeneratedFunction()
      generated_function.source_code_function_name = node.name
      class_name = meta["class_name"] if meta and "class_name" in meta else None
      generated_function.name = helper.generate_function_name()
      generated_function.source_code_class_name = class_name
      generated_function.body = ast_utils.convert_ast_to_code(node)
      generated_function.source_file = self.file_path
      generated_function.is_whole_method = True
      generated_function.generated_file = self.generated_file_path
      self.methods.append(generated_function)
      super(MethodVisitor, self).generic_visit(node, meta)


class WholeMethodVisitor(parser.Traveller):
    def __init__(self, file_path, dataset):
        parser.Traveller.__init__(self)
        parent_folder = cache.get_parent_folder(file_path)
        self.file_path = file_path
        self.dataset = dataset
        self.variable_visitor = arg_analysis.parse_file_via_inference(file_path, dataset, force_fetch=False)
        self.methods = []
        # Meta
        self._variable_map = None
        # print(self.variable_visitor.scope_variable_map.keys())

    def parse(self):
        self.visit(self.variable_visitor.tree)
        return self.methods

    def visit_FunctionDef(self, node, meta):
        generated_function = GeneratedFunction()
        generated_function.source_code_function_name = node.name
        class_name = meta["class_name"] if meta and "class_name" in meta else None
        generated_function.name = helper.generate_function_name()
        generated_function.source_code_class_name = class_name
        generated_function.body = ast_utils.convert_ast_to_code(node)
        generated_function.source_file = self.file_path
        generated_function.is_whole_method = True
        generated_function._ast = node
        self.methods.append(generated_function)
        super(WholeMethodVisitor, self).generic_visit(node, meta)

    def get_variable_map(self):
        if self._variable_map is not None:
            return self._variable_map
        self._variable_map = {}
        for scope in self.variable_visitor.scope_variable_map.keys():
            curr_scope = scope
            variables = set()
            while curr_scope:
                for var in self.variable_visitor.scope_variable_map[curr_scope].values():
                    variables.add(var)
                curr_scope = curr_scope.parent
            self._variable_map[str(scope)] = variables
        return self._variable_map

    def get_meta_for_method(self, gen_func):
        arg_names = ast_utils.get_arg_names(gen_func.get_ast())
        scope_name = gen_func.get_scope_name()
        variables = []
        for arg_name in arg_names:
            for var in self.get_variable_map()[scope_name]:
                if var.name == arg_name:
                    variables.append(var)
                    break
        has_return_stmt = ast_utils.has_return_statement(gen_func.get_ast())
        is_valid = len(variables) > 0
        for var in variables:
            if not var.is_valid():
                is_valid = False
                break
        return {
            "args": variables,
            "has_return_statement": has_return_stmt,
            "returns": variables,
            "is_valid": is_valid
        }