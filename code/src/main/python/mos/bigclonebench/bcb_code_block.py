import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from mos.blocks.code_block import CodeBlock
import properties


class BCBCodeBlock(CodeBlock):
  def __init__(self, **kwargs):
    CodeBlock.__init__(self, **kwargs)
    self.is_class = True
    self.language = properties.LANGUAGE_JAVA
    self.problem_id = None
    self.submission_type = None
    self.submission_id = None
    self.is_class = True
    self.is_file = True
    self.is_static = True

  def to_bson(self):
    bson = super(BCBCodeBlock, self).to_bson()
    bson["problemId"] = self.problem_id
    bson["submissionType"] = self.submission_type
    bson["submissionId"] = self.submission_id
    return bson

  @staticmethod
  def from_bson(bson):
    code = BCBCodeBlock()
    code.__dict__ = CodeBlock.from_bson(bson).__dict__
    code.problem_id = bson.get("problemId", None)
    code.submission_type = bson.get("submissionType", None)
    code.submission_id = bson.get("submissionId", None)
    return code
