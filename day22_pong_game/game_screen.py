from turtle import Screen, Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OFFSET = 30
DASH_LINE_LENGTH = 10
DASH_LINE_SIZE = 5
DOWN = 270

UPPER_EDGE = SCREEN_HEIGHT / 2 - OFFSET
LOWER_EDGE = -SCREEN_HEIGHT / 2 + OFFSET

RIGHT_EDGE = SCREEN_WIDTH / 2
LEFT_EDGE = - SCREEN_WIDTH / 2


def draw_line():
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, UPPER_EDGE)
    turtle.setheading(DOWN)
    turtle.pencolor('white')
    turtle.pensize(DASH_LINE_SIZE)
    height = SCREEN_HEIGHT / 2 - OFFSET
    counter = 0
    while turtle.ycor() >= LOWER_EDGE:
        if counter % 2 == 0:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(DASH_LINE_LENGTH)
        counter += 1


class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.title("Pong Game")
        self.screen.tracer(0)
        draw_line()
        # Disable resizing externally (Windows)
        self.screen._root.resizable(False, False)

    def __getattr__(self, attr):
        """Forward unknown attributes to self.screen"""
        return getattr(self.screen, attr)
