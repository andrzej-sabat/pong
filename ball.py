from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def move_ball(self):
        """Move ball on game start"""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        """Bounce ball from tob and bottom wall"""
        self.y_move *= -1


    def bounce_x(self):
        """Bounce ball from paddle"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """Reset ball position to it's starting position"""
        self.home()
        self.ball_speed = 0.1
        self.bounce_x()