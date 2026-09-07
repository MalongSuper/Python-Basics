# 41. GCD and LCM
# Compute the greatest common divisor
# and least common multiple of two numbers.


def greatest_common_divisor(a, b):
    gcd = 0
    if a == b:
        gcd = a

    elif a < b:
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                gcd = i

    else:
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                gcd = i

    return gcd


def least_common_multiple(a, b):
    lcm = (a * b) // greatest_common_divisor(a, b)
    return lcm


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"- The greatest common divisor is {greatest_common_divisor(a, b)}.")
print(f"- The least common multiple is {least_common_multiple(a, b)}.")
