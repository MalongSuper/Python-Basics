# 25. Time Conversion
# Convert seconds into minutes, hours, and days.

seconds = int(input("Enter the amount of seconds: "))

# Compute minutes, hours, and days
minutes = seconds / 60
hours = seconds / 3600
days = seconds / 86400
print(f"The amount of seconds in minutes is {minutes:.2f}")
print(f"The amount of seconds in hours is {hours:.2f}")
print(f"The amount of seconds in days is {days:.2f}")

days = int(input("Enter the number of days: "))
# Convert to month
print(f"Month: {days / 31:.2f}")
# Convert to year
print(f"Year: {days / 365:.2f}")

# Convert days, hours, minutes, seconds -> seconds
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
print(f"Total seconds: {total_seconds}")
