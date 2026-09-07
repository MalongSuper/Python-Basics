# Simple Stopwatch Conversion
import time

start = time.time()
input("Press Enter to stop the timer...")
end = time.time()

elapsed = end - start

minutes = elapsed / 60
hours = elapsed / 3600
print(f"Seconds: {elapsed:.2f}")
print(f"Minutes: {minutes:.2f}")
print(f"Hours: {hours:.4f}")
