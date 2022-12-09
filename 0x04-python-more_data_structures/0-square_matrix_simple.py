#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for arr in matrix:
        mat.append(list(map(lambda x: x*x, arr)))
    return mat
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
