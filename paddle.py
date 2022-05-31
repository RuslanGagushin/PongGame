from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_coord, self.y_coord)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
