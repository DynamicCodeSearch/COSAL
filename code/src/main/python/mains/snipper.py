import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from analysis.helpers import constants as a_consts
from analysis import generate
from utils import cache
import properties


def execute(root_folder):
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    file_name = cache.get_file_name(file_path)
    if file_name == "__init__" or file_name.startswith(a_consts.GENERATED_PREFIX) or file_name.startswith(a_consts.PERMUTATED_PREFIX) or file_name.endswith(".py"):
      continue
    generate.generate_for_file(properties.CONFIG.get_dataset(), file_path)


def execute_dataset():
  execute(properties.PYTHON_PROJECTS_HOME)


def execute_problem(problem):
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, problem)
  execute(root_folder)


def export_methods(problem):
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, dataset)
  if problem:
    root_folder = os.path.join(root_folder, problem)
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    file_name = cache.get_file_name(file_path)
    if file_name == "__init__" or file_name.startswith(a_consts.GENERATED_PREFIX) or file_name.startswith(a_consts.PERMUTATED_PREFIX):
      continue
    generate.generate_for_file(properties.CONFIG.get_dataset(), file_path)


if __name__ == "__main__":
  args = sys.argv

  if len(args) > 1:
    execute_problem(args[1])
  else:
    execute_dataset()
