# 86. Inverse Matrix Using Cofactor Method
import numpy as np
from numpy.linalg import det


def inverse_matrix_cofactor(matrix):
    n = len(matrix)
    if n == 0:
        raise ValueError("Empty matrix has no inverse.")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to find its inverse.")

    det_matrix = round(det(matrix))
    if det_matrix == 0:
        print("Determinant is 0, the matrix is non-invertible")
        return None

    # Handle 1x1 matrix case separately
    if n == 1:
        return np.array([[1 / matrix[0, 0]]])

    cofactors = []  # Store the cofactors
    for i in range(n):  # Iterate each element in the matrix
        for j in range(n):
            M = np.delete(matrix, i, 0)  # Remove row i
            M = np.delete(M, j, 1)  # Remove column j
            A = ((-1) ** (i + j)) * det(M)
            cofactors.append(round(A))  # Append the cofactors

    # Transpose to get the adjugate matrix
    cofactor_matrix = np.array(cofactors).reshape(n, n)
    adjugate_matrix = np.transpose(cofactor_matrix)

    # Find the inverse matrix
    inverse_matrix = (1 / det_matrix) * adjugate_matrix
    return inverse_matrix


n = int(input("Enter size of the matrix: "))

# Form a matrix of order n
matrix = np.random.randint(0, 10, size=(n, n))
print("Matrix:\n", matrix)

# Calculate and print the inverse matrix
result_inverse_matrix = inverse_matrix_cofactor(matrix)

if result_inverse_matrix is not None:
    print("Inverse Matrix:\n", np.round(result_inverse_matrix, 2))

# Use numpy's inverse function
np_inverse = np.linalg.inv(matrix)
print("\nSolution using NumPy:\n", np.round(np_inverse, 2))
