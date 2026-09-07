# Loops with Conditional Statements

# Odd-Even numbers between 1 and 100

count = 0

for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1

        if count == 3:
            print()
            count = 0

# Prime numbers between 1 and 100

count = 0

for i in range(2, 101):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=" ")
        count += 1

        if count == 3:
            print()
            count = 0

# Count numbers divisible by 3, 6, and 9

count1, count2, count3 = 0, 0, 0

for i in range(3, 101):

    if i % 3 == 0:
        count1 += 1

    if i % 6 == 0:
        count2 += 1

    if i % 9 == 0:
        count3 += 1

print("Count of 3:", count1)
print("Count of 6:", count2)
print("Count of 9:", count3)

# Find the largest number in a list

sequence = [92, 51, 27, 56, 48, 18, 57, 64, 31, 8]
number = float('-inf')

# Iterate through the list and compare values
for x in sequence:
    if x > number:
        number = x

print("Largest Number:", number)

# Sum of even and odd numbers between 1 and 112

sum_of_even = 0
sum_of_odd = 0

for i in range(1, 112 + 1):
    if i % 2 == 0:
        sum_of_even += i
    else:
        sum_of_odd += i

print("Sum of even:", sum_of_even)
print("Sum of odd:", sum_of_odd)

# Greatest Common Divisor using loops

gcd = 0

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a < b:
    for i in range(1, a + 1):
        if (a % i) == 0 and (b % i) == 0:
            gcd = i
    print(f"GCD of {a} and {b} is {gcd}")

elif a > b:
    for i in range(1, b + 1):
        if (a % i) == 0 and (b % i) == 0:
            gcd = i
    print(f"GCD of {a} and {b} is {gcd}")

else:
    print(f"GCD of {a} and {b} is {a}")