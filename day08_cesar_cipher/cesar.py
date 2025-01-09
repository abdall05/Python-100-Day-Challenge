alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, key):
    word_letters = list(original_text)
    for i, letter in enumerate(original_text):
        if letter not in alphabet:
            continue
        current_letter = original_text[i]
        index = alphabet.index(current_letter)
        new_index = (index + key) % len(alphabet)
        word_letters[i] = alphabet[new_index]
    encrypted_text = ''.join(word_letters)
    return encrypted_text


def decrypt(encrypted_text, key):
    word_letters = list(encrypted_text)
    for i, letter in enumerate(encrypted_text):
        if letter not in alphabet:
            continue
        current_letter = encrypted_text[i]
        index = alphabet.index(current_letter)
        new_index = (index - key) % len(alphabet)
        word_letters[i] = alphabet[new_index]
    original_text = ''.join(word_letters)
    return original_text


def cesar(original_text, key, encode_or_decode):
    if encode_or_decode == "encode":
        print(f"here's the {encode_or_decode}d result:{encrypt(original_text, key)}")
    elif encode_or_decode == "decode":
        print(f"here's the {encode_or_decode}d result:{decrypt(original_text, key)}")
    else:
        print("Wrong option! 'encode' or 'decode'")

