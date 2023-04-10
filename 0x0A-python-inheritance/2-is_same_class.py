#!/usr/bin/python3
"""define function"""


def is_same_class(obj, a_class):
    """check object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
