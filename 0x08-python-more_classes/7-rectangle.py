#!/usr/bin/python3
""" creates a Rectangle class """


class Rectangle:
    """  Class Rectangle    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiates width and height/ constructor """
        type(self).number_of_instances += 1
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

    def area(self):
        """ return area of a rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ return perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def _print_rectangle(self):
        """ print the rectangle """
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "{}".format(self.print_symbol)
            if self.__width != 0 and r < (self.__height - 1):
                s += '\n'
        return s

    def __str__(self):
        """ override str function """
        return self._print_rectangle()

    def __repr__(self):
        """ recreate a new instance by using eval """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(ins):
        """ print message added while an instance deletion """
        ins.number_of_instances -= 1
        print("Bye rectangle...")
