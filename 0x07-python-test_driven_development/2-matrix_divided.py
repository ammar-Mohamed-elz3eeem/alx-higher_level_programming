def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    oldlen = None
    for i in range(0, len(matrix)):
        if oldlen and oldlen != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row.append(round(matrix[i][j] * 1.0 / div, 2))
        new_matrix.append(row)
        oldlen = len(matrix[i])
    return new_matrix