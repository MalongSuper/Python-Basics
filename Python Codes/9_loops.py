# Loops

# Iterates from 0 to 4
for i in range(5):
    print(i)

# Iterates from 2 to 10 with step size 2
for i in range(2, 11, 2):
    print(i)

s = [1, 2, 3, 4, 5, 6]

for i in range(len(s)):
    print(s[i])

s = [1, 2, 3, 4, 5, 6]

for i in range(len(s)):
    # The end= puts all output in a single row
    print(s[i], end=' ')

print()  # Create a space

for j in range(len(s)):
    print(s[j], end=' & ')


fruits = ['apple', 'banana', 'orange', 'mango']

for fruit in fruits:
    print(fruit)

for index, value in enumerate(fruits):
    print(index, value)


# Asking the user for a password until it's correct
password = ""

# Password Checking with Loops
while password != "myname123":
    password = input("Enter the password: ")
    if password != "myname123":
        print("Wrong password, try again!")

print("Access granted!")


# Calculation of all numbers
# Stop when the user enters 0
number = 1

while number != 0:
    number = int(input("Enter a number: "))
    if number != 0:
        print(number)

print("End Loop")


i = 10
count = 0

while i > -10:
    if i == 0:
        print("Reaches 0 at iteration:", count)
        break

    count += 1
    i -= 1

# Continuously compute 1 + 2 + 3 + ... + n
# Stop when the sum reaches 1000
j = 0

for i in range(1, 101):
    j += i
    if j >= 1000:
        print("Reaches 1000 at number", i)
        break

i = 0
while i < 20:
    if i % 2 != 0:
        i += 1
        continue

    print(i)
    i += 1

# Print Odd Numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i, end=" ")