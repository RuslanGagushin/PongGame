from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Make a move for ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Make a bounce for ball"""
        self.y_move *= -1

    def bounce_x(self):
        """Make a bounce for ball"""
        self.x_move *= -1

    def reset_position(self):
        """Reset the ball position"""
        self.goto(0, 0)
