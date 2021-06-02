import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils import cache
import properties


FILE_INPUT_TYPE = "__SLACC_FILE_INPUT__"
FILE_OUTPUT_TYPE = "__SLACC_FILE_OUTPUT__"
_PY_TEMP_FOLDER = "_py_temp_files"
_GEN_FILE_PREFIX = os.path.join(properties.CONFIG.CODE_HOME, _PY_TEMP_FOLDER)


def convert_to_file_input(file_content, file_type, func_name, arg_index):
  """
  Convert content to file input
  :param file_content: Contents of file
  :param file_type: Type of file - eg. __builin__.file
  :param func_name: Name of the function
  :param arg_index: Index of file
  :return: File Object
  """
  file_path = os.path.join(_GEN_FILE_PREFIX, "%s_%d.txt" % (func_name, arg_index))
  cache.write_file(file_path, file_content)
  if file_type == "__builtin__.file":
    f = open(file_path, "r+")
    return f
  raise RuntimeError("@COSAL: Unsupported file type '%s'" % file_type)


def convert_to_file_output(file_obj):
  """
  Convert instance of file output to text
  :param file_obj: Instance of file
  :return: Contents of file_obj
  """
  ft = type(file_obj)
  file_type = "%s.%s" % (ft.__module__, ft.__name__)
  if file_type == "__builtin__.file":
    if not file_obj.closed:
      file_obj.close()
    try:
      return cache.read_file(file_obj.name)
    except Exception:
      return None
  raise RuntimeError("@COSAL: Unsupported file type '%s'" % file_type)


def delete_all_input_temp_files():
  """
  Delete all temporary input files
  """
  cache.delete_folder(_GEN_FILE_PREFIX)


def delete_input_temp_files(func_id):
  """
  Delete all temporary input files for function
  :param func_id: Id of function
  """
  cache.delete_files_with_pattern(_GEN_FILE_PREFIX, "%s_*.txt" % func_id)


def _test():
  cache.delete_files_with_pattern(_GEN_FILE_PREFIX, "4473835728_*.txt")


if __name__ == "__main__":
  _test()
