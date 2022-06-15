# import module

# print(module.variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("DarkGreen")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon", ["Pikachu", "Mew", "Squirtle"])
# table.add_column("Type", ["Electric", "Magic", "Water"])
# table.align = "l"
# print(table)


# create a square in turtle
# from turtle import Screen, Turtle

# tim_turtle = Turtle()
# tim_turtle.shape("circle")
# tim_turtle.color("blue")

# for _ in range(4):
#     tim_turtle.forward(100)
#     tim_turtle.right(90)


# screen = Screen()
# screen.exitonclick()


#  Draw a dash line
# from turtle import *

# tim = Turtle()
# tim.pen(fillcolor="black", pencolor="black")
# for _ in range(4):
#     tim.pendown()
#     tim.forward(60)
#     tim.penup()
#     tim.forward(30)


# screen = Screen()
# screen.exitonclick()


######################## shape generator
# from random import *
# from turtle import *


# import numpy as np

# tim = Turtle()

# n = [3, 4, 5, 6, 7, 8, 9, 10]
# for i in n:
#     sides = i
#     angle = 360 / sides
#     random_color = (np.random.random(), np.random.random(), np.random.random())
#     for _ in range(sides):
#         tim.pencolor(random_color)
#         tim.right(angle)
#         tim.forward(100)

#     print(tim.color())


# screen = Screen()
# screen.exitonclick()


############ Random Walk
# import random
# from turtle import *
# import numpy as np

# tim = Turtle()

# movement = [0, 90, 180, 270]
# for _ in range(300):
#     tim.speed(0)
#     tim.forward(30)
#     tim.pencolor(np.random.random(), np.random.random(), np.random.random())
#     tim.pensize(15)
#     tim.setheading(random.choice(movement))


# screen = Screen()
# screen.exitonclick()

##########Spirograph
# from turtle import *
# import numpy as np

# tim = Turtle()
# tim.speed(0)
# tim.pensize(2)

# for _ in range(90):
#     tim.circle(100)
#     tim.pencolor(np.random.random(), np.random.random(), np.random.random())
#     tim.left(4)

# screen = Screen()
# screen.e
#


######### Etch a Sketch

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()


# def move_forward():
#     tim.forward(10)


# def move_backwards():
#     tim.back(10)


# def rotate_left():
#     tim.left(10)


# def rotate_right():
#     tim.right(10)


# def clear():
#     tim.reset()


# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=rotate_left)
# screen.onkey(key="d", fun=rotate_right)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()


####################### Turtle Race


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color of the rainbow: ",
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-167, -101, -35, 35, 101, 167]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
