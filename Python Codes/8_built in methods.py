# Built-in Methods
# print() and input()
name = input("Enter your name: ")
print("Hello", name)

# eval() with split() and map()
numbers = list(map(int, input("Enter numbers: ").split(",")))

print("Numbers:", numbers)

# min(), max(), sum(), len()
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Total:", sum(numbers))
print("Length:", len(numbers))

# sorted()
print("Sorted:", sorted(numbers))

# round()
pi = 3.1415926535
print("Rounded:", round(pi, 3))

# Data Type Conversion Methods
# Original data
x = "25"
# type()
print(type(x))
# str(), int(), float(), bool()
a = int(x)
b = float(x)
c = str(a)
d = bool(a)

print("Integer:", a)
print("Float:", b)
print("String:", c)
print("Boolean:", d)

# list(), tuple(), set()
data = [1, 2, 2, 3, 4]

print("List:", list(data))
print("Tuple:", tuple(data))
print("Set:", set(data))

# dict()
pairs = [("name", "Alex"), ("age", 20)]
print("Dictionary:", dict(pairs))

# reversed()
text = "Python"
print("Reversed List:", list(reversed(text)))

# filter()
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter List:", even)

# Advanced Methods
# ord() and chr()
print(ord('A'))
print(chr(66))

# ascii()
text = "Pythön"
print(ascii(text))

# any() and all()
conditions = [True, False, True]

print(any(conditions))
print(all(conditions))

# id()
x = [1, 2, 3]
print(id(x))

# divmod()
result = divmod(17, 5)

print("Quotient:", result[0])
print("Remainder:", result[1])

# Bytes-Coding Methods
number = 25

# bin()
print("Binary:", bin(number))
# hex()
print("Hexadecimal:", hex(number))
# oct()
print("Octal:", oct(number))

# Attributive Methods
# .split()
text = "Python is fun"
words = text.split()
print(words)

# .sort()
numbers = [5, 1, 4, 2, 3]
numbers.sort()
print("Sorted:", numbers)
# .pop(i)
numbers.pop(2)
print("Pop 2:", numbers)
# .reverse()
numbers.reverse()
print("Reversed:", numbers)

# .upper() and .lower()
name = "Iris"

print(name.upper())
print(name.lower())

# .replace(old, new)
sentence = "Python is hard"
sentence = sentence.replace("hard", "powerful")

print(sentence)
