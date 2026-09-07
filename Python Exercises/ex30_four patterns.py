# 30. Number Patterns
# Create four different number patterns
# using nested loops and separate functions.

# Pattern 1
for i in range(1, 7):
    for j in range(i):
        j += 1
        print(format(j, '2d'), end="")
    print()

print()

# Pattern 2
for i in range(7, 1, -1):
    for j in range(i - 1):
        j += 1
        print(format(j, '2d'), end="")
    print()

print()

# Pattern 3
for i in range(1, 7):
    for j in range(6 - i):
        print(format("  "), end="")
    for k in range(i, 0, -1):
        print(format(k, '2d'), end="")
    print()

print()

# Pattern 4
for i in range(7, 1, -1):
    for j in range(7 - i):
        print(format("  "), end="")
    for k in range(i - 1):
        k += 1
        print(format(k, '2d'), end="")
    print()

print()
