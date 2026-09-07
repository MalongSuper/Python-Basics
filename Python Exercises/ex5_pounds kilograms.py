# 5. Pounds and Kilograms Conversion
# Write a program that converts pounds to kilograms or kilograms to pounds.

pounds = float(input("Enter the weight in pounds: "))
kilograms = pounds * 0.453592
print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms")

kilograms = float(input("Enter the weight in kilograms: "))
pounds = kilograms / 0.453592
print(f"{kilograms} kilograms is equal to {pounds:.2f} pounds")
