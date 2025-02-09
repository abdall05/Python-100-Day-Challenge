import pandas
import random

DATA_PATH = "data/french_words.csv"


def load_data():

    df = pandas.read_csv(DATA_PATH)
    list_of_words = [[row["French"], row["English"]] for _, row in df.iterrows()]
    random.shuffle(list_of_words)
    return list_of_words


class WordsManager:
    def __init__(self):
        self.words = load_data()
        self.words_count = len(self.words)
        self.index = 0

    def next_word_pair(self):
        word = self.words[self.index]
        self.index = (self.index + 1) % self.words_count
        return word


