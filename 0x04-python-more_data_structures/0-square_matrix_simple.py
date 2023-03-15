#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_item = []
        for i in range(0, len(row)):
            new_item.append(row[i] ** 2)
        new_matrix.append(new_item)
    return (new_matrix)
