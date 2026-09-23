# 59. Dot Product of Three 3×3 Matrices

def dot_product(matrix1, matrix2):
  rows = len(matrix1)
  cols = len(matrix2[0])
  result_matrix = []

  for i in range(rows):
    row = []
    for j in range(cols):
      dot_product = 0
      for k in range(len(matrix2)):
        dot_product += matrix1[i][k] * matrix2[k][j]
      row.append(dot_product)
    result_matrix.append(row)

  return result_matrix


import numpy as np

# Random 3x3 matrices
matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Dot Product:\n", np.array(dot_product(matrix1, matrix2)))

matrix3 = np.random.randint(1, 10, size=(3, 3))
print("Matrix 3:\n", matrix3)
print("Dot Product:\n", np.array(dot_product(dot_product(matrix1, matrix2),
                                             matrix3)))
