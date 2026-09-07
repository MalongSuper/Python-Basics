# 46. Lottery Game
# Simulate a lottery system based on digit matching rules.
import random


def lottery_game(n):
    # if the number is not three digits, exit the program
    if n < 100 or n > 999:
        print("Invalid input. Please enter a three-digit number.")
        return None
    else:
        random_number = random.randint(100, 999)
        print(f"- The random number is {random_number}.")

        # Get the digits for validation
        n1 = n // 100
        n2 = (n % 100) // 10
        n3 = n % 10

        random_number1 = random_number // 100
        random_number2 = (random_number % 100) // 10
        random_number3 = random_number % 10

        # Exact match → $3,000
        if n1 == random_number1 and n2 == random_number2 and n3 == random_number3:
            return 3000

        # At least 2 matching digits → $2,000
        elif ((n1 == random_number1 or n1 == random_number2 or n1 == random_number3)
              and (n2 == random_number1 or n2 == random_number2 or n2 == random_number3)
              and (n3 == random_number1 or n3 == random_number2 or n3 == random_number3)):
            return 2000

        # At least 1 matching digit → $1,000
        elif ((n1 == random_number1 or n1 == random_number2 or n1 == random_number3)
              or (n2 == random_number1 or n2 == random_number2 or n2 == random_number3)
              or (n3 == random_number1 or n3 == random_number2 or n3 == random_number3)):
            return 1000

        # No matching digits → $0
        else:
            return 0


n = int(input("Enter a three-digit number: "))
print(f"- You won ${lottery_game(n)}")
