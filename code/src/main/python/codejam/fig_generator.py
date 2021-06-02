from __future__ import division, print_function
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("white")

def plot():
  java_functions = np.cumsum([1680,1572,439,321,168])
  py_functions = np.cumsum([963,1015,498,382,277])
  mixed_functions = np.cumsum([62,63,6,0,0])
  funcs = np.transpose([java_functions, py_functions, mixed_functions])
  x = ["1", "2", "3", "4", "5"]
  # plt.figure()
  fig, ax = plt.subplots(figsize=(8, 4))

  ax.plot(np.arange(5), java_functions, '*-', label="Java")
  ax.plot(np.arange(5), py_functions, '*-',label="Python")
  ax.plot(np.arange(5), mixed_functions, '*-',label="Java + Python")
  ax.set_yscale("log")
  plt.ylabel("# Clones (Log Scale)", fontweight="bold", fontsize=16)
  plt.xlabel("# Arguments", fontweight="bold", fontsize=16)
  plt.xticks(np.arange(5), x)
  ax.tick_params(axis='both', which='major', labelsize=14)
  # ax.tick_params(axis='both', which='minor', labelsize=12)
  legend = ax.legend(shadow=True, fontsize=16)
  plt.tight_layout()
  plt.savefig("png_clones_vs_args.png")


# plot()

def plot_bar():
  # y = [271,811,843,747,753,502,275,281,383,364,288,261,279,252,227,184,132,101,73,66,69,55,53,46,24,28,31,7,4,36]
  java_lst =  [140, 420, 436, 387, 390, 260, 142, 145, 198, 188, 149, 135, 144, 130, 117, 95, 68, 52, 38, 34, 36, 26, 22, 24, 12, 14, 16, 4, 2, 19]
  py_lst = [148, 334, 365, 271, 273, 132, 100, 102, 109, 102, 104, 95, 101, 81, 72, 57, 48, 37, 26, 24, 25, 18, 16, 17, 9, 10, 11, 3, 1, 13]
  j_sum = sum(java_lst)
  p_sum = sum(py_lst)
  print("### Java")
  for j in xrange(len(java_lst)):
    print(j, round(sum(java_lst[:j+1]) / j_sum, 2))
  print("### Python")
  for j in xrange(len(py_lst)):
    print(j, round(sum(py_lst[:j+1]) / p_sum, 2))
  x = map(str, range(1,30)) + ["30+"]
  indices = np.arange(len(x))
  plt.figure(figsize=(8, 3))
  plt.plot(indices, java_lst, label="Java")
  plt.plot(indices, py_lst, label="Python")
  plt.xticks(indices, x)
  plt.xlabel("Lines of Code", fontweight="bold", fontsize=16)
  plt.ylabel("# Clones", fontweight="bold", fontsize=16)
  plt.tick_params(axis='y', which='major', labelsize=12)
  legend = plt.legend(shadow=True, fontsize=16)
  plt.tight_layout()
  plt.savefig("png_clones_vs_loc.png", bbox_inches='tight')





plot_bar()

lst = [271,811,843,747,753,502,275,281,383,364,288,261,279,252,227,184,132,101,73,66,69,50,43,46,24,28,31,7,4,36]
# java_lst =  [int(round(3845/7431 * x)) for x in lst]
java_lst =  [140, 420, 436, 387, 390, 260, 142, 145, 198, 188, 149, 135, 144, 130, 117, 95, 68, 52, 38, 34, 36, 26, 22, 24, 12, 14, 16, 4, 2, 19]
# py_lst =  [int(round(2691/7431 * x)) for x in lst]
py_lst = [148, 334, 365, 271, 273, 132, 100, 102, 109, 102, 104, 95, 101, 91, 82, 67, 48, 37, 26, 24, 25, 18, 16, 17, 9, 10, 11, 3, 1, 13]
print(0.53 * 3845, 0.51 * 2691)