# Linear Algebra
import numpy as np

# Determinant
A = np.array([[1, 2, 3],
              [3, 4, 3],
              [6, 6, 7]])

print(np.linalg.det(A))

# Inverse Matrix
A_inv = np.linalg.inv(A)
print(A_inv)

# Solving Systems of Linear Equations
A = np.array([[1,1], [2,1]])
B = np.array([5,8])
solution = np.linalg.solve(A,B)
print(solution)

# Eigenvalues and Eigenvectors
A = np.array([[4, 2, 3],
              [1, 3, 3],
              [2, 6, 1]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
