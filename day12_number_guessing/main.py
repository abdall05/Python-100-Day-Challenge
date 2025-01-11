from ascii_art import logo
import game

print(logo)
keep_playing = True

while keep_playing:
    random_number = game.generate_random_number()
    attempts = game.number_of_attempts()
    print("Guess the number between 1 and 100.")
    print(f"You have {attempts} to guess the number")
    guessed = False
    while attempts > 0:
        guessed = game.make_a_guess(random_number)
        if guessed:
            break
        attempts -= 1
        print(f"You have {attempts} attempts to guess the number.")
    if not guessed:
        print(f"The number was {random_number}")

    play_again = input("do you want to try again (y/n)? ").lower()
    if play_again == 'n':
        keep_playing = False
