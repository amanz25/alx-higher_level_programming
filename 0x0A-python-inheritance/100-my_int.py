#!/usr/bin/python3
""" create class """


class MyInt(int):
    """ create MyInt class """
    def __init__(self, num):
        """ initalization """
        self.num = num

    def __eq__(self, other):
        """ equal method """
        return other != self.num

    def __ne__(self, other):
        """ not equal """
        retrun other == self.num
