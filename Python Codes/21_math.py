# Python Mathematical Functions
import math


# Built-in Mathematical Functions
print(abs(-15))
print(divmod(17, 5))

numbers = [5, 1, 9, 3]
print(max(numbers))
print(min(numbers))

print(pow(2, 5))
print(round(3.141592, 2))

numbers = [1, 2, 3, 4]
print(sum(numbers))

num_list = [1, 2, 3, 4, 5, 5, 8, 9, 9, 10]


def square(x):
    return x ** 2


squared_list = list(map(square, num_list))
print(squared_list)

num_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x ** 2, num_list))
print(squared_list)

# Functions from the math Library
# Number-Theoretic and Rounding Functions
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.comb(5, 2))
print(math.factorial(5))
print(math.gcd(24, 36))
print(math.isclose(0.1 + 0.2, 0.3))
print(math.prod([1, 2, 3, 4]))

# Power, Exponential, and Logarithmic Functions
print(math.sqrt(25))
print(math.cbrt(27))
print(math.exp(2))
print(math.log(8, 2))
print(math.log10(1000))
print(math.log2(16))

# Trigonometric and Angular Conversion Functions
print(math.sin(math.radians(90)))
print(math.cos(math.radians(90)))
print(math.tan(math.radians(90)))
# Cotane
print(1 / math.tan(math.radians(90)))

# Special Cases
print(math.sin(math.pi / 2))
print(math.cos(math.pi))
print(math.tan(math.pi / 4))

print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.atan2(1, 1))
print(math.degrees(math.pi))
print(math.radians(180))
print(math.hypot(3, 4))

# Mathematical Constants
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
