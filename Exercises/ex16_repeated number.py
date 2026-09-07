# 16. Repeated Number Entry Until 0
# Write a program that continuously accepts numbers until the user enters 0.

sum_numbers = 0
counts = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    sum_numbers += number
    counts += 1
print(f"The sum of the numbers is {sum_numbers}")
print(f"The average of the numbers is {sum_numbers / counts}")
