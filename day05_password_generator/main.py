import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"',
           "'", '<', '>', ',', '.', '?', '/']

characters = [letters, symbols, numbers]

print("Welcome to Password Generator!")
number_of_letters = int(input("How many letters Would you like in your password?\n"))
number_of_symbols = int(input("How many symbols Would you like in your password?\n"))
number_of_numbers = int(input("How many numbers Would you like in your password?\n"))
characters_count = [number_of_letters, number_of_symbols, number_of_numbers]
indices = []
for i in range(len(characters_count)):
    if characters_count[i] != 0:
        indices.append(i)

total = number_of_letters + number_of_symbols + number_of_numbers
password = ""
for i in range(total):
    index = random.choice(indices)
    characters_count[index] -= 1
    if characters_count[index] == 0:
        indices.remove(index)
    random_character = random.choice(characters[index])
    password += random_character
print("Your password is", password)
