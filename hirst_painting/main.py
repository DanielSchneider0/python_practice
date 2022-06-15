# import colorgram

# rgb_list = []
# colors = colorgram.extract("hirst.jpg", 40)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     formatted_color = (r, g, b)
#     rgb_list.append(formatted_color)

# print(rgb_list)


colors = [
    (205, 5, 69),
    (202, 74, 12),
    (111, 181, 218),
    (197, 164, 10),
    (217, 161, 109),
    (235, 50, 131),
    (235, 224, 6),
    (15, 29, 175),
    (29, 189, 114),
    (13, 23, 63),
    (23, 106, 174),
    (213, 136, 177),
    (9, 185, 215),
    (207, 27, 143),
    (228, 168, 201),
    (122, 191, 163),
    (66, 22, 7),
    (8, 49, 28),
    (189, 15, 5),
    (31, 136, 73),
    (127, 218, 232),
    (56, 10, 33),
    (144, 216, 201),
    (111, 89, 211),
    (235, 63, 38),
    (10, 98, 51),
    (172, 181, 228),
    (238, 169, 157),
    (252, 6, 40),
    (85, 89, 4),
    (8, 84, 104),
    (251, 10, 6),
    (27, 46, 246),
]

import random
from turtle import *

screen = Screen()
screen.colormode(255)
tim = Turtle()

tim.hideturtle()
tim.speed(0)
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
dots = 100

for count in range(1, dots + 1):
    tim.pencolor(random.choice(colors))
    tim.pendown
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
