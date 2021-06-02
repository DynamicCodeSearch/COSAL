import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from analysis.parsers import arg_parser
from analysis.tracer import Tracer
from analysis.helpers import helper
from analysis.blocks import block_utils
from store import mongo_store
from utils import logger
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


FORCE_FETCH = False


def get_data_store(dataset):
  if properties.STORE == "mongo":
    return mongo_store.PyFileMetaStore(dataset)
  raise RuntimeError("Currently supports only mongo store. Not supported for '%s'" % properties.STORE)


def get_class_store():
  if properties.STORE == "mongo":
    return mongo_store.PyClassStore()
  raise RuntimeError("Currently supports only mongo store. Not supported for '%s'" % properties.STORE)


def parse_file_for_args(file_path, dataset, main_function_name="_main", force_fetch=FORCE_FETCH):
  store = get_data_store(dataset)
  existing = store.load_meta(file_path)
  if not force_fetch and existing:
    LOGGER.info("Fetching existing metadata for %s" % file_path)
    return arg_parser.VariableVisitor.from_bson(existing)
  LOGGER.info("Generating metadata for %s" % file_path)
  variable_visitor = arg_parser.VariableVisitor(file_path).parse()
  tracer = Tracer(variable_visitor, file_path, ['parse_file_for_args'])
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  module = helper.import_file(file_path)
  main_function = getattr(module, main_function_name)
  sys.settrace(tracer.trace_calls)
  main_function()
  sys.settrace(None)
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)
  store.save_meta(variable_visitor.to_bson())
  # cache.store_json(variable_visitor.to_bson(), "temp_3.json")
  # visitor = arg_parser.VariableVisitor.from_bson(cache.load_json("temp_3.json"))
  # cache.store_json(visitor.to_bson(), "temp_4.json")
  return variable_visitor


def parse_file_via_inference(file_path, dataset, force_fetch=FORCE_FETCH):
  store = get_data_store(dataset)
  existing = store.load_meta(file_path)
  if not force_fetch and existing:
    LOGGER.info("Fetching existing metadata for %s" % file_path)
    return arg_parser.VariableVisitor.from_bson(existing)
  # LOGGER.info("Generating metadata for %s" % file_path)
  variable_visitor = arg_parser.VariableVisitor(file_path).parse_pytype()
  py_class_store = get_class_store()
  # Saving custom classes
  custom_classes = variable_visitor.update_classes()
  if custom_classes:
    for custom_class in custom_classes:
      py_class_store.save_custom_class(custom_class)
  # Saving system classes
  system_classes = variable_visitor.get_system_classes()
  if system_classes:
    for system_class in system_classes:
      existing_system_class = py_class_store.load_system_class(system_class.module, system_class.name)
      if existing_system_class:
        existing_system_class = block_utils.from_SystemType_bson(existing_system_class)
        for i, i_parameters in enumerate(existing_system_class.parameters):
          system_class.parameters[i].update(i_parameters)
      py_class_store.save_system_class(system_class)
  return variable_visitor


if __name__ == "__main__":
  # parse_file_for_args("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/dummy.py", properties.CODE_JAM)
  parse_file_for_args("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/dennislissov/A.py", properties.CODE_JAM)
