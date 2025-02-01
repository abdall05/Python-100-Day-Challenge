import time
from turtle import Screen

from game_screen import GameScreen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_screen = GameScreen()

car_manager = CarManager()
player = Player()

game_screen.listen()
game_screen.onkeypress(lambda: player.move_up(), "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_screen.update()
    car_manager.move_cars()
    if car_manager.check_collision(player):
        print("collision!")

    if player.reached_finish_line():
        print("you win!")
