# Creating Arrays and Matrices
import numpy as np

# Creating Arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr)

print(len(arr))      # Number of elements
print(arr.size)      # Total number of elements
print(arr.shape)     # Shape of array

# Creating Matrices
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)

# Reshaping Arrays
arr = np.array([1,2,3,4,5,6])
matrix = arr.reshape(2,3)
print(matrix)

# Flattening Matrices
flat = matrix.flatten()
print(flat)

# Random Arrays
np.random.rand(3)  # Generate random decimal values
np.random.randint(1, 10, size=5)  # Generate random integers

# Arrays Filled with Zeros or Ones
np.zeros(5)
np.ones((2, 3))

# Arrays with Ranges
np.arange(0, 10, 2)  # arange()  works similarly to Python's range()
np.linspace(0, 1, 5)    # linspace() generates evenly spaced values.
