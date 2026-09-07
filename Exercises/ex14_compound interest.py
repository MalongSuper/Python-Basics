# 14. Compound Interest

P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate: ")) / 100
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the number of years: "))

A = P * (1 + (r / n)) ** (n * t)
print(f"The final amount is {A:.2f}")
