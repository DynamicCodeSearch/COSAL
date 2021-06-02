
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


from utils.lib import O
from utils import cache
from analysis.helpers.helper import generate_random_string
from mos.blocks.contest_meta_block import ContestMeta
from mos.search.tree.common import Node

import ast
import json


def to_json(json_str):
  try:
    return json.loads(json_str)
  except ValueError:
    try:
      return ast.literal_eval(json_str)
    except Exception:
      return None


class CodeBlock(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.uid = generate_random_string()
    self.language = None
    self.source_file = None
    self.code = None
    self.comments = None
    self.is_static = False
    self.is_method = False
    self.is_class = False
    self.is_file = False
    self.parent_class_name = None
    self.file_class_name = None
    self.package_name = None
    self.project_source_path = None
    self.project_lang_folder = None
    self.contextual_tokens = None
    self.ast = None
    self.contest_meta = None
    self.func_key = None

  def to_bson(self):
    bson = {
      "uid": self.uid,
      "language": self.language,
      "sourceFile": cache.get_repo_local_path(self.source_file),
      "code": self.code
    }
    if self.comments:
      bson["comments"] = self.comments
    bson["isStatic"] = self.is_static
    bson["isMethod"] = self.is_method
    bson["isClass"] = self.is_class
    bson["isFile"] = self.is_file
    if self.parent_class_name:
      bson["parentClassName"] = self.parent_class_name
    if self.file_class_name:
      bson["fileClassName"] = self.file_class_name
    if self.package_name:
      bson["packageName"] = self.package_name
    if self.project_source_path:
      bson["projectSourcePath"] = cache.get_repo_local_path(self.project_source_path)
    if self.project_lang_folder:
      bson["projectLangFolder"] = cache.get_repo_local_path(self.project_lang_folder)
    if self.contextual_tokens:
      bson["contextualTokens"] = list(self.contextual_tokens)
    if self.ast:
      code_ast = self.ast.to_bson() if isinstance(self.ast, Node) else self.ast
      bson["ast"] = str(code_ast)
    if self.contest_meta:
      bson["contestMeta"] = self.contest_meta.to_bson()
    if self.func_key:
      bson["funcKey"] = self.func_key
    return bson

  @staticmethod
  def from_bson(bson):
    code = CodeBlock()
    code.uid = bson.get("uid", None)
    code.language = bson.get("language", None)
    if "sourceFile" in bson:
      code.source_file = cache.get_absolute_path(bson["sourceFile"])
    code.code = bson.get("code", None)
    code.comments = bson.get("comments", None)
    if "isStatic" in bson:
      code.is_static = bson["isStatic"]
    if "isMethod" in bson:
      code.is_method = bson["isMethod"]
    if "isMethod" in bson:
      code.is_class = bson["isClass"]
    if "isMethod" in bson:
      code.is_file = bson["isFile"]
    code.parent_class_name = bson.get("parentClassName", None)
    code.file_class_name = bson.get("fileClassName", None)
    code.package_name = bson.get("packageName", None)
    if "projectSourcePath" in bson:
      code.project_source_path = cache.get_absolute_path(bson["projectSourcePath"])
    if "projectSourcePath" in bson:
      code.project_lang_folder = cache.get_absolute_path(bson["projectLangFolder"])
    if "contextualTokens" in bson:
      code.contextual_tokens = set(bson["contextualTokens"])
    if "ast" in bson:
      code.ast = Node.from_bson(to_json(bson['ast']))
    if "contestMeta" in bson:
      code.contest_meta = ContestMeta.from_bson(bson["contestMeta"])
    code.func_key = bson.get("funcKey", None)
    return code
