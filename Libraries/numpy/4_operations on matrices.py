# Common Operations on Matrices
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Addition
print(A + B)
print(np.add(A, B))

# Subtraction
print(A - B)
print(np.subtract(A, B))

# Division
print(A / B)
print(np.divide(A, B))

# Element-wise Multiplication
print(A * B)
print(np.multiply(A, B))

# Scalar Multiplication
print(A * 10)
print(np.multiply(A, 10))

# Dot Product
print(np.dot(A, B))

# Outer Product
print(np.outer(A, B))
