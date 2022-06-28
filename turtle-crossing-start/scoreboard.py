from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", align="left", font=(FONT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Game Over.", align="center", font=(FONT))
