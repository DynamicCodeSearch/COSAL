import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils import cache, logger
from utils.stat import Stat
from store import mongo_store


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def execution_similarity(func1, func2):
    if func1.input_key != func2.input_key:
        return 0.0
    sames = 0.0
    alls = 0.0
    assert len(func1.outputs.returns) == len(func2.outputs.returns)
    for i in range(len(func1.outputs.returns)):
        alls += 1
        o1 = func1.outputs.returns[i]
        o2 = func2.outputs.returns[i]
        e1 = func1.outputs.errors[i]
        e2 = func2.outputs.errors[i]
        if o1 == o2 and e1 == e2:
            sames += 1
    return sames / alls


def execution_distance(func1, func2):
    return 1.0 - execution_similarity(func1, func2)


def save_clusters_to_txt(clusters, file_name):
    LOGGER.info("Saving clusters to txt file '%s' ... " % file_name)
    file_contents = []
    for label, func_cluster in clusters.items():
        if label == -1: continue
        cluster_str = "\n\n****** Cluster %d ******" % label
        file_contents.append(cluster_str)
        for func in func_cluster:
            file_contents.append(func.body)
    cache.write_file(file_name, "\n".join(file_contents))


def save_clusters_to_db(dataset, clusters, suffix):
    LOGGER.info("Saving clusters to DB for dataset: '%s' ... " % dataset)
    store = mongo_store.ClusterStore(dataset)
    store.save_clusters(clusters, suffix)


def save_clusters_to_pkl(clusters, pkl_file_name):
    LOGGER.info("Saving clusters to pkl file: '%s' ... " % pkl_file_name)
    cache.save_pickle(pkl_file_name, clusters)


def load_clusters_from_pkl(file_name):
    return cache.load_pickle(file_name)


def save_clusters_metadata(clusters, num_functions, metadata_file_name):
    n_clusters = len(clusters)
    sizes = [len(cluster_funcs) for label, cluster_funcs in clusters.items() if label != -1]
    meta_data = "## Cluster sizes\n"
    meta_data += "* Number of clusters: %d\n" % n_clusters
    meta_data += "* Number of functions clustered: %d\n" % sum(sizes)
    meta_data += "* Number of functions not clustered: %d\n\n" % (num_functions - sum(sizes))
    meta_data += "## REPORT\n"
    meta_data += Stat(sizes).report()
    cache.write_file(metadata_file_name, meta_data)