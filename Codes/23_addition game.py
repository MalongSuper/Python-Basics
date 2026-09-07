# Addition Game
import time

score = 0

print("=== Addition Game ===")
print("Answer 10 questions as fast as possible!")

start_time = time.time()

for i in range(1, 11):
    num1 = i * 2
    num2 = i * 3
    answer = int(input(f"Question {i}: {num1} + {num2} = "))

    if answer == num1 + num2:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

end_time = time.time()
total_time = end_time - start_time

print("\nGame Finished!")
print(f"Score: {score}/10")
print(f"Time Taken: {total_time:.2f} seconds")
