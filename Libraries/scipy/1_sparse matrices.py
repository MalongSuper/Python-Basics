# Sparse Matrices
import numpy as np
import scipy as sp

# Dense Matrix vs Sparse Matrix
dense = np.array([[0, 1, 0],
                  [0, 0, 2],
                  [3, 0, 4]])

print("Dense Matrix:\n", dense)

sparse = sp.sparse.coo_matrix(dense)
print(sparse)
print(sparse.count_nonzero())  # Count all non-zero entries

# Count non-zeros by row or column
print(sparse.getnnz())
print(sparse.getnnz(axis=0))   # columns
print(sparse.getnnz(axis=1))   # rows

print(sparse.shape)  # Matrix shape
print(sparse.data.shape)  # Stored data size

# Converting Back to NumPy
dense_again = sparse.toarray()
print("Dense Matrix (revised):\n", dense_again)
