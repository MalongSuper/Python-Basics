# Time Conversion
import time

start = time.time()
time.sleep(120)
end = time.time()

elapsed_seconds = end - start

minutes = elapsed_seconds / 60
print("Seconds:", elapsed_seconds)
print("Minutes:", minutes)

# Convert Seconds into Milliseconds
start = time.time()
time.sleep(2)
end = time.time()

elapsed_seconds = end - start
milliseconds = elapsed_seconds * 1000
print("Milliseconds:", milliseconds)
