# 9. Male and Female Percentages
# Write a program that displays the percentage
# of males and females in a class.

male = int(input("Enter the number of males in the class: "))
female = int(input("Enter the number of females in the class: "))
total = male + female
print(f"Percentage of males: {male / total * 100:.2f}%")
print(f"Percentage of females: {female / total * 100:.2f}%")
