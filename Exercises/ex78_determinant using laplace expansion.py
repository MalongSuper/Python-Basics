# 78. Determinant Using Laplace Expansion
import numpy as np
from numpy.linalg import det


def laplace_expansion(matrix, row):
    if row >= len(matrix):
        raise ValueError('Out of Range. The program cannot proceed any further')
    cofactor_matrix = []

    for i in range(len(matrix)):
        # Take sub matrix for every iteration
        sub_matrix = np.delete(np.delete(matrix, row, axis=0), i, axis=1)
        cofactor = (-1) ** (row + i) * det(sub_matrix)
        cofactor_matrix.append(cofactor)
        print(f"matrix[{row}, {i}] = {matrix[row, i]}, cofactor = {cofactor}")

    determinant = sum(matrix[row, k] * cofactor_matrix[k] for k in range(len(matrix)))
    return determinant


# Random n x n matrix
n = int(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 10, size=(n, n))
print("Matrix:\n", matrix)

# Select nth row
row = int(input("Enter row: "))
print("+ Determinant of Matrix (based on the row):", laplace_expansion(matrix, row))
print("+ Determinant of Matrix (actual):", det(matrix))
