#!/usr/bin/python3
""" create class """


class MyInt(int):
    """ create MyInt class """

    def __eq__(self, other):
        """ equal method """
        return int(other) != int(self)

    def __ne__(self, other):
        """ not equal """
        retrun int(other) == int(self)
