#!/usr/bin/python3
""" creates a Rectangle class """


class Rectangle:
    """  Class Rectangle    """

    def __init__(self, width=0, height=0):
        """Instantiates width and height/ constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value as a width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value as a height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
