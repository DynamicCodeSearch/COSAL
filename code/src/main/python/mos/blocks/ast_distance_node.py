import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O


class ASTDistanceNode(O):
  DELIMITER = "-"

  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.uid1 = None
    self.uid2 = None
    self.distance = None

  def get_key(self):
    return ASTDistanceNode.DELIMITER.join(sorted([self.uid1, self.uid2]))

  def to_bson(self):
    return {
      "uid1": self.uid1,
      "uid2": self.uid2,
      "key": self.get_key(),
      "distance": self.distance
    }

  @staticmethod
  def from_bson(bson):
    node = ASTDistanceNode()
    splits = bson["key"].split(ASTDistanceNode.DELIMITER)
    node.uid1 = splits[0]
    node.uid2 = splits[1]
    node.distance = bson["distance"]
    return node
