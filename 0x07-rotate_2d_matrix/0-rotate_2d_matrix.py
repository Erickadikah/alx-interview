#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix implementation
    """
    n = len(matrix)
    # transpose the metrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix
