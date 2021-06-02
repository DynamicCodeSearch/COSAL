import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from store import json_store, mongo_store
from utils import cache, logger
import properties

import random


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_store():
    dataset = properties.CONFIG.get_dataset()
    if properties.STORE == "json":
        return json_store.FunctionStore(dataset)
    elif properties.STORE == "mongo":
        return mongo_store.FunctionStore(dataset)
    raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def load_functions(limit=None, sample_size=0.01):
    LOGGER.info("Saving java functions for '%s' ... " % properties.CONFIG.get_dataset())
    store = get_store()
    functions_arr = store.load_all_metadata(limit=limit)
    bodies = []
    for i, func in enumerate(functions_arr):
        if "argsPermutation" not in func:
            continue
        if i % 1000 == 0:
            LOGGER.info("Processing functions: %d ... " % i)
        bodies.append(func["body"])
    random.shuffle(bodies)
    bodies = bodies[0:int(sample_size * len(bodies))]
    file_name = os.path.join(properties.CONFIG.CODE_HOME, "_expts", "functions.txt")
    cache.write_file(file_name, "\n\n".join(bodies))


if __name__ == "__main__":
    load_functions()
