import random
from turtle import Turtle
from game_screen import SCREEN_WIDTH, SCREEN_HEIGHT
from player import PLAYER_SIZE
from collections import deque

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

DEFAULT_SIZE = 20
STRETCH_WIDTH = 1
STRETCH_LENGTH = 2

CAR_WIDTH = DEFAULT_SIZE * STRETCH_LENGTH
CAR_START_LINE = SCREEN_WIDTH // 2
OFFSET = 70
CAR_MIN_Y = -240
CAR_MAX_Y = 240
ROW_DISTANCE = 40


# creates a new car on position (SCREEN_WIDTH/2,y)
def random_car(ycor, xcor=CAR_START_LINE):
    color = random.choice(COLORS)
    car = Car(color, (xcor, ycor))
    return car


def random_row_of_cars(ycor):
    cars = []
    choice = [True, False]
    for x in range(SCREEN_WIDTH // 2, -SCREEN_WIDTH // 2, - CAR_WIDTH - OFFSET):
        append = random.choice(choice)
        if append:
            car = random_car(ycor, x)
            cars.append(car)
    return cars


class Car(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.goto(position)
        self.speed = STARTING_MOVE_DISTANCE

    def boost_speed(self):
        self.speed += MOVE_INCREMENT

    def move(self):
        self.forward(self.speed)


class CarManager:
    def __init__(self):
        self.cars = {}
        for y in range(CAR_MIN_Y, CAR_MAX_Y + 1, ROW_DISTANCE):
            self.cars[y] = random_row_of_cars(y)

    def move_cars(self):
        for row in self.cars:
            cars = self.cars[row]
            for car in cars:
                car.move()
                if car.xcor() < -SCREEN_WIDTH // 2:
                    car.goto(SCREEN_WIDTH // 2, car.ycor())

    def check_collision(self, player):
        for row in self.cars:
            cars = self.cars[row]
            for car in cars:
                if abs(player.ycor() - car.ycor()) <= PLAYER_SIZE / 2 + DEFAULT_SIZE / 2 and (
                        car.xcor() - CAR_WIDTH / 2 < player.xcor() - DEFAULT_SIZE / 2 < car.xcor() + CAR_WIDTH / 2 or
                        car.xcor() - CAR_WIDTH / 2 < player.xcor() + DEFAULT_SIZE / 2 < car.xcor() + CAR_WIDTH / 2):
                    return True
        return False
