# Python Multi-Dimensional Lists

distances = [
    [0, 983, 787, 714, 1375, 967, 1087],
    [983, 0, 214, 1102, 1505, 1723, 1842],
    [787, 214, 0, 888, 1549, 1548, 1627],
    [714, 1102, 888, 0, 661, 781, 810],
    [1375, 1505, 1549, 661, 0, 1426, 1187],
    [967, 1723, 1548, 781, 1426, 0, 239],
    [1087, 1842, 1627, 810, 1187, 239, 0]
]

cities = ["Chicago", "Boston", "New York", "Atlanta",
          "Miami", "Dallas", "Houston"]

# Displaying the Distance Table
print(f"{'':12}", end="")
for city in cities:
    print(f"{city:12}", end="")
print()
for i in range(len(distances)):
    print(f"{cities[i]:12}", end="")
    for value in distances[i]:
        print(f"{value:12}", end="")
    print()


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 8],
    [0, 0, 9, 0, 3]
]

# Traversing Every Element
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# Return shape of the matrix
def shape(matrix):
    return len(matrix), len(matrix[0])


print("Length of row:", shape(matrix)[0])
print("Length of column:", shape(matrix)[1])
# Total elements
print("Total elements:", shape(matrix)[0] * shape(matrix)[1])

# Finding the Sum of Each Row
for i, row in enumerate(matrix):
    print(f"Row {i}: {sum(row)}")


# Finding the Sum of Each Column
# Sum of Columns
for j in range(len(matrix[0])):
    column_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Column {j}: {column_sum}")


# Finding the Row and Column with the Largest Sum
largest_row = 0
largest_sum_row = sum(matrix[0])
largest_col = 0
largest_sum_col = sum(matrix[i][0] for i in range(len(matrix)))

for i, row in enumerate(matrix):
    row_sum = sum(row)
    if row_sum > largest_sum_row:
        largest_sum_row = row_sum
        largest_row = i

for j in range(len(matrix[0])):
    column_sum = sum(matrix[i][j] for i in range(len(matrix)))
    if column_sum > largest_sum_col:
        largest_sum_col = column_sum
        largest_col = j

print(f"Largest row: {largest_row}; Sum: {largest_sum_row}")
print(f"Largest column: {largest_col}; Sum: {largest_sum_col}")

# Retrieving the Diagonal Elements
for i in range(len(matrix)):
    print(matrix[i][i], end=" ")

# Sorting Rows
matrix.sort(key=sum)
for row in matrix:
    print(row)

# Sorting Columns
for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    column.sort()
    print(column)


# Transpose
def transpose():
    return [[matrix[j][i] for j in range(len(matrix))]
          for i in range(len(matrix[0]))]


for row in transpose():
    print(row)
