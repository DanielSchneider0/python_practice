from turtle import Screen, Turtle, color, tracer
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()
