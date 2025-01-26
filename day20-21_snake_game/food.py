from turtle import Turtle
import utils
from my_game_screen import SCREEN_HEIGHT, SCREEN_WIDTH


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.move()

    def move(self):
        x, y = utils.random_position(SCREEN_HEIGHT, SCREEN_WIDTH)
        self.goto(x, y)
