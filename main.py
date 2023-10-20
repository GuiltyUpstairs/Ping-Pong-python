from turtle import Screen
from paddle import Paddle
from ball import Ball
from random import randint
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
game = True
screen.listen()
screen.tracer(0)
right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()
right_paddle.go_right()
left_paddle.go_left()
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)
score = Scoreboard()
x = 0.08
while game:
    screen.update()
    ball.move()
    time.sleep(x)
    if abs(ball.ycor()) > 280:
        ball.bounce()
    if (320 < ball.xcor() < 335 and abs(ball.ycor() - right_paddle.ycor()) < 50) or (-320 > ball.xcor() > -335 and abs(ball.ycor() - left_paddle.ycor()) < 50):
        ball.horizontal_bounce()
    if abs(ball.xcor()) > 400:
        x *= 0.9
        if ball.xcor() > 0:
            score.left_point()
        else:
            score.right_point()
        i = randint(0, 4)
        ball.reset_ball(i)
        time.sleep(1)

screen.exitonclick()