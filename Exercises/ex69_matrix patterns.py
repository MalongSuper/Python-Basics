# 69. Matrix Patterns

def matrix_pattern1(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()


n = int(input("Enter size: "))
matrix_pattern1(n)


def matrix_pattern2(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()


n = int(input("Enter size: "))
matrix_pattern2(n)


def matrix_pattern3(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


n = int(input("Enter size: "))
matrix_pattern3(n)
