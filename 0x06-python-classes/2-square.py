#!/usr/bin/python3
""""Define a class Square with init"""


class Square:
    """initalization/constructor while instance of clss"""

    def __init__(self, size):
        """check the type and set the values of class intance variable"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
