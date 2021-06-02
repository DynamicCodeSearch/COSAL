import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from ctypes import *
import struct
import msgpack
import subprocess

from utils import cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
DEBUG = False

free = cdll.LoadLibrary(os.path.sep + os.path.join("usr", "lib", "libc.dylib")).free

SLACC_EXPORT_HS = "_slacc_export"
SLACC_EXPORT_FILE_SUFFIX = "SLACCExport"


def make_msgpack_fun(fun):
  fun.restype = POINTER(c_char)

  def f(*args):
    packed = msgpack.packb(args)
    length_64bits = struct.pack(">q", len(packed)) # big-endian
    ptr = fun(length_64bits + packed)
    data_length = struct.unpack(">q", ptr[:8])[0]
    res = msgpack.unpackb(ptr[8:8+data_length])
    free(ptr)
    return res
  return f


cmd = " ".join([
  "ghc"
  , "-shared"  # Key to create a shared dylib file
  , "-lHSrts"  # Avoiding 'Symbol not found. Refer: https://github.com/Cosmius/haskell-ffi-example'
  , "-outputdir tmp" # Folder to send all intermediate files. Remember to delete this.
  , "-o <path-to-output-dylib-file>" # Path to output dylib file
  , "<path-to-input-hs-file>" # Path to input dylib file
])


def create_executable(source_file, output_file, root_folder, tmp_folder="tmp", delete_executable=False):
  full_output_file = os.path.join(root_folder, output_file)
  cache.delete_folder(os.path.join(root_folder, tmp_folder))
  if cache.file_exists(full_output_file):
    cache.delete_file(full_output_file)
  ghc_cmd = [
    "ghc",
    "-shared",    # Key to create a shared dylib file
    "-lHSrts",    # Avoiding 'Symbol not found. Refer: https://github.com/Cosmius/haskell-ffi-example'
    "-outputdir",
    tmp_folder,  # Folder to send all intermediate files. Remember to delete this.
    "-o",
    output_file,    # Path to output dylib file
    source_file    # Path to input dylib file
  ]
  p = subprocess.Popen(ghc_cmd, cwd=root_folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate()
  validity = cache.file_exists(full_output_file)
  if not validity and DEBUG:
    LOGGER.error("Exception creating shared lib. Run '%s'" % " ".join(ghc_cmd))
  if delete_executable:
    cache.delete_file(full_output_file)
  return validity


def load_function(func_name, executable_path):
  if not cache.file_exists(executable_path):
    LOGGER.error("Executable path '%s' does not exist for function '%s'" % (executable_path, func_name))
    return None
  if not func_name.endswith(SLACC_EXPORT_HS):
    func_name += SLACC_EXPORT_HS
  lib = cdll.LoadLibrary(executable_path)
  lib.hs_init(0, 0)
  hs_func = getattr(lib, func_name, None)
  if hs_func:
    return make_msgpack_fun(hs_func)
  return None


def test_execution():
  func = load_function("add_slacc_export", "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell/Tutorial/ExampleSLACCExport.dylib")
  print(func(2, 3))
  # print(func(4), func(5), func(6))


def test_funcload():
  func = load_function("fibTail", "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell/Tutorial/ExampleSLACCExport.dylib")
  assert func is not None
  print(func(20))


def test_creation():
  root_folder = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/haskell"
  source_file = "Tutorial/ExampleSLACCExport.hs"
  output_file = "Tutorial/ExampleSLACCExport.dylib"
  create_executable(source_file, output_file, root_folder)


if __name__ == "__main__":
  # test_creation()
  test_execution()
