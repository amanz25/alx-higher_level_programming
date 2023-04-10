#!/usr/bin/python3
"""class inheritance"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class """
    def __init__(self, size):
        """ initialization"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size * self.__size
