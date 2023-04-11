#!/usr/bin/python3
"""file manipulation"""


def read_file(filename=""):
    """read file"""
    content = ""
    with open(filename, encoding="UTF8") as f:
        content = f.read()
    print(content)
