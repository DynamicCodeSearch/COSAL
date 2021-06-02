from __future__ import division, print_function
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import numpy as np
import itertools
import multiprocessing
from collections import defaultdict
from multiprocessing import Pool, Manager
from time import time


from utils import logger, uf
from utils.lib import O
from utils.stat import Stat
from sos.function import FunctionCache
from sos.cluster import cluster_utils
from store.mongo_store import ClusterStore
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
CLUSTER_STORE = ClusterStore(dataset=properties.CONFIG.get_dataset())


class KeyComparison(O):
    def __init__(self, k1, k2, similarity_score, **kwargs):
        self.k1 = k1
        self.k2 = k2
        self.similarity_score = similarity_score
        O.__init__(self, **kwargs)


def is_same(val1, val2):
    t1, t2 = type(val1), type(val2)
    if t1 != t2:
        return False
    elif t1 == list:
        return is_same_list(val1, val2)
    elif t1 == dict:
        return is_same_dict(val1, val2)
    else:
        return val1 == val2


def is_same_list(val1, val2):
    if len(val1) != len(val2):
        return False
    for v1, v2 in zip(val1, val2):
        if not is_same(v1, v2):
            return False
    return True


def is_same_dict(val1, val2):
    if len(val1.keys()) != len(val2.keys()):
        return False
    matched = set()
    to_be_matched = 0
    for k1, v1 in val1.items():
        to_be_matched += 1
        for k2, v2 in val2.items():
            if k2 in matched:
                continue
            if is_same(v1, v2):
                matched.add(k2)
        if len(matched) != to_be_matched:
            return False
    return True


def multi_attribute_comparison(func1, func2):

    def _get_keys(rets):
        for ret in rets:
            if ret is not None:
                return ret.keys()
        return None

    def _make_key(key1, key2):
        return "%s$%s::%s:%s" % (func1.name, key1, func2.name, key2)

    best_matching = []
    best_score = 0.0
    if func1.input_key != func2.input_key:
        return best_score, best_matching
    if func1.source_file == func2.source_file:
        return best_score, best_matching
    assert len(func1.outputs.returns) == len(func2.outputs.returns)
    n = len(func1.outputs.errors)
    key_comparison_map = {}
    f1_keys = _get_keys(func1.outputs.returns)
    f2_keys = _get_keys(func2.outputs.returns)
    if f1_keys is None or f2_keys is None:
        return best_score, best_matching
    for k1 in f1_keys:
        for k2 in f2_keys:
            sames = 0
            for i in xrange(n):
                o1 = None if func1.outputs.returns[i] is None else func1.outputs.returns[i][k1]
                o2 = None if func2.outputs.returns[i] is None else func2.outputs.returns[i][k2]
                e1 = func1.outputs.errors[i]
                e2 = func2.outputs.errors[i]
                if o1 == o2 and e1 == e2:
                    sames += 1
            similarity_score = sames / float(n)
            key_comparison = KeyComparison(k1, k2, similarity_score)
            key_comparison_map[_make_key(k1, k2)] = key_comparison
    for f1_key_perm in itertools.permutations(f1_keys):
        matched = set()
        matchings = []
        scores = []
        for k1 in f1_key_perm:
            best_k2_score = 0.0
            best_k2 = None
            if len(matched) == len(f2_keys):
                break
            for k2 in f2_keys:
                if k2 in matched:
                    continue
                similarity_score = key_comparison_map[_make_key(k1, k2)].similarity_score
                if similarity_score >= best_k2_score:
                    best_k2_score = similarity_score
                    best_k2 = k2
            assert best_k2 is not None
            matched.add(best_k2)
            matchings.append((k1, best_k2))
            scores.append(best_k2_score)
        score = np.asscalar(np.mean(scores))
        if score > best_score:
            best_score = score
            best_matching = matchings
    return best_score, best_matching


class ClusterNode(O):
    def __init__(self, key, name, similarity, attributes, **kwargs):
        self.key = key
        self.name = name
        self.similarity = similarity
        self.attributes = attributes
        O.__init__(self, **kwargs)

    @staticmethod
    def make_key(name, attributes):
        return "%s::%s" % (name, "$".join(attributes))

    @staticmethod
    def create(nodes, function, similarity, attributes):
        key = ClusterNode.make_key(function.name, attributes)
        node = nodes.get(key, None)
        if node is None:
            node = ClusterNode(key, function.name, similarity, attributes)
            nodes[key] = node
        return node


def compute_difference_unpack(args):
    compute_difference(*args)


def compute_difference(func1, func2, clustering_error, stats):
    stats[0] += 1
    if func1.input_key != func2.input_key or func1.name == func2.name:
        return
    if stats[0] % 100000 == 0:
        LOGGER.info("Processing difference %d; Worker ID: %s ...." % (stats[0], multiprocessing.current_process().ident))
    dist, best_matching = multi_attribute_comparison(func1, func2)
    dist = 1.0 - dist
    if dist > clustering_error or not best_matching:
        return
    names = sorted([func1.name, func2.name])
    key = "%s::%s" % (names[0], names[1])
    difference = {
        "key": key,
        "f1": func1.name,
        "f2": func2.name,
        "input_key": func1.input_key,
        "dist": dist,
        "best_matching": best_matching
    }
    CLUSTER_STORE.save_difference(difference, clustering_error)


class MultiAttributeRepresentativeClusterer(O):
    # TODO:
    """
    1. Compute differences and store in auxilarytable
    2. Generate clusters based on differences and similarities
    """
    def __init__(self, **kwargs):
        self.nodes = {}
        self.union_find = uf.UnionFind()
        O.__init__(self, **kwargs)

    def preprocess(self, clustering_error, processes=None):
        stats = Manager().dict()
        stats[0] = 0
        stats[1] = 0
        input_key_buckets = bucketize(FunctionCache.load_functions(), "input_key")
        if processes is None:
            processes = multiprocessing.cpu_count()
        # async_pool = Pool(processes=processes)
        start = time()
        completed_functions = set(CLUSTER_STORE.get_completed_functions(clustering_error))
        for bucket_i, (input_key, input_key_functions) in enumerate(input_key_buckets.items()):
            ik_n = len(input_key_functions)
            if ik_n < 2:
                continue
            LOGGER.info("Processing Bucket: %d/%d. Key = '%s'. Number of functions = %d ...." % (bucket_i, len(input_key_buckets), input_key, ik_n))
            file_buckets = bucketize(input_key_functions, 'source_file')
            file_names = file_buckets.keys()
            n_files = len(file_names)
            for fn_i in xrange(n_files - 1):
                for fn_j in xrange(fn_i + 1, n_files):
                    for i, func_i in enumerate(file_buckets[file_names[fn_i]]):
                        if i % 100 == 0:
                            completed_functions = set(CLUSTER_STORE.get_completed_functions(clustering_error))
                        if func_i.name in completed_functions:
                            # LOGGER.info("Completed preprocessing function: '%s'. Moving on ..." % func_i.name)
                            continue
                        for func_j in file_buckets[file_names[fn_j]]:
                            if func_j.name in completed_functions:
                                continue
                            # stats[1] += 1
                            # args.append((func_i, func_j, clustering_error, stats))
                            # async_pool.apply_async(compute_difference, args=(func_i, func_j, clustering_error, stats))
                            compute_difference(func_i, func_j, clustering_error, stats)
                        # TODO: Uncomment line below
                        # CLUSTER_STORE.register_completed_function(func_i.name, clustering_error)
        print("Time Taken: %0.4f" % (time() - start))
            # for fn_i in xrange(n_files - 1):
            #     for fn_j in xrange(fn_i + 1, n_files):
            #         for i, func_i in enumerate(file_buckets[file_names[fn_i]]):
            #             # if i % 100 == 0:
            #             #     completed_functions = set(CLUSTER_STORE.get_completed_functions(clustering_error))
            #             if func_i.name in completed_functions:
            #                 # LOGGER.info("Completed preprocessing function: '%s'. Moving on ..." % func_i.name)
            #                 continue
            #             for func_j in file_buckets[file_names[fn_j]]:
            #                 # stats[1] += 1
            #                 # args.append((func_i, func_j, clustering_error, stats))
            #                 # async_pool.apply_async(compute_difference, args=(func_i, func_j, clustering_error, stats))
            #                 compute_difference(func_i, func_j, clustering_error, stats)
            #             CLUSTER_STORE.register_completed_function(func_i.name, clustering_error)


    def update_cluster(self, f_i, f_j, difference):
        dist = difference["dist"]
        best_matching = difference["best_matching"]
        sim = 1.0 - dist
        f_i_attributes, f_j_attributes = zip(*best_matching)
        f_i_node = ClusterNode.create(self.nodes, f_i, sim, f_i_attributes)
        f_j_node = ClusterNode.create(self.nodes, f_j, sim, f_j_attributes)
        self.union_find.union(f_i_node, f_j_node)

    def cluster(self, file_name=None, skip_singles=False, clustering_error=0.01, log_interval=100):
        n = len(self.functions)
        LOGGER.info("Clustering %d clusters using Multi Attribute Representative Clusterer with tolerance '%0.2f'"
                    % (n, clustering_error))
        functions = {f.name: f for f in self.functions}
        n_differences = CLUSTER_STORE.count_differences(clustering_error)
        for i, diff in enumerate(CLUSTER_STORE.load_differences(clustering_error)):
            if i % 1000 == 0:
                LOGGER.info("Processed differences: %d/%d ... " % (i, n_differences))
            if diff["f1"] not in functions or diff["f2"] not in functions:
                continue
            f1 = functions[diff["f1"]]
            f2 = functions[diff["f2"]]
            self.update_cluster(f1, f2, diff)

        # time_counts = []
        # for i in xrange(n - 1):
        #     if (i + 1) % log_interval == 0:
        #         LOGGER.info("Processing function %d / %d " % (i + 1, n - 1))
        #     for j in xrange(i + 1, n):
        #         start = time()
        #         update_cluster(self, functions[i].name, functions[j].name, clustering_error)
        #         time_counts.append(time() - start)
        #         # f_i = functions[i]
        #         # f_j = functions[j]
        #         # dist, best_matching = multi_attribute_comparison(f_i, f_j)
        #         # sim = 1.0 - dist
        #         # if sim > clustering_error or not best_matching:
        #         #     continue
        #         # f_i_attributes, f_j_attributes = zip(*best_matching)
        #         # f_i_node = ClusterNode.create(self.nodes, f_i, sim, f_i_attributes)
        #         # f_j_node = ClusterNode.create(self.nodes, f_j, sim, f_j_attributes)
        #         # self.union_find.union(f_i_node, f_j_node)
        # print(Stat(time_counts).report())
        clusters = {}
        for cluster_id, cluster_nodes in self.union_find.get_disjoint_sets().items():
            if skip_singles and len(cluster_nodes) == 1:
                continue
            clusters[cluster_id] = [functions[node.name] for node in cluster_nodes]
        cluster_utils.save_clusters_to_txt(clusters, file_name)
        return clusters


def bucketize(items, attribute):
    buckets = defaultdict(list)
    for item in items:
        buckets[getattr(item, attribute)].append(item)
    return buckets
