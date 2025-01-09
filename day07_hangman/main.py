import random
from ascii_art import hangman, logo
from hangman_words import word_list

print(logo)

LIVES = len(hangman)
random_word = random.choice(word_list)
constructed_word = ['_'] * len(random_word)
won = False
current_hangman_index = 0
print(f"You have {LIVES} lives to guess the word!")


print("##############################################")

while LIVES > 0 and not won:
    guess = input("Guess a letter: ").lower()

    if guess in constructed_word:
        print(f"You have already guessed {guess}!")
        continue
    elif guess not in random_word:
        print(f"{guess} is not in the word!")
        LIVES -= 1
        print(hangman[current_hangman_index])
        current_hangman_index += 1
        print(f"You have {LIVES} lives left.")
    else:
        for i, letter in enumerate(random_word):
            if letter == guess:
                constructed_word[i] = letter
        word = ''.join(constructed_word)
        print(word)
        if word == random_word:
            won = True
    print("##############################################")


if won:
    print("Congrats! You won!")
else:
    print("Sorry, you lost.")
print("The word was", random_word)
