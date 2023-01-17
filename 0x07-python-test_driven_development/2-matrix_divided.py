#!/usr/bin/python3
"""
Containing mathematicams opparations

raise exception error for type
"""


def matrix_divided(matrix, div):
    """
    divides a givin matrix by div
    """
    for list in matrix:
        for element in list:
            if not (isinstance(element, (int, float))):
                msg_0 = "matrix must be a matrix"
                msg_1 = " (list of lists) of integers/floats"
                raise TypeError(msg_0 + msg_1)
    size = len(matrix[0])
    for list in matrix[1:]:
        if len(list) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = []
    for list in range(len(matrix)):
        row = []
        for element in range(size):
            row.append(round(matrix[list][element] / div, 2))
        divided_matrix.append(row)
    return divided_matrix
