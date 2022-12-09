#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for arr in matrix:
        mat.append(list(map(lambda x: x*x, arr)))
    return mat
