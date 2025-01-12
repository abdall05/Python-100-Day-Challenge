import random

LOWER_BOUND = 1
UPPER_BOUND = 100
EASY_LEVEL_ATTEMPTS = 5
HARD_LEVEL_ATTEMPTS = 10


def generate_random_number():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def number_of_attempts():
    attempts = HARD_LEVEL_ATTEMPTS
    difficulty = input("Choose your difficulty level (low or high): ").lower()
    if difficulty == "high":
        attempts = EASY_LEVEL_ATTEMPTS
    return attempts


def make_a_guess(target_number):
    guess = int(input("Guess the number: "))
    if guess == target_number:
        print(f"You got it! the number was {target_number}.")
        return True
    elif guess < target_number:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
    return False
