from turtle import Screen
import time

from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# print("FOOD", food, food.xcor(), food.ycor())

screen.listen()
screen.onkey(snake.up, "Up")  # 90
screen.onkey(snake.down, "Down")  # 270
screen.onkey(snake.left, "Left")  # 180
screen.onkey(snake.right, "Right")  # 0


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        score.game_over()

    # detect tail collision
    # slicing in python example slicing tuple [1:]
    for segment in snake.tim_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
