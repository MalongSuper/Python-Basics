# List Comprehension

# Creating a List using a Loop
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

numbers = [i for i in range(1, 6)]
print(numbers)

# Creating Squares of Numbers
squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

squares = [i ** 2 for i in range(1, 6)]
print(squares)


# Applying Conditions using if
even_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Applying if-else in List Comprehension
result = []

for i in range(1, 6):
    if i % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

print(result)

result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)

# Creating Lists from Another List
numbers = [1, 2, 3, 4, 5]
double_numbers = [i * 2 for i in numbers]
print(double_numbers)

# Converting Strings to Uppercase
names = ['iris', 'python', 'machine learning']
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

# Nested List Comprehension
pairs = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print(pairs)
