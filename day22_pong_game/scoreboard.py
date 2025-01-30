from turtle import Turtle

from game_screen import UPPER_EDGE

FONT = ("Arial", 30, "bold")

LEFT_SCORE_XPOS = -150
RIGHT_SCORE_XPOS = +150

OFFSET = 30
SCORE_YPOS = UPPER_EDGE - OFFSET


class Scoreboard(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('blue')
        self.goto(xpos, SCORE_YPOS)
        self.write(f'{self.score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align='center', font=FONT)


class GameScoreBoard:
    def __init__(self):
        self.scoreboard1 = Scoreboard(LEFT_SCORE_XPOS)
        self.scoreboard2 = Scoreboard(RIGHT_SCORE_XPOS)

    def increase_score(self, player):
        if player == 1:
            self.scoreboard1.increase_score()
        elif player == 2:
            self.scoreboard2.increase_score()
