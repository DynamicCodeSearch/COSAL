import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from collections import defaultdict
from sklearn.cluster import DBSCAN


from utils import logger
from utils.lib import O
from sos.cluster import cluster_utils

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class DBScanClusterer(O):
    def __init__(self, functions, **kwargs):
        self.functions = functions
        # noinspection PyUnresolvedReferences
        self.X = np.arange(len(self.functions)).reshape(-1, 1)
        O.__init__(self, **kwargs)

    def distance(self, x, y):
        return cluster_utils.execution_distance(self.functions[int(x)], self.functions[int(y)])

    def cluster(self, file_name=None, skip_singles=False, clustering_error=0.01):
        LOGGER.info("Clustering using DBScan with tolerance '%0.2f'" % clustering_error)
        dbs = DBSCAN(eps=clustering_error, min_samples=2, metric=self.distance)
        labels = dbs.fit_predict(self.X)
        clusters = defaultdict(list)
        for label, func in zip(labels, self.functions):
            if skip_singles and label == -1:
                continue
            clusters[label].append(func)
        cluster_utils.save_clusters_to_txt(clusters, file_name)
        return clusters
