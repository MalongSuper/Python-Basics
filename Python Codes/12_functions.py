# Functions
def greet():
    print("Hello World from Python")


greet()


def greet(name):
    print(f"Hello World, {name}")


greet("Alice")


def calculate(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)


calculate(x=12, y=25)
calculate(12.43, 9.11)
print(calculate(12, 25))


def display_info(name, age, city):
    return f"Hello {name}, {age}, from {city}"


name, age, city = 'Alice', 23, 'Washington D.C.'
print(display_info(name, age, city))


def area_rectangle(a, b):
    return a * b


print(f"The area of rectangle is: {area_rectangle(12, 25)}")


# Odd and Even Checker
def is_odd_even(x):
    if x % 2 == 0:
        print(x, "is an even number")
    else:
        print(x, "is an odd number")


number = int(input("Enter a number: "))
is_odd_even(number)


def is_prime(x):
    is_prime = True

    if x < 0:
        is_prime = False
    elif x == 0 or x == 1:
        is_prime = False
    elif x == 2:
        is_prime = True
    else:
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break

    return is_prime


# Prime Number Checker
number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# Recursive Function
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(10))


# Overriding Built-in Functions
def len(numbers):
    total = 0
    for i in numbers:
        total += i

    return total


values = [1, 2, 3, 4, 5]
print(len(values))


# Multiple Functions with the Same Name
def add(a, b):
    return a + b

# Python will execute this one
def add(a, b):
    return str(a) + str(b)


print(add(10, 20))


# Nested Functions
def create_student():

    def get_name():
        return "Alice"

    def get_background():
        return "Computer Science"

    student_name = get_name()
    background = get_background()

    return f"{student_name} studies {background}"


print(create_student())


# Using print() and return Together
def calculate_square(x):
    print("Calculating square...")
    return x ** 2


result = calculate_square(5)
print(result)


# Variables with Functions
def compute_salary():
    return 5000


salary = compute_salary()

print(salary)
print(salary ** 2)


# Using Functions Inside Loops
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


prime_numbers = []

for i in range(1, 51):
    if is_prime(i):
        prime_numbers.append(i)

print(prime_numbers)


# Returning Multiple Values
def compute_squares(a, b, c):
    square_a = a ** 2
    square_b = b ** 2
    square_c = c ** 2

    return square_a, square_b, square_c


x, y, z = compute_squares(2, 3, 4)
total = x + y + z
print("The total is:", total)


# Returning Values as a Collection
def compute_squares(a, b, c):
    return a ** 2, b ** 2, c ** 2


values = compute_squares(2, 3, 4)
print(values)
