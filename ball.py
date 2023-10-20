from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 15
        self.ymove = 15

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def horizontal_bounce(self):
        self.xmove *= -1

    def reset_ball(self, i):
        self.goto(0, 0)
        if i % 4 == 0:
            self.xmove = 15
            self.ymove = 15
        elif i % 4 == 1:
            self.xmove = -15
            self.ymove = -15
        elif i % 4 == 2:
            self.xmove = 15
            self.ymove = -15
        else:
            self.xmove = -15
            self.ymove = 15
