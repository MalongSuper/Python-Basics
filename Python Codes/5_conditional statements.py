# If-Else Statements
i = int(input("Enter a number: "))

if i >= 10:
    print(i, "is equal to or greater than 10")
else:
    print(i, "is not greater than 10")


# Determine Odd and Even Number
number = int(input("Enter a number: "))

if number % 2 != 0:
    print(number, "is an odd number")
else:
    print(number, "is an even number")


# Password Checking Example
password = input("Enter the password: ")

if password == "iris123":
    print("Access Granted")
else:
    print("Incorrect Password")


# Boolean Conditional Statements
# The and Operator
x = int(input("Enter a number x: "))

if (x > 10) and (x % 2 == 0):
    print('The number is greater than 10 and is an even number')
else:
    print('The number is not greater than 10 or is not an even number')

# The or Operator
y = int(input("Enter a number y1: "))

if (y > 10) or (y % 2 != 0):
    print('The number is greater than 10 or is not an even number')
else:
    print('The number is not greater than 10 and is an even number')

# Leap Year Example
year = int(input("Enter a year: "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# The not Operator
number = int(input("Enter a number: "))

if not (number % 2 == 0):
    print(number, "is an odd number")
else:
    print(number, "is not an odd number")

# Membership Conditional Statements
# The in Operator
list_of_fruits = ['apple', 'banana', 'cherry']
fruit = 'apple'

if fruit in list_of_fruits:
    print("Yes,", fruit, "is in the list")
else:
    print("No,", fruit, "is not in the list")

# The not in Operator
month = int(input("Enter a month: "))

list_of_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if month not in list_of_months:
    print(month, 'is not a month')
else:
    print('Month is', month)

# Membership Operators with Strings
sentence = "This is Python Programming. Hello!! My name is Iris"

if "Python" in sentence:
    print("Python was found in the sentence")
else:
    print("Python was not found")

sentence = "This is Python Programming. Hello!! My name is Iris"

if "Java" not in sentence:
    print("Java was not found in the sentence")
else:
    print("Java exists in the sentence")
