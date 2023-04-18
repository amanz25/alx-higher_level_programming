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

    def update(self, *args, **kwargs):
        """üpdate the square"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of a Square"""
        return {
                "size": self.size,
                "x": self.x,
                "y": self.y,
                "id": self.id
                }
