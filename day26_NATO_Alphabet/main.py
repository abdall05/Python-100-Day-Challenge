import pandas

file_path = 'nato_phonetic_alphabet.csv'


def get_phonetic_mapping():
    df = pandas.read_csv(file_path)
    return {row["letter"]: row["code"] for _, row in df.iterrows()}


def get_word_spelling(word_to_spell, phonetic_mapping_dict):
    spell_word = word_to_spell.strip().upper()
    return [phonetic_mapping[letter] for letter in spell_word if letter in phonetic_mapping_dict]


if __name__ == "__main__":
    phonetic_mapping = get_phonetic_mapping()
    word = input("Enter a word: ")
    phonetic_word = get_word_spelling(word, phonetic_mapping)
    print(phonetic_word)
