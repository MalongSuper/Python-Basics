# 27. Rock Paper Scissors
# Simulate a two-player Rock Paper Scissors game until one player wins 3 rounds.
import random


def rock_paper_scissors(win_rounds=3):
    player1 = 0
    player2 = 0
    choices = ["rock", "paper", "scissors"]
    round = 1

    while True:
        # Randomly select choices
        player1_choice = random.choice(choices)
        player2_choice = random.choice(choices)

        print(f"Round {round}:")
        print(f"Player 1: {player1_choice}")
        print(f"Player 2: {player2_choice}")

        if player1_choice == player2_choice:
            print("It's a tie!\n")

        elif player1_choice == "rock":
            if player2_choice == "scissors":
                print("Player 1 wins!\n")
                player1 += 1
            else:
                print("Player 2 wins!\n")
                player2 += 1

        elif player1_choice == "paper":
            if player2_choice == "rock":
                print("Player 1 wins!\n")
                player1 += 1
            else:
                print("Player 2 wins!\n")
                player2 += 1

        elif player1_choice == "scissors":
            if player2_choice == "paper":
                print("Player 1 wins!\n")
                player1 += 1
            else:
                print("Player 2 wins!\n")

        round += 1
        # Display current score
        print(f"Score: Player 1: {player1} - Player 2: {player2}\n")

        if player1 == win_rounds:
            print("-" * 50)
            print("Player 1 wins the game!")
            print("-" * 50)
            break

        elif player2 == win_rounds:
            print("-" * 50)
            print("Player 2 wins the game!")
            print("-" * 50)
            break


rock_paper_scissors()
