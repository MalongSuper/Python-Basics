# Simple Countdown
import time

count = 10

while count > 0:
    print(count)
    # time.sleep(1) pauses the program for exactly 1 second
    # After waiting, the counter decreases by 1
    # The loop repeats until the countdown reaches 0
    time.sleep(1)
    count -= 1

print("Time's up!")
