from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle
import time


screen = Screen()
scoreboard = ScoreBoard()

screen.tracer(0)
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



screen.exitonclick()