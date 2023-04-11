#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""
import sys


if __name__ == "__main__":
    try:
        val = __import__('6-load_from_json_file')\
                .load_from_json_file("add_item.json")
    except FileNotFoundError:
        val = []
    val.extend(sys.argv[1:])
    __import__('5-save_to_json_file')\
        .save_to_json_file(val, "add_item.json")
