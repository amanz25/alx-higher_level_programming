#!/usr/bin/python3
"""define a function"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        """initalization"""
        super().__init__

    def print_sorted(self):
        """print sorted array"""
        print(sorted(self))
