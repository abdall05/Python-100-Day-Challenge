import time
import utils
from food import Food
from snake import Snake
from my_game_screen import GameScreen
from scoreboard import Scoreboard

game_screen = GameScreen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_running = True

game_screen.listen()
game_screen.onkey(lambda: snake.turn('right'), "Right")
game_screen.onkey(lambda: snake.turn('left'), "Left")

while game_running:
    game_screen.update()
    time.sleep(0.1)
    snake.forward()

    if snake.bite_itself() or utils.hit_screen(snake, game_screen):
        game_running = False
        scoreboard.game_over()

    if utils.found_food(snake, food):
        scoreboard.increase_score()
        food.move()
        snake.grow()

game_screen.exitonclick()
