import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils import logger, uf
from utils.lib import O
from sos.cluster import cluster_utils

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class RepresentativeClusterer(O):
    def __init__(self, functions, distance_function=cluster_utils.execution_distance, **kwargs):
        self.functions = functions
        self.distance_function = distance_function
        self.union_find = uf.UnionFind(functions)
        O.__init__(self, **kwargs)

    def cluster(self, file_name=None, skip_singles=False, clustering_error=0.01):
        LOGGER.info("Clustering using Representative Sampling with tolerance '%0.2f'" % clustering_error)
        n = len(self.functions)
        for i in xrange(n - 1):
            LOGGER.info("Processing function %d / %d " % (i + 1, n - 1))
            for j in xrange(i+1, n):
                f_i = self.functions[i]
                f_j = self.functions[j]
                if self.union_find.find(f_i) == self.union_find.find(f_j):
                    continue
                dist = self.distance_function(f_i, f_j)
                if dist <= clustering_error:
                    self.union_find.union(f_i, f_j)
        clusters = {}
        for cluster_id, cluster_nodes in self.union_find.get_disjoint_sets().items():
            if skip_singles and len(cluster_nodes) == 1:
                continue
            clusters[cluster_id] = cluster_nodes
        cluster_utils.save_clusters_to_txt(clusters, file_name)
        return clusters

