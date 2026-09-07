# 31. Numbered Pattern
# Generate a descending triangular number pattern based on user input.

def display_pattern(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            # This part uses to space the pattern
            print(format("  "), end="")
        for k in range(i, 0, -1):
            print(format(k, '2d'), end="")
        print()


n = int(input("Enter a number: "))
display_pattern(n)
