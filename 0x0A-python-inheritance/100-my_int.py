#!/usr/bin/python3
""" create class """


class MyInt(int):
    """ create MyInt class """
    def __new__(cls, *args, **kwargs):
        """ create instance """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ equal method """
        return other != int(self)

    def __ne__(self, other):
        """ not equal """
        retrun other == int(self)
