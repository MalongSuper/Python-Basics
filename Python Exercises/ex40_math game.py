# 40. Math Game
# Play a timed addition and subtraction quiz
# until the user answers incorrectly.
import random


def math_game():
    score = 0
    game_over = False
    operator = ["+", "-"]

    while not game_over:
        # Generate two random numbers
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        # Generate a random operator
        op = random.choice(operator)

        # Calculate the answer
        if op == "+":
            answer = a + b
        else:
            # Swap a, b to ensure a > b
            if a < b:
                a, b = b, a
            answer = a - b  # Ensure answer is always assigned here

        # The game ends when incorrect answer is typed, else, increase the score
        try:
            user_answer = int(input(f"{a} {op} {b} = "))
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {answer}.")
                game_over = True

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return score


# Play the game
print(f"- Your score is {math_game()}.")
