#!/usr/bin/python3
"""rectangle defination"""
from models.base import Base


class Rectangle(Base):
    """define rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """define constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """return x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x value"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """return y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y value"""
        self.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(attribute, value):
        """validation of all setter methods and instantiation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        rectangle = ""
        print("\n" * self.y, end="")
        for e in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """override the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update the rectangle"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
