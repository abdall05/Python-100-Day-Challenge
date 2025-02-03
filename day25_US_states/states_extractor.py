import pandas
import pandas as pd

FILE_PATH = "50_states.csv"
df = pandas.read_csv(FILE_PATH)


def get_states():
    return df["state"].str.lower().tolist()

def get_coordinate(state):
    state_row = df[df["state"].str.lower() == state]
    if not state_row.empty:
        x, y = int(state_row.iloc[0]["x"]), int(state_row.iloc[0]["y"])
        return x, y
    return None

