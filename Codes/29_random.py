# Python Random Numbers
import random

# Select a random element from a sequence.
fruits = ["apple", "banana", "orange", "grape"]
print(random.choice(fruits))

word = "PYTHON"
print(random.choice(word))

# Select multiple random elements with replacement.
numbers = [1, 2, 3, 4]
print(random.choices(numbers, k=5))

# Select multiple unique random items.
students = ["Alex", "John", "Emma", "Sophia"]
print(random.sample(students, 2))

# Generate a random integer between two values (inclusive).
print(random.randint(1, 10))

# Generate a random floating-point number between 0 and 1.
print(random.random())

# Generate a random float between two numbers.
print(random.uniform(1, 5))

# Works similarly to range() but randomly selects a value.
print(random.randrange(0, 20, 2))

# Shuffle a mutable sequence like a list.
cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)

# Set a starting point for randomness. This creates constant randomness.
random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))

# Special Randomization
damage = random.randint(10, 20) * 1.5
print(damage)

# simulate dice
dice = random.randint(1, 6)
print(dice)

# create random passwords
characters = "abcdefghijklmnopqrstuvwxyz123456789"
password = "".join(random.choices(characters, k=8))
print(password)

# randomize formulas
x = random.uniform(1, 10)
result = x ** 2 + 5
print(result)
