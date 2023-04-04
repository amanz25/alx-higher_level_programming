#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """disply name"""
    if not isinstance(first_name, str):
        """if firstname isn't string"""
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """if lastname  isn't string"""
        raise TypeError("last_name  must be a string")
    print("My name is", first_name, last_name)
