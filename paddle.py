from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_right(self):
        self.goto(350, 0)

    def go_left(self):
        self.goto(-350, 0)

    def go_up(self):
        if self.ycor() < 230:
            current_y = self.ycor()
            current_x = self.xcor()
            self.goto(current_x, current_y+60)

    def go_down(self):
        if self.ycor() > -230:
            current_y = self.ycor()
            current_x = self.xcor()
            self.goto(current_x, current_y - 60)