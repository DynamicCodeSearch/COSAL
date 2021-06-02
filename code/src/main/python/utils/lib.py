import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"

import properties
import warnings
import json

warnings.filterwarnings("ignore", category=DeprecationWarning)


def to_json(val):
    if isinstance(val, list):
        return [to_json(v) for v in val]
    elif isinstance(val, set):
        return [to_json(v) for v in list(val)]
    elif isinstance(val, tuple):
        return [to_json(v) for v in list(val)]
    elif isinstance(val, dict):
        return {k: to_json(v) for k, v in val.items()}
    elif isinstance(val, O):
        return {k: to_json(v) for k, v in val.has().items()}
    else:
        return val


class O(object):
    def __init__(self, **d):
        """
    Base class. All classes must extend this.
    :param d: kwargs for object
    """
        self.has().update(**d)

    def has(self):
        """
    Return dictionary for object
    :return:
    """
        return self.__dict__

    def update(self, **d):
        """
        Update kwargs of dictionary
        :param d: kwargs to be updated.
        :return: Instance of object
        """
        self.has().update(d)
        return self

    def __repr__(self):
        """
        Represent as string
        :return:
        """
        return pprint(self, do_print=False)

    def __getitem__(self, key):
        """
    Retrieve item from dictionary.
    :param key: Key to be retrieved
    :return: Value at key. Will throw error if key does not exist
    """
        return self.has().get(key)

    def __setitem__(self, key, value):
        """
    Set value in dictionary.
    :param key: Key to be set
    :param value: Value at key
    """
        self.has()[key] = value

    def get_obj_type(self):
        return self.__class__.__name__


def pprint(obj, sort_keys=True, indent=2, do_print=True, skip_None=False, skip_class=False):
    contents = json.dumps(pretty(obj, indent=indent, skip_None=skip_None, skip_class=skip_class), sort_keys=sort_keys, indent=indent)
    if do_print:
        print(contents)
    return contents


def pretty(obj, indent=2, skip_None=False, skip_class=False):
    if isinstance(obj, O):
        contents = obj.has()
        if not skip_class:
            contents["$class"] = type(obj).__name__
        return pretty(contents, indent, skip_None=skip_None, skip_class=skip_class)
    elif isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            if k[0] is "_":
                continue
            if skip_None and (v is None or v == []):
                continue
            cleaned[k] = pretty(v, indent, skip_None=skip_None, skip_class=skip_class)
        return cleaned
    elif isinstance(obj, list):
        return [pretty(obj_i, indent, skip_None=skip_None, skip_class=skip_class) for obj_i in obj]
    elif isinstance(obj, set):
        return pretty(list(obj), indent, skip_None=skip_None, skip_class=skip_class)
    else:
        return obj


class O2(O):
    def __init__(self, **d):
        """
    A cleaner base class.
    1. Hides None values
    :param d: kwargs for object
    """
        O.__init__(self, **d)

    def __repr__(self):
        """
    Represent as string
    :return:
    """
        show = [':%s %s' % (k, self.has()[k])
                for k in sorted(self.has().keys())
                if self.has()[k] is not None and k[0] is not "_"]
        txt = ' '.join(show)
        if len(txt) > 60:
            show = map(lambda x: '\t' + x + '\n', show)
        return '{' + ' '.join(show) + '}'


def is_int(string):
    """
  Check if string is an integer
  :param string:
  :return: True or false
  """
    try:
        int(string)
        return True
    except ValueError:
        return False


def get_dataset_functions_results_folder(dataset):
    """
  Return the path of folder containing the function results for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
    return properties.FUNCTIONS_RESULTS_FOLDER % dataset


def get_dataset_meta_results_folder(dataset):
    """
  Return the path of folder containing the function meta data for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
    return properties.FUNCTIONS_META_FOLDER % dataset


def get_dataset_arg_index(dataset):
    """
  Return the path of index json containing the arguments for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
    return properties.ARGUMENTS_INDEX_JSON % dataset


def get_dataset_args_folder(dataset):
    """
  Return the path of folder containing the arguments for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
    return properties.ARGUMENTS_FOLDER % dataset


def get_clusters_folder(dataset):
    """
  Return the path of folder containing the clusters for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
    return properties.CLUSTERS_FOLDER % dataset
