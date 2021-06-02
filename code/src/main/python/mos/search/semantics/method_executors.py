import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis import arguments as arg_analysis
from analysis.blocks import block_utils
from analysis.blocks.method import GeneratedFunction
from analysis.helpers import helper, ast_utils, execution_utils, parse_utils
from analysis.parsers import parser
from mos.search_store.code_store import CodeStore, MetaStore, ExecStore
from utils import cache, logger, lib
import properties

import traceback

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class ExecutorVisitor(parser.Traveller):
  def __init__(self, file_path):
    parser.Traveller.__init__(self)
    parent_folder = cache.get_parent_folder(file_path)
    self.file_path = file_path
    self.dataset = properties.CONFIG.get_dataset()
    self.variable_visitor = arg_analysis.parse_file_via_inference(file_path, properties.CONFIG.get_dataset(), force_fetch=False)
    self.methods = []
    self.headers = []
    # Meta
    self._variable_map = None
    # print(self.variable_visitor.scope_variable_map.keys())

  def parse(self):
    self.visit(self.variable_visitor.tree)
    return self.methods

  def visit_Import(self, node, meta):
    self.headers.append(ast_utils.convert_ast_to_code(node))

  def visit_ImportFrom(self, node, meta):
    self.headers.append(ast_utils.convert_ast_to_code(node))

  def visit_ClassDef(self, node, meta):
    class_name = node.name
    meta = {"class_name": class_name}
    super(ExecutorVisitor, self).generic_visit(node, meta)

  @staticmethod
  def make_code_block_key(func_ast, class_name):
    func_name = func_ast.name
    args = [arg.id for arg in func_ast.args.args]
    if func_ast.args.vararg:
      args.append(func_ast.args.vararg)
    if func_ast.args.kwarg:
      args.append(func_ast.args.kwarg)
    args = ",".join(args)
    key = "%s(%s)" % (func_name, args)
    if class_name:
      key = "%s.%s" % (class_name, key)
    return key

  def visit_FunctionDef(self, node, meta):
    if node.name != "__init__":
      generated_function = GeneratedFunction()
      generated_function.source_code_function_name = node.name
      class_name = meta["class_name"] if meta and "class_name" in meta else None
      generated_function.name = helper.generate_function_name()
      generated_function.source_code_class_name = class_name
      generated_function.original_function_name = self.make_code_block_key(node, class_name)
      generated_function.body = ast_utils.convert_ast_to_code(node)
      generated_function.source_file = self.file_path
      generated_function.is_whole_method = True
      generated_function.is_static_method = class_name is None
      generated_function._ast = node
      self.methods.append(generated_function)
    super(ExecutorVisitor, self).generic_visit(node, meta)

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
    method_meta = gen_func.get_method_meta()
    if method_meta is not None:
      return method_meta
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
    method_meta = {
      "args": variables,
      "has_return_statement": has_return_stmt,
      "returns": variables,
      "is_valid": is_valid
    }
    gen_func.set_method_meta(method_meta)
    return method_meta

  def get_headers(self, as_str=True):
    if as_str:
      return "\n".join(self.headers)
    else:
      return self.headers


def get_code_store():
  return CodeStore()


def get_meta_store():
  return MetaStore()


def get_exec_store():
  return ExecStore()


class MethodExecutors(lib.O):
  def __init__(self, file_path, **kwargs):
    lib.O.__init__(self, **kwargs)
    self.adapter = ExecutorVisitor(file_path)
    self.base_functions = None

  def get_base_functions(self):
    if self.base_functions is not None:
      return self.base_functions
    self.base_functions = []
    file_path = self.adapter.file_path
    parsed_methods = self.adapter.parse()
    for parsed_method in parsed_methods:
      method_meta = self.adapter.get_meta_for_method(parsed_method)
      is_from_class = parsed_method.source_code_class_name is not None
      if is_from_class or not method_meta["is_valid"] or not method_meta["has_return_statement"] or len(method_meta["args"]) > 3:
        continue
      self.base_functions.append(parsed_method)
    return self.base_functions

  def create_module(self):
    funcs = self.get_base_functions()
    file_path = self.adapter.file_path
    temp_file = os.path.join(properties.PYTHON_PROJECTS_HOME, "%s.py" % helper.generate_py_temp_name())
    try:
      sys.path.append(properties.PYTHON_PROJECTS_HOME)
      headers = "\n".join(["import sys",
                           "sys.path.append('%s')" % properties.PYTHON_PROJECTS_HOME,
                           self.adapter.get_headers(as_str=True)])
      content = "\n\n".join([headers] + [func.body for func in funcs])
      cache.write_file(temp_file, content)
      validity = helper.is_valid_file(temp_file)
      if not validity:
        return None
      python_name = temp_file.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0].replace(os.path.sep, ".")
      module = __import__(python_name)
      return module
    except Exception as e:
      LOGGER.info("@COSAL: Error - %s" % e.message)
    finally:
      cache.delete_file(temp_file)
      sys.path.remove(properties.PYTHON_PROJECTS_HOME)

  def expand_function(self, func):
    method_meta = self.adapter.get_meta_for_method(func)
    expanded_argsets = parse_utils.expand_arguments(method_meta['args'])
    generated_functions = []
    if not expanded_argsets:
      return generated_functions
    for argset in expanded_argsets:
      arg_dict = {}
      for index, arg in enumerate(sorted(argset, key=lambda x: x.name)):
        arg.index = index
        arg_dict[arg.name] = arg.to_specific_parameter()
      generated_func = func.clone()
      generated_func.name = helper.generate_random_string()
      generated_func.parameters = arg_dict
      perm_funcs = MethodExecutors.permutate_function(generated_func)
      if not perm_funcs:
        continue
      generated_functions += perm_funcs
    return generated_functions

  @staticmethod
  def permutate_function(func):
    arg_keys = execution_utils.get_function_arg_and_key(func)
    grouped_arg_keys = execution_utils.group_arg_and_key(arg_keys)
    if execution_utils.has_too_many_arguments(grouped_arg_keys):
      return None
    function_input_key = execution_utils.get_function_args_key(grouped_arg_keys)
    if not function_input_key:
      return None
    func.input_key = function_input_key
    args_permutations = execution_utils.permutate_args_and_key(grouped_arg_keys)
    if not args_permutations:
      return None
    existing_perms = set()
    permutated_funcs = []
    for i, args_permutation in enumerate(args_permutations):
      serialized_arg_permutation = str(args_permutation)
      if serialized_arg_permutation in existing_perms:
        continue
      existing_perms.add(serialized_arg_permutation)
      cloned = func.clone()
      cloned.name = helper.generate_random_string()
      cloned.args_permutation = args_permutation
      permutated_funcs.append(cloned)
    return permutated_funcs

  def generate_functions(self):
    mod = self.create_module()
    generated_functions = []
    for func in self.get_base_functions():
      func_name = func.source_code_function_name
      func.set_func_obj(getattr(mod, func_name, None))
      expanded_funcs = self.expand_function(func)
      generated_functions += expanded_funcs
    return generated_functions


def execute_function(func):
  try:
    func_obj = func.get_func_obj()
    args = execution_utils.get_function_args(func)
    if not args:
      LOGGER.info("Failed to fetch ARGS for %s" % str(func_obj))
      return
    results = []
    for arg_index, arg in enumerate(args):
      exec_results = execution_utils.execute_function(func_obj, arg)
      exec_results["return"] = block_utils.format_value_as_json(exec_results["return"], func, arg_index)
      results.append(exec_results)
    exec_store = get_exec_store()
    exec_store.save_class_function_meta(func.to_bson_camel_case())
    exec_store.update_class_function_result({
      "name": func.name,
      "inputKey": func.input_key,
      "outputs": results,
      "originalFunctionName": func.original_function_name,
      "filePath": cache.get_repo_local_path(func.source_file)
    })
  except Exception as e:
    LOGGER.info("Error while executing '%s' ..." % func.original_function_name)
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60


def process_py_file(file_path):
  if get_meta_store().is_py_file_processed(file_path):
    LOGGER.info("Already processed file '%s'. Moving on!", cache.get_repo_local_path(file_path))
    return
  get_meta_store().update_py_file_processed(file_path)
  exec_store = get_exec_store()
  exec_store.delete_class_function_meta(file_path)
  exec_store.delete_class_function_result(file_path)
  try:
    executor = MethodExecutors(file_path)
    funcs = executor.generate_functions()
    if len(funcs) > 0:
      LOGGER.info("Numger of functions to process: %d ..." % len(funcs))
      for func in funcs:
        execute_function(func)
  except Exception as e:
    LOGGER.info("Error while processing file '%s' ..." % cache.get_repo_local_path(file_path))



def get_py_files():
  py_files = cache.list_files(properties.PYTHON_PROJECTS_HOME, check_nest=True, is_absolute=True, ignores=["__init__.py"])
  for file_index, py_file in enumerate(py_files):
    LOGGER.info("Processing file '%s'. %d/%d .... " % (cache.get_repo_local_path(py_file), file_index + 1, len(py_files)))
    process_py_file(py_file)


def _test():
  # file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/atcoder/src/main/python/C4/P3/1595563.py"
  file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/atcoder/src/main/python/C52/P2/1101721.py"
  process_py_file(file_path)


if __name__ == "__main__":
  get_py_files()
  # _test()
