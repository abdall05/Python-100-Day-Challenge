import random
import ascii_art

print("Welcome to Rock Paper Scissors!")
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(ascii_art.choices[your_choice])
print("Computer chose:")
computer_choice = random.randint(0, 2)
print(ascii_art.choices[computer_choice])
if your_choice == computer_choice:
    print("It's a tie!")
elif your_choice == (computer_choice + 1) % 3:
    print("You Win!")
else:
    print("You Lose!")
