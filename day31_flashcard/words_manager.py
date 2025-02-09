import pandas
import random

DATA_PATH = "data/word_list.csv"


def add_weights():
    df = pandas.read_csv(DATA_PATH)
    if 'Weight' not in df.columns:
        df['Weight'] = 1
        df.to_csv(DATA_PATH, index=False)


add_weights()


class WordsManager:
    def __init__(self):
        self.indices = None
        self.expressions = None
        self.explanations = None
        self.weights = None
        self.load_data()

    def load_data(self):
        df = pandas.read_csv(DATA_PATH)
        self.indices = df.index
        self.expressions = df.Expression
        self.explanations = df.Explanation
        self.weights = df.Weight
        self.weights = self.weights.astype(float)

    def update_weight(self, word_index):
        self.weights[word_index] = 1 / ((1 / self.weights[word_index]) + 1)

    def next_word_index(self):
        return random.choices(self.indices, weights=self.weights)[0]

    def next_word(self, word_index):
        return self.expressions[word_index], self.explanations[word_index]

    def save_data(self):
        data = {
            'Expression': self.expressions,
            'Explanation': self.explanations,
            'Weights': self.weights,
        }
        df_to_save = pandas.DataFrame(data)
        df_to_save.to_csv(DATA_PATH, index=False)

