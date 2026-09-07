# 50. Time Breakdown
# Display current time and break it into year, month, week,
# and time components.
import time


def get_time_components(current_time):
    year = current_time.tm_year
    month = current_time.tm_mon
    week = current_time.tm_wday
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    return year, month, week, hour, minute, second


# Get current time
current_time = time.localtime()
year, month, week, hour, minute, second = get_time_components(current_time)

print("Year:", year)
print("Month:", month)
print("Week:", week)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
