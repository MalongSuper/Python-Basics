# 18. Palindrome Number Checker
# Write a program that checks whether a number is a palindrome.

def is_palindrome(number):
    return str(number) == str(number)[::-1]


number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome")
