# Indexing and Slicing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1])
print(arr[1:4])
print(arr[2:])
print(arr[:3])
print(arr[::2])

matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

# Row index 0
print(matrix[0])
# Element at row index 1, column index 2
print(matrix[1, 2])
# Entire rows
print(matrix[1, :])
# Entire columns
print(matrix[:, 1])
