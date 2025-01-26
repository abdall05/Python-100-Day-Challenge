from turtle import Turtle
from my_game_screen import SCREEN_HEIGHT

OFFSET = 50
FONT = ("Arial", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('blue')
        self.goto(0, SCREEN_HEIGHT // 2 - OFFSET)
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!\n', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=FONT)
