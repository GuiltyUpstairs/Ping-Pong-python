from turtle import Turtle
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(arg=self.left_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(arg=self.right_score, align="center", font=FONT)

    def left_point(self):
        self.clear()
        self.left_score += 1
        self.update()

    def right_point(self):
        self.clear()
        self.right_score += 1
        self.update()
