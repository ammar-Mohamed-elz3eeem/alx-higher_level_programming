#!/usr/bin/python3
def pascal_triangle(n):

    if n <= 0:
        return []
    if n == 1:
        matrix.append([1])

    matrix = [[1]]

    while len(matrix) != n:
        tri = matrix[-1]
        start = [1]
        for i in range(0, len(tri) - 1):
            start.append(tri[i] + tri[i + 1])
        start.append(1)
        matrix.append(start)
    return matrix
