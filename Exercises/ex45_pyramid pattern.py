# 45. Pyramid Pattern
# Generate a centered numeric pyramid based on user input.


def draw_pattern(n):
    for i in range(1, n + 1):
        for j in range(n, i, -1):
            print(" ", end=" ")

        # Left side pyramid
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Right side pyramid
        for j in range(2, i + 1):
            print(j, end=" ")

        print()


P = int(input("Enter a number: "))
draw_pattern(P)
