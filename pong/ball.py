from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() - self.x_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def point_reset(self):
        self.goto(0, 0)
        self.paddle_bounce()
