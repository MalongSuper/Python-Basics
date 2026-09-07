# 1. Single Line Input: Name, Age, Major
# Write a program that prompts the user to enter their name, age, and major
# in a single line input. Display all values clearly.

name, age, major = input("Enter your name, age, and major "
                         "separated by spaces: ").split(", ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
