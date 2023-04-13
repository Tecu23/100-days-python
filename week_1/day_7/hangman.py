import requests
import random
import hangman_art

def generate_word():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    
    response = requests.get(word_site)
    
    WORDS = response.content.splitlines()
    
    byte_word = random.choice(WORDS)

    return byte_word.decode('utf-8')


def hangman():

    print(hangman_art.logo)

    word = generate_word()
    lives = 6
    word_guess = ['_' for _ in word]

    guesses_letters = []

    print(f"The number of letters in the word is {''.join(word_guess)}")

    while lives > 0 and word != ''.join(word_guess):
        user_guess = input("Please Provide a guess. ").lower()

        found = False

        if user_guess in guesses_letters:
            print(f"Already guessed {user_guess}.")
            continue

        for letter_index, letter in enumerate(word):
            if letter == user_guess:
                print("You guessed a letter.")
                word_guess[letter_index] = user_guess
                found = True

                if word == ''.join(word_guess):
                    break

        if word == ''.join(word_guess):
            break

        if not found:
            print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(f"Remaining lives: {lives}")
            print(hangman_art.stages[lives])

    
        guesses_letters.append(user_guess)

        print(word_guess)


    if word == ''.join(word_guess):
        print("You win")
        print(f"Final Guess {word_guess}")
    else:
        print("You lose")
        print(f"The word was {word}")
    
