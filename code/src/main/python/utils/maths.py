import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


import itertools


def permutate_lists(list_of_lists):
  """
  [[1,2,3],[4],[5,6]] => [[1,4,5], [1,4,6], [2,4,5], [2,4,6], [3,4,5], [3,4,6]]
  Permutate
  :param list_of_lists: List of lists
  :return: Each member of a list permutated with each other member of other lists
  """
  if list_of_lists is None:
    return None
  return map(list, itertools.product(*list_of_lists))


def permutate_list(lst):
  """
  [1,2,3] => [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
  :param lst: List of values
  :return: All permutations of the list
  """
  if not lst:
    return None
  return map(list, itertools.permutations(lst))

