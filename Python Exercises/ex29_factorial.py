# 29. Factorial
# Compute the factorial of a given number using iteration.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}.")
