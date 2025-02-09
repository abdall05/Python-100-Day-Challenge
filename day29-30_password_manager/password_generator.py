import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':',
           ';', '"',
           "'", '<', '>', ',', '.', '?', '/']
MIN_LETTERS = 8
MAX_LETTERS = 10
MIN_NUMBERS = 2
MAX_NUMBERS = 4
MIN_SYMBOLS = 2
MAX_SYMBOLS = 4


def generate():
    nr_letters = random.randint(MIN_LETTERS, MAX_LETTERS)
    nr_numbers = random.randint(MIN_NUMBERS, MAX_NUMBERS)
    nr_symbols = random.randint(MIN_SYMBOLS, MAX_SYMBOLS)
    password_list = []
    for _ in range(nr_letters):
        password_list.append(random.choice(LETTERS))
    for _ in range(nr_numbers):
        password_list.append(random.choice(NUMBERS))
    for _ in range(nr_symbols):
        password_list.append(random.choice(SYMBOLS))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
