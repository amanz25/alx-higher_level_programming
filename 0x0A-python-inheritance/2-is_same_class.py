#!/usr/bin/python3
"""define function"""


def is_same_class(obj, a_class):
    """check object is exactly an instance of the specified class"""
    return issubclass(obj, a_class)
