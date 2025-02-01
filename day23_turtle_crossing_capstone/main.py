import time

from game_screen import GameScreen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_screen = GameScreen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

game_screen.listen()
game_screen.onkeypress(lambda: player.move_up(), "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_screen.update()
    car_manager.move_cars()
    if car_manager.check_collision(player):
        print("collision!")
        game_is_on = False
        scoreboard.game_over()
        game_screen.update()



    if player.reached_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.update_level()

        print("you win!")

game_screen.exitonclick()