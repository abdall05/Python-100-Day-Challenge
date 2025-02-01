from turtle import Turtle
from my_game_screen import SCREEN_HEIGHT

SCORE_OFFSET = 40
FONT = ("Arial", 15, "bold")
SCORE_FILE = "score.txt"


def read_score(file=SCORE_FILE):
    with open(file, "r") as file:
        try:
            score = int(file.readline())
            return score
        except:
            return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_score()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, SCREEN_HEIGHT // 2 - SCORE_OFFSET)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.highest_score}', align='center', font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.save_score()

        self.score = 0
        self.update_score()

    def read_score(self, file="score.txt"):
        with open(file, "r") as file:
            try:
                self.highest_score = int(file.readline())
            except:
                self.highest_score = 0

    def save_score(self):
        with open("score.txt", "w") as file:
            file.write(str(self.highest_score))

    def increase_score(self):
        self.score += 1
        self.update_score()
