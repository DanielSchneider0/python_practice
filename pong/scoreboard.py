from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(
            f"{self.score1}  ||   {self.score2}",
            align="center",
            font=("Verdana", 15, "normal"),
        )

    def increase_1(self):
        self.score1 += 1
        self.clear()
        self.update_score()

    def increase_2(self):
        self.score2 += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game over. Final score is {self.score1} || {self.score2}",
            align="center",
            font=("Verdana", 15, "normal"),
        )
