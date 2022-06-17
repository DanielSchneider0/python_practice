from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.tim_body = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            x_axis = -20 * len(self.tim_body)
            y_axis = 0
            body.goto(x_axis, y_axis)
            self.tim_body.append(body)

    def move(self):
        for seg_num in range(len(self.tim_body) - 1, 0, -1):
            new_x = self.tim_body[seg_num - 1].xcor()
            # print(new_x)
            new_y = self.tim_body[seg_num - 1].ycor()
            # print(new_y)
            self.tim_body[seg_num].goto(new_x, new_y)
        self.tim_body[0].forward(20)

    def up(self):
        if self.tim_body[0].heading() != DOWN:
            self.tim_body[0].setheading(UP)

    def down(self):
        if self.tim_body[0].heading() != UP:
            self.tim_body[0].setheading(DOWN)

    def left(self):
        if self.tim_body[0].heading() != RIGHT:
            self.tim_body[0].setheading(LEFT)

    def right(self):
        if self.tim_body[0].heading() != LEFT:
            self.tim_body[0].setheading(RIGHT)
