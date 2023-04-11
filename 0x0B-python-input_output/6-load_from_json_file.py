#!/usr/bin/python3
"""load from json file"""


import json


def load_from_json_file(filename):
    """lload from json file function"""
    with open(filename) as f:
        return json.load(f)
