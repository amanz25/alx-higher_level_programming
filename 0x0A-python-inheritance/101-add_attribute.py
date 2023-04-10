#!/usr/bin/python3
""" ddefine a function """


def add_attribute(cls, name, value):
    """ add new attribute """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
