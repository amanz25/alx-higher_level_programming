#!/usr/bin/python3
"""cclass inheritance"""


class Square(Rectangle):
    """square class """
    def __init__(self, size):
        """ initialization"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """area method"""
        return self.__size * self.__size
