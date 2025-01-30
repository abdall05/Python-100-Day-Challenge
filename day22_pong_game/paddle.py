from turtle import Turtle
from game_screen import UPPER_EDGE, LOWER_EDGE, SCREEN_WIDTH, OFFSET

LEFT_PADDLE_X = -SCREEN_WIDTH / 2 + OFFSET
RIGHT_PADDLE_X = SCREEN_WIDTH / 2 - OFFSET
PLAYER_MOVING_STEP = 30
COMPUTER_MOVING_STEP = PLAYER_MOVING_STEP // 4
DEFAULT_SIZE = 20
STRETCH_LEN = 4
STRETCH_WID = 0.5
PADDLE_WIDTH = DEFAULT_SIZE * STRETCH_WID
PADDLE_HEIGHT = DEFAULT_SIZE * STRETCH_LEN


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.setheading(90)
        self.goto(x=x_position, y=0)
        self.ball = None  # Default: No ball tracking

    @classmethod
    def player_paddle(cls):
        return cls(x_position=LEFT_PADDLE_X)

    @classmethod
    def computer_paddle(cls, ball):
        paddle = cls(x_position=RIGHT_PADDLE_X)
        paddle.ball = ball
        return paddle

    def paddle_up(self, step=PLAYER_MOVING_STEP):
        if self.ycor() < UPPER_EDGE:
            self.forward(step)

    def paddle_down(self, step=PLAYER_MOVING_STEP):
        if self.ycor() > LOWER_EDGE:
            self.backward(step)

    def auto_move(self):
        if self.ball is None:
            pass
        else:
            if self.ball.ycor() >= self.ycor() + PADDLE_HEIGHT // 4:
                self.paddle_up(COMPUTER_MOVING_STEP)
            elif self.ball.ycor() + PADDLE_HEIGHT // 4 <= self.ycor():
                self.paddle_down(COMPUTER_MOVING_STEP)
