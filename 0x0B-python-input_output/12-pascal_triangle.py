#!/usr/bin/python3
""" module that have function for making pascal trianle """


def pascal_triangle(n):

    """ pascal_triangle - returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
        n (int): size of pascal trinagle

    Returns:
        list: matrix to represent pascal triangle

    """

    if n <= 0:
        return []

    matrix = [[1]]

    while len(matrix) != n:
        tri = matrix[-1]
        start = [1]
        for i in range(0, len(tri) - 1):
            start.append(tri[i] + tri[i + 1])
        start.append(1)
        matrix.append(start)
    return matrix
