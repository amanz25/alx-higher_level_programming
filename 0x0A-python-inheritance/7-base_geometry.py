#!/usr/bin/python3
"""create a base class"""


class BaseGeometry:
    """class with method return exception"""
    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
