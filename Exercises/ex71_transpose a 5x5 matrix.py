# 71. Transpose a 5×5 Matrix
import numpy as np


def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Random 5x5 matrix
matrix = np.random.randint(1, 10, size=(5, 5))
print("Original Matrix:\n", matrix)

transpose_matrix(matrix)
print("Transposed Matrix:\n", np.array(matrix))
