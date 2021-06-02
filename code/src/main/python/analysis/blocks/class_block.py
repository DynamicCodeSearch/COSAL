import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O
from utils import cache
from analysis.blocks import position as position_block
from analysis.blocks import parameter as parameter_block
from analysis.blocks import types as types_block


class Class(O):
    def __init__(self, name, **kwargs):
        self.name = name
        self.file_source = None
        self.start_pos = None
        self.end_pos = None
        self.constructor_params = []
        self.scope_str = None
        self._ast = None
        O.__init__(self, **kwargs)

    def get_ast(self):
        return self._ast

    def set_ast(self, _ast):
        self._ast = _ast

    def is_valid(self):
        if not self.constructor_params:
            return False
        for param in self.constructor_params:
            if not param.is_valid():
                return False
        return True

    @staticmethod
    def load(node, file_source=None, scope=None, **kwargs):
        clazz = Class(node.name)
        clazz.update(**kwargs)
        clazz.file_source = file_source
        clazz.start_pos, clazz.end_pos = position_block.Position.get_start_end(node)
        clazz.set_ast(node)
        if scope:
            clazz.scope_str = str(scope)
        return clazz

    def to_bson(self):
        bson = {
            "name": self.name,
            "file_source": cache.get_repo_local_path(self.file_source)
        }
        if self.start_pos:
            bson["start_pos"] = self.start_pos.to_bson()
        if self.end_pos:
            bson["end_pos"] = self.end_pos.to_bson()
        if self.scope_str:
            bson["scope_str"] = self.scope_str
        if self.constructor_params:
            bson["constructor_params"] = [param.to_bson() for param in self.constructor_params]
        return bson

    def to_custom_type(self):
        typ = types_block.CustomType(name=self.name, file_path=self.file_source)
        typ.parameters = self.constructor_params
        return typ
