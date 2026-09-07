# Data Types
print("Python")     # This is a string
print(3)            # This is an integer
print(3.12)         # This is a float
print(True, False)  # These are booleans
print(None)         # Represents no value

print([1, 2, 3])                 # List
print((1, 2, 3))                 # Tuple
print({1, 2, 3})                 # Set
print({"Name": "Alice"})         # Dictionary

num = 10

print(str(num))
print(float(num))
print(bool(num))

print(str(100))
print(str(True))
print(str([1, 2, 3]))

num1 = 1.2
print(int(num1))

num2 = 1.5
print(int(num2))

num3 = 1.9
print(int(num3))

print(int('1'))
print(float('1.4'))

print("12330110")
print(int("12330110"))

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(name, age)

# The type() Method
print(type('Hello'))
print(type(2))
print(type(True))
print(type(None))
print(type(2.5))

print(type(['Hello', 'Goodbye']))
print(type((1, 2, 3)))
print(type({1, 2, 4, 5}))
print(type({'Name': 'Chris', 'Age': 30}))

print(type([[1, 2], [4, 5]]))
print(type([("Alice", 25), ("Bob", 30)]))
print(type({(1, 2), (2, 3), (3, 4)}))

# Operations Between Data Types
print(int(12), int("12"))
print(str("12") + str("13.3"))

print(int(1) + int("1"))
print(float("3.13") + int(432))

# bool(True) returns 1
# bool(False) returns 0
print(bool(True) + bool(False))
print(bool(True) + bool(False) * 1000)

string1 = " "
print(bool(string1))

string2 = 0
print(bool(string2))

string3 = 1
print(bool(string3))

string4 = -1
print(bool(string4))

string5 = None
print(bool(string5))

string6 = 1.0
print(bool(string6 + string6))

# The round() Method
x = round(5.1245, 2)
print(x)

y = round(5.773831883, 4)
print(y)

z = round(6.532)
print(z)

x1, y1 = 7.5, 5.5
x2, y2 = 6.5, 4.5

print(round(x1), round(y1))
print(round(x2), round(y2))
print(round(x1 + y1 + 0.5))
print(round(x2 - y2 + 0.5))
