from cesar import cesar
from ascii_art import logo

print(logo)
finished = False
while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar(original_text=text, key=shift, encode_or_decode=direction)
    restart = input("Do you want to try again?(yes/no)\n").lower()
    if restart == 'no':
        finished = True
