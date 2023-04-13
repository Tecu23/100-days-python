"""
    BLACKJACK CAPSTONE
"""

import random


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play():

    players_cards = random.choices(cards, k=2)
    dealers_cards = random.choices(cards, k=2)

    print(f"Your Cards: {players_cards}")
    print(f"Computers first card: {dealers_cards[0]}")

    should_continue_dealing = True
    game_ended = False

    while should_continue_dealing:

        next_move = input("Type 'y' to get another card, type 'n' to pass: ")

        if next_move == 'y':
            players_cards.append(random.choice(cards))
            print(players_cards)
            if sum(players_cards) > 21:
                print("You lost!!")
                game_ended = True
                should_continue_dealing = False
                break
        else:
            should_continue_dealing = False


    while sum(dealers_cards) < 17:
        dealers_cards.append(random.choice(cards))

    if sum(dealers_cards) > 21:
        print(f"Your cards are {players_cards} and the computer's are {dealers_cards}")
        print("The computer wen over 21. You win!!")
        game_ended = True

    if not game_ended:
        print(f"Your cards are {players_cards} and the computer's are {dealers_cards}")
        if sum(players_cards) > sum(dealers_cards):
            print("You win!!")
        else:
            print("You lost!!")

end_program = False
play()

while not end_program:
    next_play = input("Type 'y' if you want to play again and 'n' otherwise: ")
    if next_play == 'y':
        play()
    else:
        end_program = True