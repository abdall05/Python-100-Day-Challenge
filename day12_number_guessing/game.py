import random


def generate_random_number():
    return random.randint(1, 100)


def number_of_attempts():
    attempts = 10
    difficulty = input("Choose your difficulty level (low or high): ").lower()
    if difficulty == "high":
        attempts = 5
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
