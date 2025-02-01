from turtle import Turtle
from random import randint
from scoreboard import SCORE_OFFSET

SQUARE_SIZE = 20


def create_square():
    square = Turtle()
    square.shape('square')
    square.color('white')
    square.penup()
    return square


def is_collision(head, body_part):
    head_x = head.position()[0]
    head_y = head.position()[1]
    body_x = body_part.position()[0]
    body_y = body_part.position()[1]
    return abs(head_x - body_x) < SQUARE_SIZE and abs(head_y - body_y) < SQUARE_SIZE


def found_food(snake, food):
    head_x = snake.head.position()[0]
    head_y = snake.head.position()[1]
    food_x = food.position()[0]
    food_y = food.position()[1]
    return ((head_x + SQUARE_SIZE / 2) >= food_x >= head_x - (SQUARE_SIZE / 2)) and (
            (head_y + (SQUARE_SIZE / 2)) >= food_y >= (head_y - SQUARE_SIZE / 2))


def hit_screen(snake, game_screen):
    head_x = snake.head.position()[0]
    head_y = snake.head.position()[1]
    screen_height = game_screen.window_height()
    screen_width = game_screen.window_width()
    if (head_x > screen_width / 2 - SQUARE_SIZE / 2 or head_x < -screen_width / 2 + SQUARE_SIZE / 2 or
            head_y > screen_height / 2 - SQUARE_SIZE / 2 - SCORE_OFFSET or head_y < - screen_height / 2 + SQUARE_SIZE / 2):
        return True
    return False


def random_position(height, width):
    (x, y) = (0, 0)
    (x, y) = randint(-width // + SQUARE_SIZE, width // 2 - SQUARE_SIZE), randint(-height // 2 + SQUARE_SIZE,
                                                                                 height // 2 - SQUARE_SIZE - SCORE_OFFSET)
    return x, y
