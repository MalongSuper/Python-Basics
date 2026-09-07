# Modifying Multi-Dimensional Lists

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 8],
    [0, 0, 9, 0, 3],
]

# Appending new row
matrix.append([8, 8, 8, 8, 8])
print(matrix)

# Appending a New Column
for i in matrix:
    i.append(10)
print(matrix)

# Appending a Single Element
matrix[0].append(99)
print(matrix)

# Replacing Elements
matrix[1][1] = 100

# Replacing an Entire Row
matrix[2] = [9, 9, 9, 9, 9]
print(matrix)

# Replacing an Entire Column
for i in matrix:
    i[2] = 99
print(matrix)

# Reversing Rows
for i in matrix:
    i.reverse()
print(matrix)


# Reversing the Order of Rows
matrix.reverse()