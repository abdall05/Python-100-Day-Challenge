from turtle import Turtle
import random

MOVING_STEP = 10
DEFAULT_SIZE = 20
STRETCH_FACTOR = 0.5
BALL_SIZE = DEFAULT_SIZE * STRETCH_FACTOR


def random_angle():
    left_angle = random.randint(110, 250)
    right_angle = random.randint(290, 340)
    return random.choice([left_angle, right_angle])


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=STRETCH_FACTOR, stretch_len=STRETCH_FACTOR)
        self.setheading(random_angle())

    def move(self):
        self.forward(MOVING_STEP)

    def restart(self):
        self.goto(0, 0)
        self.setheading(random_angle())

    def bounce(self, obstacle):
        current_angle = self.heading()
        if obstacle == "PADDLE":
            current_angle = (180 - current_angle) % 360
        elif obstacle == "WALL":
            current_angle = 360 - current_angle

        self.setheading(current_angle)
        self.forward(2 * BALL_SIZE)
