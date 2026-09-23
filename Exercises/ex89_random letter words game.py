# 89. Random Letter Words Game
import string
import random


def dictionaries(filename):  # Load a dictionary for the game
    try:
        with open(filename, 'r') as file:
            # Read the file and create a set of words, stripping whitespace
            words = {line.strip().lower() for line in file if line.strip()}
        return words
    except FileNotFoundError:
        print("File not found")


def play_random_letter_word_game():
    used_words = set()  # Keep track of the already used word
    dictionary = dictionaries("words.txt")
    selected_letter = random.choice(string.ascii_uppercase)
    letter = selected_letter.lower()

    print(f"Your letter is {selected_letter}")

    # Play word game
    count = 0

    for i in range(1, 101):
        input_word = input(f"{i}. Enter a word: ")
        word = input_word.lower()  # Put the word in lowercase for consideration

        if not word: # Handle empty input
            print("=" * 50)
            print("=> Empty input. You Lose!!")
            return
        if word in used_words:
            print("=" * 50)
            print("=> Duplicate Word\nYou Lose!!")
            return
        elif letter not in word:
            print("=" * 50)
            print("=> Invalid Word (does not contain the letter)\nYou Lose!!")
            return
        elif word not in dictionary:
            print("=" * 50)
            print("=> Not Meaningful Word\nYou Lose!!")
            return
        else:
            print("=> Correct! Keep going.")
            used_words.add(word)
            count += 1

    print("=" * 50)
    print(f"=> Congratulations! You found {count} words and won!")


play_random_letter_word_game()
