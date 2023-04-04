#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ division fuction """
    typeErrorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    zeroErrorMsg = "division by zero"
    if not matrix:
        """ check if the matrix is empty """
        raise TypeError(typeErrorMsg)
    if not isinstance(matrix, list):
        """ check if the matrix type is list """
        raise TypeError(typeErrorMsg)
    if not isinstance(div, int) and not isinstance(div, float):
        """ check the divisor data type is int or float """
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        """ check all list sizes are equal """
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError(zeroErrorMsg)
    for arr in matrix:
        """ check all elements are int or float """
        if len(arr) == 0:
            raise TypeError(typeErrorMsg)
        if not isinstance(arr, list):
            """ the element isn't a list """
            raise TypeError(typeErrorMsg)
        for element in arr:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(typeErrorMsg)
    return [[round(item / div, 2) for item in lists] for lists in matrix]
