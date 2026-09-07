# Common Types of Matrices
import numpy as np

# Square Matrix: A matrix with equal numbers of rows and columns.
square = np.array([[1,2], [3,4]])
print(square)

# Diagonal Matrix: All non-diagonal elements are zero.
diag = np.diag([1,2,3])
print(diag)

# Identity Matrix: A special diagonal matrix
# where all diagonal entries are 1.
identity = np.identity(3)
print(identity)

# Triangular Matrix:  This is a square matrix
# where either the upper half or lower half is only zeros
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(np.triu(A))
print(np.tril(A))

# Transpose Matrix: Rows become columns and columns become rows.
A = np.array([[1,2,3],
              [4,5,6]])

print(np.transpose(A))
