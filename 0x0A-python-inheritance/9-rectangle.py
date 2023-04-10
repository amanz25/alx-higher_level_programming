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


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", heighit)

    def area(self):
        """area method"""
        return self.__width * self .__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
