# 15. Odd and Even
# Write a program that determines whether a number is odd or even.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
