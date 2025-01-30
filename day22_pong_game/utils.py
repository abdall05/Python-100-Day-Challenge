from game_screen import UPPER_EDGE, LOWER_EDGE, RIGHT_EDGE, LEFT_EDGE
from paddle import PADDLE_WIDTH, PADDLE_HEIGHT
from ball import BALL_SIZE


def ball_paddle_collision(ball, paddle):
    return (abs(
        ball.xcor() - paddle.xcor()) <= BALL_SIZE / 2 + PADDLE_WIDTH / 2 and
            paddle.ycor() - PADDLE_HEIGHT / 2 <= ball.ycor() <= paddle.ycor() + PADDLE_HEIGHT / 2)


def ball_wall_collision(ball):
    return ball.ycor()+ BALL_SIZE//2 >= UPPER_EDGE or ball.ycor() - BALL_SIZE//2 <= LOWER_EDGE


# returns 0 if no goal ; 1 if goal for player 1 ; 2 if goal for player 2
def is_goal(ball):
    if ball.xcor() <= LEFT_EDGE:
        return 2
    elif ball.xcor() > RIGHT_EDGE:
        return 1
    else:
        return 0
