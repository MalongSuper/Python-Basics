# 56. Determinant of a 3×3 Matrix
import numpy as np


def create_matrix(matrix):
    # Take the first and second column of the matrix
    column1 = np.array(matrix[:, 0])
    column2 = np.array(matrix[:, 1])

    # Add them to the right of column three
    new = np.insert(matrix, 3, column1, axis=1)
    new_matrix = np.insert(new, 4, column2, axis=1)

    return new_matrix


def rule_of_sarrus(matrix):
    new_matrix = create_matrix(matrix)
    i = 0
    # For the main diagonal
    a11, a22, a33 = new_matrix[i][0], new_matrix[i + 1][1], new_matrix[i + 2][2]
    a12, a23, a34 = new_matrix[i][1], new_matrix[i + 1][2], new_matrix[i + 2][3]
    a13, a24, a35 = new_matrix[i][2], new_matrix[i + 1][3], new_matrix[i + 2][4]

    # Calculate the product of each lines
    main_product1 = np.prod(np.array([a11, a22, a33]))
    main_product2 = np.prod(np.array([a12, a23, a34]))
    main_product3 = np.prod(np.array([a13, a24, a35]))

    # Calculate the summation of the products
    main_diagonal = sum([main_product1, main_product2, main_product3])

    # For the anti-diagonal
    a13, a22, a31 = new_matrix[i][2], new_matrix[i + 1][1], new_matrix[i + 2][0]
    a14, a23, a32 = new_matrix[i][3], new_matrix[i + 1][2], new_matrix[i + 2][1]
    a15, a24, a33 = new_matrix[i][4], new_matrix[i + 1][3], new_matrix[i + 2][2]

    # Calculate the product of each lines
    anti_product1 = np.prod(np.array([a13, a22, a31]))
    anti_product2 = np.prod(np.array([a14, a23, a32]))
    anti_product3 = np.prod(np.array([a15, a24, a33]))
    anti_diagonal = sum([anti_product1, anti_product2, anti_product3])

    # Subtract the main_diagonal and anti_diagonal to get the determinant
    determinant = main_diagonal - anti_diagonal

    return determinant


matrix = np.random.randint(1, 10, size=(3, 3))
print("Matrix:\n", matrix)
print("Determinant:", rule_of_sarrus(matrix))
