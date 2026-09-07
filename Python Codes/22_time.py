# Python Date and Time Functions
import time

# Common Time Functions
current_time = time.time()
print(current_time)

# Pauses the program for a number of seconds.
print("Start")
time.sleep(2)
print("End")

print(time.ctime())
current = time.localtime()
print(current)
print(time.asctime(current))

print(time.gmtime())

formatted = time.strftime("%Y-%m-%d %H:%M:%S", current)
print(formatted)

date_string = "24-05-2026"
converted = time.strptime(date_string, "%d-%m-%Y")
print(converted)

print(time.mktime(current))

print(current.tm_year)
print(current.tm_mon)
print(current.tm_mday)


start = time.perf_counter()
for i in range(1000000):
    pass

end = time.perf_counter()
print(end - start)

# Extract Time Elements
current = time.localtime()
print("Second:", current.tm_sec)   # Second
print("Minute:", current.tm_min)   # Minute
print("Hour:", current.tm_hour)  # Hour
print("Day:", current.tm_mday)  # Day
print("Month:", current.tm_mon)   # Month
print("Year:", current.tm_year)  # Year

# UTC Offset
utc = time.gmtime()
local = time.localtime()
print("UTC Time:")
print(time.asctime(utc))
print("\nLocal Time:")
print(time.asctime(local))
