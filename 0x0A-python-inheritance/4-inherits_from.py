#!/usr/bin/python3
"""define function"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
