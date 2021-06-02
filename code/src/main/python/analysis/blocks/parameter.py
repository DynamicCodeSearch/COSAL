import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

from utils.lib import O


class Parameter(O):
  def __init__(self, name, index, **kwargs):
    self.name = name
    self.index = index
    self.types = None
    self.has_default_value = False
    O.__init__(self, **kwargs)

  def is_valid(self):
    """
    :return: True if either types is not empty or if default value is set
    """
    return self.has_default_value or (self.types and any([typ.is_valid for typ in self.types]))

  def to_bson(self):
    bson = {
      "name": self.name,
      "index": self.index,
      "has_default_value": self.has_default_value
    }
    if self.types:
      bson["types"] = [typ.to_bson() for typ in self.types]
    return bson

  def to_specific_parameters(self):
    if self.types is None:
      return None
    specific_params = []
    for typ in self.types:
      specific_types = typ.to_specific_types()
      if specific_types is None:
        continue
      for specific_type in specific_types:
        if not specific_type.is_valid:
          continue
        specific_param = SpecificParameter(self.name, self.index, type=specific_type,
                                           has_default_value=self.has_default_value)
        specific_params.append(specific_param)
    if len(specific_params) == 0:
      return None
    return specific_params

  def clone(self):
    cloned = Parameter(self.name, self.index)
    cloned.has_default_value = self.has_default_value
    if self.types:
      cloned.types = [typ.clone() for typ in self.types]
    return cloned


class SpecificParameter(O):
  def __init__(self, name, index, **kwargs):
    self.name = name
    self.index = index
    self.type = None
    self.has_default_value = False
    O.__init__(self, **kwargs)

  def is_valid(self):
    """
    :return: True if either types is not empty or if default value is set
    """
    return self.has_default_value or (self.type and self.type.is_valid)

  def to_bson(self):
    bson = {
      "slacc_type": self.get_obj_type(),
      "name": self.name,
      "index": self.index,
      "has_default_value": self.has_default_value
    }
    if self.type:
      bson["type"] = self.type.to_bson()
    return bson

  def clone(self):
    cloned = SpecificParameter(self.name, self.index)
    cloned.has_default_value = self.has_default_value
    if self.type:
      cloned.type = self.type.clone()
    return cloned
