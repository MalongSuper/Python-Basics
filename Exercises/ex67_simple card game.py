# 67. Simple Card Game

def card_ranking(card):
    if card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 1
    else:
        return int(card)


def determine_winner(player1, player2):
    player1_score = sum(card_ranking(card) for card in player1)
    player2_score = sum(card_ranking(card) for card in player2)

    print("Player 1's cards:", player1, "=> Score:", player1_score)
    print("Player 2's cards:", player2, "=> Score:", player2_score)

    if player1_score > player2_score:
        print("+ Player 1 wins!")
    elif player2_score > player1_score:
        print("+ Player 2 wins!")
    else:
        print("+ It's a tie!")


import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
n = int(input("Enter number of card to choose: "))
player1 = random.sample(cards, n)
player2 = random.sample(cards, n)

determine_winner(player1, player2)
