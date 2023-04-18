#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """define constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size value to the width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """override str function"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)
