from turtle import Screen, Turtle
import time
from left_paddle import LeftPaddle
from ball import Ball
from right_paddle import RightPaddle

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
ball = Ball()
right_paddle = RightPaddle()
left_paddle = LeftPaddle()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    score.update_score()
    ball.move()

    # Detect collison with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 400:
        ball.point_reset()
        score.increase_1()

    if ball.xcor() < -400:
        ball.point_reset()
        score.increase_2()

    if score.score1 >= 7 or score.score2 >= 7:
        game_is_on = False
        score.game_over()

screen.exitonclick()
