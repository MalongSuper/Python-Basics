# Common Format Techniques
name = "Alice"
age = 21

print("My name is", name, "and I am", age, "years old.")

print("My name is %s and I am %d years old!" % ('Michael', 21))
print("This is %s and she is learning %s" % ('Alice', 'Python'))

name = "Johnny"
print("Hello " + name)

age = 20
print("I am " + str(age) + " years old.")


# The format() Method
name = "Maria"
age, major = 23, 'IT'

print("Hello! My name is {} and my age is {} years".format(name, age))
print("And my major is {}".format(major))

name = ["A", "B", "C", "D", "E", "F"]
age = [21, 19, 19, 18, 19, 20]

for i in range(len(name)):
    print('{} {}'.format(name[i], age[i]))

name = ["A", "B", "C", "D", "E", "F"]
age = [21, 19, 19, 18, 19, 20]

for i in range(len(name)):
    print('{:<10} {:>15}'.format(name[i], age[i]))

# The f-string
name = 'Johnny'

print(f'Hello {name}.')
print(f'The value is {10 + 2}.')

name = "Maria"
age, major = 23, 'IT'
height, weight = 178, 67

print(f"Hello, I am {name}, {age} years old, and my major is {major}")
print(f"My height and weight is ({height}, {weight})")

x = 10
y = 5

print(f"The sum of x and y is {x + y}")

num = 123.456789
# .2f means round the value to 2 decimal places
print(f'{num:.2f}')
num = 1000000.00
print(f'{num:,.2f}')

discount = 0.5
print(f'{discount:.0%}')

num = 123456789
print(f'{num:,d}')

num = 12345.6789
print(f'{num:.2e}')


# Escape Characters
print("This is: \nPython Programming")

print("This is Python Programming")
print("\nBy Alice Brants")

print("This is:\tPython Programming")
print("\tThis is: Python Programming")
print("This\tis:\tPython\nProgramming")

print("This is:\t\tPython Programming")
print("This is:\n\nPython Programming")
print("This is:" + '\t' * 5 + "Python Programming")

print("This is:Python\rProgramming")
print("This is: \rPython Programming")

print("This is not Python\r")
print("This is \n not\rPython")
print("This is not\r\tPython")

print("This is:Python\bProgramming")
print("This is: \tPython\bProgramming")

print("This is not Python\b")
print("This\bis \n not\rPython")
print("This is not\r\tPython\b")

# This program displays Welcome to Python -> single-line comment
print("Welcome to Python")
print("Python is fun")

''' This program displays Welcome to Python and
Python is fun -> multi-line comments
'''
print("Welcome to Python")
print("Python is fun")
