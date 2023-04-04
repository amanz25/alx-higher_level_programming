#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """"matrix multiplication"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for arr_a in m_a:
        if not isinstance(arr_a, list):
            raise TypeError("m_a must be a list of lists")
    for arr_b in m_b:
        if not isinstance(arr_b, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) > 0:
        for arr_a in m_a:
            if len(arr_a) == 0:
                raise ValueError("m_a can't be empty")
    else:
        raise ValueError("m_a can't be empty")
    if len(m_b) > 0:
        for arr_b in m_b:
            if len(arr_b) == 0:
                raise ValueError("m_b can't be empty")
    else:
        raise ValueError("m_b can't be empty")
    for r in m_a:
        for c in r:
            if type(c) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for r in m_b:
        for c in r:
            if type(c) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    first_matrix_col_len = 0
    second_matrix_col_len = 0
    for r in m_a:
        if len(r) != first_matrix_col_len and first_matrix_col_len != 0:
            raise TypeError("each row of m_a must be of the same size")
        first_matrix_col_len = len(r)
    for r in m_b:
        if len(r) != second_matrix_col_len and second_matrix_col_len != 0:
            raise TypeError("each row of m_b must be of the same size")
        second_matrix_col_len = len(r)

    if first_matrix_col_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(i * j for i, j in zip(r, c))
             for c in zip(*m_b)] for r in m_a]
