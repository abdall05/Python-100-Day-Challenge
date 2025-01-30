import time

from ball import Ball
from game_screen import GameScreen
from paddle import Paddle
import utils
from scoreboard import GameScoreBoard

PLAYER1 = 1
PLAYER2 = 2
NO_GOAL = 0

REFRESH_TIME = 0.05
# To decrease the refresh time of screen -> to increase the ball speed.
REFRESH_TIME_FACTOR = 0.9

game_screen = GameScreen()
ball = Ball()
player_paddle = Paddle.player_paddle()
computer_paddle = Paddle.computer_paddle(ball)
scoreboard = GameScoreBoard()
game_screen.listen()
game_screen.onkeypress(lambda: player_paddle.paddle_up(), "Up")
game_screen.onkeypress(lambda: player_paddle.paddle_down(), "Down")
refresh_time = REFRESH_TIME
while True:
    game_screen.update()
    time.sleep(refresh_time)
    ball.move()
    computer_paddle.auto_move()
    if utils.ball_paddle_collision(ball, computer_paddle) or utils.ball_paddle_collision(ball, player_paddle):
        ball.bounce("PADDLE")
        refresh_time *= REFRESH_TIME_FACTOR
    elif utils.ball_wall_collision(ball):
        ball.bounce("WALL")
        refresh_time *= REFRESH_TIME_FACTOR

    else:
        player_goal = utils.is_goal(ball)
        if player_goal == PLAYER1:
            scoreboard.increase_score(PLAYER1)
        elif player_goal == PLAYER2:
            scoreboard.increase_score(PLAYER2)
        if player_goal != NO_GOAL:
            ball.restart()
            refresh_time = REFRESH_TIME
