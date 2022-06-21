from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.tim_body = []
        self.create_snake()
        self.head = self.tim_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.tim_body.append(body)

    def extend(self):
        self.add_segment(self.tim_body[-1].position())

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
