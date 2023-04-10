#!/usr/bin/python3
"""create a base class"""


class BaseGeometry:
    """class with method return exception"""
    def area(self):
        """area function"""
        raise Exception("area() is not implemented")
