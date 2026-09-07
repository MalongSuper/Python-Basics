# Common Date Functions
from datetime import date, datetime, timedelta

# Returns the current local date and time.
current = datetime.now()
print(current)

# Returns today’s date.
today = date.today()
print(today)

# Extracting Date Elements:
current = datetime.now()
print(current.year)
print(current.month)
print(current.day)

# Formats dates into readable strings.
current = datetime.now()
formatted = current.strftime("%d/%m/%Y")
print(formatted)

# Converts strings into datetime objects.
date_string = "24-05-2026"
converted = datetime.strptime(date_string, "%d-%m-%Y")
print(converted)

# We can subtract dates to calculate durations.
date1 = datetime(2026, 5, 24)
date2 = datetime(2026, 6, 1)
difference = date2 - date1
print("Day Differences:", difference.days)

# UTC and Regional Time Conversion
utc_time = datetime.now()

vietnam_time = utc_time + timedelta(hours=7)
japan_time = utc_time + timedelta(hours=9)
uk_time = utc_time + timedelta(hours=0)
german_time = utc_time + timedelta(hours=1)
america_ny_time = utc_time - timedelta(hours=5)
america_cali_time = utc_time - timedelta(hours=8)

print("UTC:", utc_time)
print("Vietnam:", vietnam_time)
print("Japan:", japan_time)
print("United Kingdom:", uk_time)
print("Germany:", german_time)
print("New York - United States:", america_ny_time)
print("California - United States:", america_cali_time)
