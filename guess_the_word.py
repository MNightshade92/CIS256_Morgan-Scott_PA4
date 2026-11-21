# Morgan Scott
# CIS256 FAll 2026
# Programming Assignment 4

import random

# Define a list of words and select one at random
word_list = ["dungeon","crawler","persian","achievement","syndicate","dinosaur"]
secret_word = random.choice(word_list)

# Set up the variables
# Indicate number of letters with underscores

display_word = ["_"] * len(secret_word)
guessed_letters = []
attempts_remaining = 5

print("Welcome to the game: Guess the Word")
print(f"The word has {len(secret_word)} letters.")

# Main Game loop: Continues until word is done or no attempts remain
while attempts_remaining > 0 and "_" in display_word:
    # Shows the current progress and attempts remaining
    print("\nWord:"," ".join(display_word))
    print(f"Attempts Remaining: {attempts_remaining}")

    # Asks the user for a single letter and sets it to lower case
    guess = input("Guess a letter: ").lower()

    # Checks to make sure the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Checks if the letter was already guessed
    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Please try another letter.")
        continue

    # Records the new letter guessed
    guessed_letters.append(guess)

    # Checks if the letter is in the secret word
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the secret word!")

        # Runs thru the secret word to reveal all the instances of the letter
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess
    else:
        # removes an attempt for an incorrect guess
        attempts_remaining -= 1
        print(f"Sorry, '{guess}' is not in the word.")



