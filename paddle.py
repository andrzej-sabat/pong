from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)



    def create_paddle(self):
        """Create paddle"""
        t = Turtle()
        t.shape("square")
        t.resizemode("user")
        t.shapesize(5, 1)
        t.color("white")
        t.penup()
        t.goto(350,0)  # Use the passed position argument


    def up(self):
        """Move paddle UP"""
        y = self.ycor() + 20
        self.goto(self.xcor(), y)


    def down(self):
        """Move paddle DOWN"""
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
