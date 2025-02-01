from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_SIZE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
    def reset_position(self):
        self.goto(STARTING_POSITION)


