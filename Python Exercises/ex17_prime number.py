# 17. Prime Number Checker
# Write a program that checks whether a number is prime.

is_prime = True
number = int(input("Enter a number: "))
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        print(f"{number} is not a prime number")
        break
if is_prime:
    print(f"{number} is a prime number")
