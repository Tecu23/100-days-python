#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

EASY_MODE_GUESSES = 10
HARD_MODE_GUESSES = 5

GUESSES = 0

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

number = random.randint(0, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    GUESSES = EASY_MODE_GUESSES
else:
    print("You have 5 attempts remaining to guess the number.")
    GUESSES = HARD_MODE_GUESSES

for i in range(GUESSES):
    guess = int(input("Make a guess: "))

    if guess == number:
        print("You win!!")
        break

    if guess > number:
        print("Too high")
    else:
        print("Too low")


print(f"The number was {number}")

