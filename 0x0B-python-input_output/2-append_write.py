#!/usr/bin/python3
"""append fuction"""


def append_write(filename="", text=""):
    """function that append a string to a text file"""
    with open(filename, "a") as f:
        return f.write(text)
