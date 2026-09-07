# 26. Lap Times Simulation
# Simulate jogging lap times with varying speed
# and determine the best lap time.
import random


def lap_times(distance, number_of_laps, speed=45):
    seconds = []
    for i in range(number_of_laps):
        sec = distance / speed
        print(f"+ Lap {i}: {sec} sec")
        seconds.append(sec)
        # Randomly change the speed for the next lap
        speed = random.uniform(40, 50)

    # Return the best lap
    return min(seconds), seconds.index(min(seconds)) + 1


distance = float(input("Enter the distance in meters: "))
number_of_laps = int(input("Enter the number of laps: "))
min_seconds, best_lap = lap_times(distance, number_of_laps)
print(f"- The best lap is lap {best_lap} with {min_seconds} seconds.")
