#!/usr/bin/python3
"""load from json file"""


import json


def load_from_json_file(filename):
    """lload from json file function"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f)
