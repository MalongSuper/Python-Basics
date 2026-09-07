# 8. Tip, Tax, and Total
# Write a program that calculates tip, tax, and final total bill.

food_cost = float(input("Enter the cost of the food: "))
tip_percent = float(input("Enter the tip percentage: "))
tax_percent = float(input("Enter the tax percentage: "))
tip = food_cost * (tip_percent / 100)
tax = food_cost * (tax_percent / 100)
total = food_cost + tip + tax
print(f"Tip: ${tip:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
