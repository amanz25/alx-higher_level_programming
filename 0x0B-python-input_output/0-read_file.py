#!/usr/bin/python3
"""file manipulation"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
