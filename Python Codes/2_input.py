# The input() statement
print(input("Enter something: "))

string = input("Enter a String: ")
print(string)

name = input("Enter your name: ")
print("Hello", name, "!")

age = input("Enter age: ")
print(type(age))

# Add a data type before the input()
name = str(input("Enter Name: "))
age = int(input("Enter Age: "))
salary = float(input("Enter Salary: "))

print(name, age, salary)

top_speed = float(input("Enter the top speed: "))
distance = float(input("Enter the distance: "))

# Calculation
print('The top speed is', top_speed)
print('The distance traveled is', distance)
print('The estimated time to reach the distance is', distance / top_speed)

# Common Operators
a = float(input("Enter a: "))
b = float(input("Enter b: "))

print("a + b:", a + b)   # Addition
print("a - b:", a - b)   # Subtraction
print("a * b:", a * b)   # Multiplication
print("a / b:", a / b)   # Division
print("a // b:", a // b)  # Floor Division
print("a ** b:", a ** b)  # Exponentiation
print("a % b:", a % b)   # Remainder
