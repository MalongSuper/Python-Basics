# Multiple If-Else Statements
# Non-Nested Conditions (Multiple Independent if Statements)
# Non-Nested: Check if a number is divisible by 2, 3, or 5

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is divisible by 2")

if number % 3 == 0:
    print(number, "is divisible by 3")

if number % 5 == 0:
    print(number, "is divisible by 5")

# The else only applies to the last if
else:
    print(number, "is not divisible by 2, 3, or 5")

# Nested Conditions (if-elif-else)
# Nested: Determine the grade level

grade = float(input("Enter your grade: "))

if grade >= 9.5:
    print('Level A+')

elif grade >= 8.0:
    print('Level A')

elif grade >= 7.0:
    print('Level B')

elif grade >= 6.5:
    print('Level C')

elif grade >= 5.0:
    print('Level D')

# The else executes when all above conditions are false
else:
    print('Level F')

# The Difference Between Non-Nested and Nested Conditions
age = int(input("Enter your age: "))

if age > 6:
    print("youngster")

if age > 12:
    print("teenager")

if age > 18:
    print("adolescent")

if age > 30:
    print("adult")

if age > 60:
    print("elder")

else:
    print("unknown")

# Example Using elif
age = int(input("Enter your age: "))

if age > 60:
    print("elder")

elif age > 30:
    print("adult")

elif age > 18:
    print("adolescent")

elif age > 12:
    print("teenager")

elif age > 6:
    print("youngster")

else:
    print("unknown")

# Logical Built-in Functions
# The any() and all() Function
score = [8.4, 7.5, 8.4, 4.7, 4.1, 5.8, 9.1, 8.5]

average = sum(score) / len(score)

print(f"Your average is {average:.1f}")

if average >= 8.0:
    print('Your average is 8.0 or above')

    if all(s >= 6.5 for s in score):
        print('All of the subject scores are 6.5 and above')
        print('Your final grade is A+')

    else:
        print('Not all of subject scores are 6.5 and above')
        print('Your final grade is A')

else:
    print('Your average is lower than 8.0')

    if any(s < 5.0 for s in score):
        print('There is at least one subject below 5.0')
        print('Your final grade is C')

    else:
        print('Your final grade is B')
