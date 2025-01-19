from rgb_extractor import rgb_colors
from turtle import Turtle, Screen
import random

DOT_SIZE = 20
SPACE = 50
ROWS = 10
COLUMNS = 10


class HirstPainter:
    def __init__(self, dot_size=DOT_SIZE, space=SPACE, rows=ROWS, columns=COLUMNS):
        self.dot_size = dot_size
        self.space = space
        self.rows = rows
        self.columns = columns
        self.turtle = Turtle()
        self.screen = Screen()
        self._setup_turtle()

    def _setup_turtle(self):
        self.turtle.hideturtle()
        self.turtle.penup()
        self.screen.colormode(255)

    def dot(self, size):
        random_color = random.choice(rgb_colors)
        self.turtle.pencolor(random_color)
        self.turtle.dot(size)

    def draw(self):
        start_point = (DOT_SIZE / 2 - self.screen.window_width() / 2, DOT_SIZE / 2 - self.screen.window_height() / 2)
        for row in range(ROWS):
            for col in range(COLUMNS):
                current_position = (
                    start_point[0] + ((DOT_SIZE + SPACE) * col), start_point[1] + ((DOT_SIZE + SPACE) * row))
                self.turtle.goto(current_position)
                self.dot(DOT_SIZE)

    def exit_on_click(self):
        self.screen.exitonclick()
