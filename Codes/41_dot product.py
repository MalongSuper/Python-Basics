# Dot Product

matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 8],
    [0, 0, 9, 0, 3]
]


matrix2 = [
    [1, 0, 2, 1, 0],
    [0, 1, 3, 0, 1],
    [1, 1, 0, 2, 0],
    [0, 0, 1, 1, 2],
    [2, 0, 0, 1, 1]
]


# Element-Wise Multiplication
result = [[matrix1[i][j] * matrix2[i][j] for j in range(len(matrix1[0]))]
          for i in range(len(matrix1))]

for i in range(len(result)):
    print(result[i])


# Matrix Multiplication
rows = len(matrix1)
cols = len(matrix2[0])

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(len(matrix2)):
            total += matrix1[i][k] * matrix2[k][j]
        row.append(total)
    result.append(row)

for row in result:
    print(row)
