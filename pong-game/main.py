from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from ball import Ball
import time
ball = Ball()
screen = Screen()
scoreboard = ScoreBoard()
screen.listen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Pong Game")
game_is_on = True

ball.move()
if ball.xcor() == 300 or ball.xcor() == -300 or ball.ycor() == 300 or ball.ycor() == -300:
    ball.reflect()


screen.exitonclick()
