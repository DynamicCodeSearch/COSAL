
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils.lib import O


class ContestMeta(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.submission_id = None
    self.contest_type = None
    self.contest_id = None
    self.problem_id = None
    self.exec_time = None
    self.code_size = None

  def to_bson(self):
    bson = {
      "submissionId": self.submission_id
    }
    if self.contest_type is not None:
      bson["contestType"] = self.contest_type
    if self.contest_id is not None:
      bson["contestId"] = self.contest_id
    if self.problem_id is not None:
      bson["problemId"] = self.problem_id
    if self.code_size is not None:
      bson["codeSize"] = self.code_size
    if self.exec_time is not None:
      bson["execTime"] = self.exec_time
    return bson

  @staticmethod
  def from_bson(bson):
    block = ContestMeta()
    block.submission_id = bson["submissionId"]
    if "contestType" in bson:
      block.contest_type = bson["contestType"]
    if "contestId" in bson:
      block.contest_id = bson["contestId"]
    else:
      block.contest_id = 0
    if "problemId" in bson:
      block.problem_id = bson["problemId"]
    else:
      block.problem_id = 0
    if "codeSize" in bson:
      block.code_size = bson["codeSize"]
    if "execTime" in bson:
      block.exec_time = bson["execTime"]
    return block

  def make_key(self):
    return "C:%d-P:%d" % (self.contest_id, self.problem_id)
