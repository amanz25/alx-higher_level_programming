#!/usr/bin/python3
""""Define a class Square with init"""


class Square:
    """initalization/constructor while instance of clss"""

    def __init__(self, size=0):
        """set the values to be passed on the obj to the class"""
        self.__size = size

    def area(self):
        """square of the size"""
        return self.__size ** 2

    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, val):
        """setter func"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if val < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = val
