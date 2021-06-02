import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O


class Family(O):
    def __init__(self, name, index):
        O.__init__(self, name=name, index=index)


INT_FAMILY = Family(name="int", index=0)
CHAR_FAMILY = Family(name="int", index=0)
FLOAT_FAMILY = Family(name="int", index=0)
BOOLEAN_FAMILY = Family(name="int", index=0)
BYTE_FAMILY = Family(name="int", index=0)
STRING_FAMILY = Family(name="int", index=0)


class Primitive(O):
    _primitives = []
    _typeToPrimitiveMap = dict()
    _nameToPrimitiveMap = dict()
    _primitive_types = set()

    def __init__(self, index, name, family, *types, **kwargs):
        self.index = index
        self.name = name
        self.family = family
        self.types = set(types)
        O.__init__(self, **kwargs)
        Primitive._primitives.append(self)
        for t in types:
            Primitive._primitive_types.add(t)
            Primitive._typeToPrimitiveMap[t] = self
        Primitive._nameToPrimitiveMap[name] = self

    @staticmethod
    def get_primitives():
        return Primitive._primitives

    @staticmethod
    def get_primitive_by_name(n):
        return Primitive._nameToPrimitiveMap.get(n, None)

    @staticmethod
    def get_primitive_by_type(t):
        return Primitive._typeToPrimitiveMap.get(t, None)

    @staticmethod
    def is_valid_type(t):
        return Primitive.get_primitive_by_type(t) is not None


SHORT = Primitive(0, "short", INT_FAMILY, "short", "Short", "java.lang.Short")
INTEGER = Primitive(1, "integer", INT_FAMILY, "int", "integer", "Integer", "java.lang.Integer")
LONG = Primitive(2, "long", INT_FAMILY, "long", "Long", "java.lang.Long")
CHARACTER = Primitive(3, "character", CHAR_FAMILY, "char", "character", "Character", "java.lang.Character")
FLOAT = Primitive(4, "float", FLOAT_FAMILY, "float", "Float", "java.lang.Float")
DOUBLE = Primitive(5, "double", FLOAT_FAMILY, "double", "Double", "java.lang.Double")
BOOLEAN = Primitive(6, "boolean", BOOLEAN_FAMILY, "boolean", "Boolean", "java.lang.Boolean")
BYTE = Primitive(7, "byte", BYTE_FAMILY, "byte", "Byte", "java.lang.Byte")
STRING = Primitive(8, "string", STRING_FAMILY, "String", "java.lang.String", "string")
CHAR_SEQUENCE = Primitive(9, "char_sequence", STRING_FAMILY, "CharSequence", "java.lang.CharSequence")



if __name__ == "__main__":
    print(Primitive.is_valid_type("float"))
