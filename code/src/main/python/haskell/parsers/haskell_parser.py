import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import subprocess

from haskell.blocks.haskell_function import HaskellFunction, permutate_function
from utils import cache
from utils.lib import O
import properties


HASKELL_PROJECT_SRC = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell"
HASKELL_SRC_PATH = os.path.join(properties.CONFIG.CODE_HOME, "src", "main", "haskell")
HASKELL_LOADER = "HintLoad.hs"
OUTPUT_PREFIX = "OUTPUT --> "


class HaskellParser(O):
  FUNCS_SEPARATOR = "@@"
  COL_SEPARATOR = ":$$:"

  def __init__(self, repo_home=HASKELL_SRC_PATH, **kwargs):
    O.__init__(self, **kwargs)
    self.repo_home = repo_home

  @staticmethod
  def parse_error_string(error_string):
    return error_string

  @staticmethod
  def parse_functions_string(funcs_string, mod, file_path=None):
    if type(funcs_string) == bytes:
      funcs_string = funcs_string.decode("utf-8")
    if not funcs_string.startswith(OUTPUT_PREFIX):
      return None
    funcs_string = funcs_string[len(OUTPUT_PREFIX):]
    funcs_string_split = funcs_string.split(HaskellParser.FUNCS_SEPARATOR)
    parsed_funcs = []
    for func_string in funcs_string_split:
      haskell_func = HaskellParser.parse_function_string(func_string)
      haskell_func.module = mod
      haskell_func.file_path = file_path
      parsed_funcs.append(haskell_func)
    return parsed_funcs

  @staticmethod
  def parse_function_string(func_string):
    if type(func_string) != str:
      func_string = str(func_string)
    func_string = func_string.strip()
    splits = func_string.split(HaskellParser.COL_SEPARATOR)
    h_function = HaskellFunction()
    h_function.source_code_function_name = splits[0]
    h_function.set_types(splits[1])
    # h_function.types = HaskellFunction.parse_type_string(splits[1])
    return h_function

  def parse_module(self, mod, file_path=None):
    p = subprocess.Popen(['runhaskell', HASKELL_LOADER, "-o", "browse", "-m", mod], cwd=self.repo_home,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if err and not out:
      return HaskellParser.parse_error_string(err)
    elif str(out).startswith("ERROR:"):
      return HaskellParser.parse_error_string(out)
    else:
      return HaskellParser.parse_functions_string(out, mod, file_path=file_path)


def parse(mod, file_path=None):
  """
  :param mod: Path for module
  :return:
  """
  parser = HaskellParser()
  functions_or_error = parser.parse_module(mod, file_path=file_path)
  if not isinstance(functions_or_error, list):
    print("Error: Failed to parse module - %s" % mod)
    return None
  return functions_or_error


def parse_file(file_path):
  local_path = file_path
  if local_path.startswith(HASKELL_PROJECT_SRC):
    local_path = local_path[len(HASKELL_PROJECT_SRC) + len(os.path.sep):]
  if local_path.endswith(".hs"):
    local_path = local_path[:-3]
  mod = local_path.replace(os.path.sep, ".")
  parse(file_path, mod)



def _test_parse():
  parse_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell/Tutorial/Example.hs")
  # functions_or_error = parse("Tutorial.Example")
  # if not functions_or_error:
  #   return None
  # for function in functions_or_error:
  #   print(function)
  #   print(len(permutate_function(function)))


if __name__ == "__main__":
  _test_parse()
