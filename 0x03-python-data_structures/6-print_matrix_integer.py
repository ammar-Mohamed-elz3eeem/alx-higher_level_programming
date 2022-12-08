#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    state = False
    for col in range(0, len(matrix)):
        for row in range(0, len(matrix[col])):
            if (row != len(matrix[col]) - 1):
                print("{:d}".format(matrix[col][row]), end=" ")
            else:
                print("{:d}".format(matrix[col][row]))
            state = True
    if not state:
        print("")
