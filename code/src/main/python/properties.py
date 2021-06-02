import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

import config

__author__ = "COSAL"

CONFIG = config.BigCloneBenchConfig()

"""
File paths
"""
META_RESULTS_FOLDER = os.path.join(CONFIG.CODE_HOME, "meta_results")
META_STORE_FOLDER = os.path.join(CONFIG.CODE_HOME, "meta_store")
RESULTS_FOLDER = os.path.join(CONFIG.CODE_HOME, "results")
ARGUMENTS_FOLDER = os.path.join(META_STORE_FOLDER, "%s", "arguments")
ARGUMENTS_INDEX_JSON = os.path.join(ARGUMENTS_FOLDER, "index.json")
FUNCTIONS_META_FOLDER = os.path.join(META_STORE_FOLDER, "%s", "functions")
FUNCTIONS_RESULTS_FOLDER = os.path.join(META_RESULTS_FOLDER, "%s", "functions")
CLUSTERS_FOLDER = os.path.join(META_RESULTS_FOLDER, "%s", "clusters")


PYTHON_PROJECTS_HOME = CONFIG.get_python_projects_home()



"""
Constants and Hyper parameters
"""
FUZZ_ARGUMENT_SIZE = 256
SUCCESS_CODE = 200
CODE_JAM = "codejam"
INTRO_CLASS_JAVA = "introclass"
MIN_STATEMENT_SIZE = 2
MAX_ARGUMENT_SIZE = 5
MIN_CONTEXT_TOKEN_SIZE = 3
LANGUAGE_JAVA = "java"
LANGUAGE_PYTHON = "py"
TOKEN_SIZE = 5

"""
Config
"""
STORE = "mongo"  # Can be "json"/"mongo"
CLUSTER_TYPE = "representative"  # Can be "representative"/"dbscan"

if __name__ == "__main__":
  import HaPy
  print(HaPy)