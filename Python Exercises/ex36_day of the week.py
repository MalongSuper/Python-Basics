# 36. Zeller's Congruence - Day of the Week
# Determine the day of the week for a given date using Zeller’s formula.


def zellers_congruence(day, month, year):
    days = ["Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday"]

    if month <= 2:
        year -= 1
        month += 12

    q = day
    m = month
    k = year % 100
    j = year // 100

    h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

    return days[h]


day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print(f"- The day of the week is {zellers_congruence(day, month, year)}.")
