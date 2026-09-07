# Assertion Methods
number = 10
assert number > 0
print("Valid number")

number = 5  # number = -5 raises error
assert number > 0, "Number must be positive"

# Using assert for Validation
age = int(input("Enter your age: "))
assert age >= 0, "Age cannot be negative"
print("Valid age")


# Using assert to Test Functions
def add(a, b):
    return a + b


assert add(2, 3) == 5
print("Function works correctly")


# Detecting Incorrect Function Results
def multiply(a, b):
    return a + b


# assert multiply(2, 3) == 6 raises error
assert multiply(2, 3) == 5, "Function calculation is incorrect"


# Combining try-except and assert
try:
    score = int(input("Enter score: "))
    assert score >= 0, "Score cannot be negative"
    print("Valid score")
except ValueError:
    print("Please enter a valid number")
except AssertionError as e:
    print(e)
