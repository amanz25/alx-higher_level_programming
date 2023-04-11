#!/usr/bin/python3
"""json fuction"""


import json


def save_to_json_file(my_obj, filename):
    """json to string and save to file"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
