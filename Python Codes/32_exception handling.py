# Python Exception Handling

# The try-except Method
# Handling Multiple Errors
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Success! Result is:", result)


# Printing the Actual Error
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as e:
    print("An error occurred:")
    print(e)
    print(type(e))


# Difference Between else and finally
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid number entered.")

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

# The raise Method
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative.")
print("Age accepted.")

# Triggering Custom Errors — Better Than Complex if-else
score = int(input("Enter score: "))

if score < 0:
    print("Invalid")
else:
    print("Accepted")

# with exceptions
if score < 0:
    raise ValueError("Score cannot be negative.")
print("Valid score.")

# Re-Raising Exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Logging the error...")
    raise
