#!/usr/bin/python3
""""Define a class Square with init"""


class Square:
    """initalization/constructor while instance of clss"""

    def __init__(self, size=0):
        """set the values to be passed on the obj to the class"""
        self.size = size

    def area(self):
        """square of the size"""
        return self.__size ** 2

    @property
    def size(self):
        """getter func
        Returns:
           The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter func
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
