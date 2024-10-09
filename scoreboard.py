from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self. penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        """Update scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))


    def l_point(self):
        """Add point to left player"""
        self.l_score += 1

    def r_point(self):
        """Add point to right player"""
        self.r_score += 1