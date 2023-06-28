def matrix_mul(m_a, m_b):
    new_matrix = []
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) <= 0:
        raise TypeError("m_b must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in range(0, len(m_a)):
        new_sum = 0

        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")

        # i = 0, i = 1, i = 2
        
        for j in range(0, len(m_b)):
            print(f"i = {i}, j = {j}")

        # for j in range(0, len(m_a[i])):
        #     # critcal case: matrix's list items are not numbers
        #     if type(m_a[i][j]) not in [float, int]:
        #         raise TypeError("m_a should contain only integers or floats")
        #     # critcal case: matrix's list items are not numbers
        #     if type(m_b[j][i]) not in [float, int]:
        #         raise TypeError("m_b should contain only integers or floats")
            
        #     new_sum += m_a[i][j] * m_b[j][i]
        
        # new_matrix.append(new_sum)
    return new_matrix

# i = 0, j = 0, len(m_a) = 3, len(m_a[i]) = 2
# new_sum = 0

# m_a[i][j] = m_a[0][0] = 1
# m_b[j][i] = m_b[0][0] = 1

# m_a[i][j] = m_a[0][1] = 2
# m_b[j][i] = m_b[1][0] = 3

# m_a[i][j] = m_a[1][0] = 2
# m_b[j][i] = m_b[0][1] = 


# [							[ 
# 	[1, 2],						[1, 2, 3],
#  	[2, 4],						[3, 5, 7],
#   [4, 8]
# ]							]


# i = 0, j = 0
# i = 0, j = 1
# i = 1, j = 0
# i = 1, j = 1
# i = 2, j = 0
# i = 2, j = 1

# [ ( ma[i][j] * mb[j][i] ) + ( ma[i][j] * mb[j][i] ) , ( ma[i][j] * mb[j][i] ) + ( ma[i][j] * mb[j][i] ), ( ma[i][j] * mb[j][i] ) + ( ma[i][j] * mb[j][i] ) ]

# [ (ma[0][0] * mb[0][0]) + (ma[0][1] * mb[1][0]) , (ma[0][0] * mb[0][1]) + (ma[0][1] * mb[1][1]) , (ma[0][0] * mb[0][2]) + (ma[0][1] * mb[1][2]) ]
