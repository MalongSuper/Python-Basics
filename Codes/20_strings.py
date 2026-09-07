# Python Strings
a = 10
b = 20
print(a + b)

# with strings, + performs concatenation
a = "10"
b = "20"
print(a + b)

first_name = "Iris"
last_name = "Academy"
print(first_name + " " + last_name)

# f-Strings
name = 'Iris'
message = f'My name is "{name}"'
print(message)

# Operations on Strings
# String Variables
# String in Python - String can be anything
string1 = "Hello World"
string2 = "Welcome to my world"
string3 = "12"
print(string1)
print(string2)
print(string3)

# convert numbers into strings, or vice versa
number = 100
print(str(number))
print(type(str(number)))

print(int("25"))
print(float("3.14"))

# String Concatenation (+)
string1 = "Hello, and Welcome to"
string2 = " My World"
print(string1 + string2)

# String Repetition (*)
string3 = "Python "
print(string3 * 5)

# Indexing and Slicing in a String
string = "Welcome to my world, welcome to Python"

print("Length:", len(string))  # Includes spaces
print("Length (no spaces):", len(string.replace(" ", "")))

print(string[0:4])     # Characters from index 0 to 3
print(string[2:24])    # Characters from index 2 to 23
print(string[:-1])     # Everything except the last character

# Comparing Strings
string1 = "Hello World"
string2 = "Welcome to my world"
print(string1 == string2)
print(string1 != string2)
print(string1 > string2)
print(string1 < string2)

string3 = "Hello world"
print(string1 == string3)  # Case-sensitive
print(string1 > string3)
print(string1 < string3)

# Substring
string1 = "Hello World"
string2 = "Welcome to my World"

print("World" in string1)
print("World" in string2)
print("Hello World" in string2)

# Join a List into a String
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
              'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
              'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

month_list = list(month_dict.keys())
print(', '.join(str(i) for i in month_list))

# Splitting Strings
string = "Welcome to my world, welcome to Python"
# Count words
print(len(string.split()))


# Using split() for Multiple Inputs
def display_student_info(name, age, city, major):
    print("-" * 20)
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Major:", major)
    print("-" * 20)


name, age, city = input("Enter your name, age, and city: ").split(",")
major = input("Enter your major: ")
display_student_info(name, age, city, major)

# Replacing Strings
string1 = "Hello World"
print(string1.replace("World", "Python"))

string2 = "welcome to my world, Welcome to Python"
print(string2.replace("welcome to", "Hi"))

# Unicode in Python
import string
# Unicode values from a to z
string_list = list(string.ascii_lowercase)
count = 0

for i in string_list:
    print(ord(i), end=", ")
    count += 1

    if count == 5:
        print()
        count = 0

print()

# Characters from Unicode 50 to 65
for j in range(50, 66):
    print(chr(j), end=", ")


# Other Methods on Strings
string = "I am Alice, 29 years old"

# modify letter casing
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Capitalized:", string.capitalize())

# search inside strings
print("Index of 'Alice':", string.find("Alice"))
print("Starts with 'I am':", string.startswith("I am"))
print("Ends with 'Python':", string.endswith("Python"))

# validate string content
print("Count of 'a':", string.count("a"))

sample1 = "Alice"
sample2 = "123"
sample3 = "Alice123"

print(f"'{sample1}' only contains letters:", sample1.isalpha())
print(f"'{sample2}' only contains digits:", sample2.isdigit())
print(f"'{sample3}' contains letters & digits:", sample3.isalnum())
