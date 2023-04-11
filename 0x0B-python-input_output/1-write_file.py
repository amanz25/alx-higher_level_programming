#!/usr/bin/python3
"""write fuction"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, "w") as f:
        f.write(text)
