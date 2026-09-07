# 24. Money Counting Game
# Convert dollars into pennies, nickels, dimes, and quarters.

dollars = float(input("Enter the amount of money in dollars: "))

# Compute cents, pennies, nickels, dimes, and quarters
cents = int(dollars * 100)
# Conversion
pennies = cents
nickels = cents // 5
dimes = cents // 10
quarters = cents // 25

print(f"The amount of money in cents is {cents:.2f}")
print(f"The amount of money in pennies is {pennies:.2f}")
print(f"The amount of money in nickels is {nickels}")
print(f"The amount of money in dimes is {dimes}")
