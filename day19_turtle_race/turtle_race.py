import random
from turtle import Turtle, Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OFFSET = 50
SPACE = 50

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def generate_turtles(colors):
    turtles = []
    for index, color in enumerate(colors):
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(-SCREEN_WIDTH / 2 + OFFSET, -SCREEN_HEIGHT / 4 + SPACE * index)
        turtles.append(turtle)
    return turtles


def setup_screen():
    screen = Screen()
    screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
    return screen


def get_user_bet(colors, screen):
    user_bet = None
    while user_bet not in colors:
        user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
    return user_bet


def start_race(turtles, end_line):
    is_race_on = True
    winner = None
    while is_race_on:
        for turtle in turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if turtle.xcor() >= end_line:
                winner = turtle
                is_race_on = False
                break
    return winner


def turtle_race():
    screen = setup_screen()
    turtles = generate_turtles(COLORS)
    user_bet = get_user_bet(COLORS, screen)
    end_line = SCREEN_WIDTH / 2 - OFFSET
    winner = start_race(turtles, end_line)

    if winner.pencolor() == user_bet:
        print(f"You've won! The {winner.pencolor()} turtle is the winner!")
    else:
        print(f"You've lost! The {winner.pencolor()} turtle is the winner!")

    screen.exitonclick()
