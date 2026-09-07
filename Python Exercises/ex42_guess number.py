import random


def guessing_number(number, max_attempts):
    attempts = 0
    guessed = False

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Display attempt
        print(f"- Attempt {attempts} / {max_attempts}: {guess}")

        # Compare the guess with the number
        if guess < number:
            print("=> Higher!!")
        elif guess > number:
            print("=> Lower!!")
        else:
            print("=> Correct!!")
            guessed = True
            break

    # If max_attempts reached
    if attempts == max_attempts and not guessed:
        print(f"You have reached the maximum number of attempts. "
              f"The correct number is {number}.")


# Main execution
number = random.randint(1, 1000)
max_attempts = 15
guessing_number(number, max_attempts)
