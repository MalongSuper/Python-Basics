# The calendar Module
import calendar
from datetime import datetime

# Displays the calendar of a specific month.
print(calendar.month(2026, 5))

# Displays the entire calendar of a year.
print(calendar.calendar(2026))

# Returns the weekday as an integer.
print(calendar.weekday(2026, 5, 24))

# Changes the first day of the week.
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 5))

# Returns the current first weekday setting.
print(calendar.firstweekday())

# Leap Year Functions
print(calendar.isleap(2024))
print(calendar.isleap(2025))
print(calendar.isleap(2026))

# Counts how many leap years exist between two years.
print(calendar.leapdays(2000, 2026))

# Advanced Example: Display Current Month Calendar
current = datetime.now()
print(calendar.month(current.year, current.month))
