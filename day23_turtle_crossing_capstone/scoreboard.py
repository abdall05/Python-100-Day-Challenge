from turtle import Turtle
from player import FINISH_LINE_Y
from game_screen import SCREEN_WIDTH
FONT = ("Courier", 16, "normal")
OFFSET = 30

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.goto(( -SCREEN_WIDTH/2 + 2*OFFSET, FINISH_LINE_Y - OFFSET ))
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)


    def game_over(self):
        game_over_text = Turtle()
        game_over_text.hideturtle()
        game_over_text.penup()
        self.goto((0, FINISH_LINE_Y - OFFSET))
        self.write(f'Game over!', align='center', font=FONT)




