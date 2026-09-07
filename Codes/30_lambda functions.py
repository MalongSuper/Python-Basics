# Python Lambda Functions
from functools import reduce

square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(3, 5))

multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))

greet = lambda name: "Welcome " + name
print(greet("Iris"))

equation = lambda x: x ** 2 + 5
print(equation(3))

check = lambda age: "Adult" if age >= 18 else "Minor"
print(check(20))
print(check(12))

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)


# Summing a list
number1 = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, number1)
print("Total:", total)
# Finding the maximum value
number2 = [5, 12, 8, 20, 3]
max_val = reduce(lambda a, b: a if a > b else b, number2)
print("Max Value:", total)


# Define a Function then Use Lambda
def power(n):
    return lambda x: x ** n


square = power(2)
cube = power(3)

print(square(4))
print(cube(2))


# Sorting a List with Lambda
students = [("John", 75), ("Emma", 92), ("Alex", 81)]
students.sort(key=lambda x: x[0])
print(students)

# Sorting Tuples Based on Second Number
data = [(1, 5), (1, 2), (1, 9), (1, 1)]
result = sorted(data, key=lambda x: x[1])
print(result)

# Reversing with Lambda
words = ["apple", "banana", "orange"]
words.sort(key=lambda x: x[::-1])
print(words)

# Returning Multiple Results
values = lambda x: (x, x ** 2, x ** 3)
print(values(3))
