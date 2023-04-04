#!/usr/bin/python3
def print_square(size):
    """print square"""
    if size != 0 and not size:
        """if the value is None"""
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        """if the size type isn't integer"""
        raise TypeError("size must be an integer")
    if size < 0:
        """check if the size is less than zero"""
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("#" * size)
