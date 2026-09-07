# 19. Fibonacci Sequence Checker
# Write a program that checks whether a number
# belongs to the Fibonacci sequence.


# Retrieve all the numbers in the fibonacci sequence as a list using recursion
def get_fibonacci(n):
    sequence = []

    for i in range(0, 10 ** 3):
        sequence.append(0)
        if i == 0:
            sequence[i] = 0
        elif i == 1:
            sequence[i] = 1
        else:
            sequence[i] = sequence[i - 1] + sequence[i - 2]

    if n in sequence:
        print(f"{n} belongs to the Fibonacci sequence")
    else:
        print(f"{n} does not belong to the Fibonacci sequence")


n = int(input("Enter a number: "))
get_fibonacci(n)
