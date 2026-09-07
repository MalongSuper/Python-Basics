# Operators
# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Comparison Operations
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Boolean Operators
is_rainy = True
print(is_rainy)
if is_rainy:
    print("Bring an umbrella")

# Logical Operators
# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Boolean Operations
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > b):", not(a > b))

# Bitwise Operators
# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Bitwise Operations
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise NOT of a:", ~a)
print("Bitwise XOR:", a ^ b)
print("Right Shift:", a >> 2)
print("Left Shift:", a << 2)

# Assignment Operators
# Input value
a = int(input("Enter value for a: "))
# Basic assignment
b = a
print("Assign:", b)
# Add and assign
b += a
print("After += :", b)
# Subtract and assign
b -= a
print("After -= :", b)
# Multiply and assign
b *= a
print("After *= :", b)
# Left shift and assign
b <<= 2
print("After <<= :", b)

# Identity Operators
# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# c references the same object as a
c = a

print("a is not b:", a is not b)
print("a is c:", a is c)

# Membership Operators
# Input values
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

# List
my_list = [10, 20, 30, 40, 50]

# Membership checks
if x not in my_list:
    print("x is NOT present in the list")
else:
    print("x is present in the list")

if y in my_list:
    print("y is present in the list")
else:
    print("y is NOT present in the list")

# Ternary Operator
# Input values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Ternary operation
minimum = a if a < b else b

print("Minimum value:", minimum)

age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"

print(status)

# Other Operators
expr = 10 + 20 * 30
print(expr)

name = input("Enter name: ")
age = int(input("Enter age: "))

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)
