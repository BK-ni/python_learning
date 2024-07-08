from turtle import Turtle, Screen
from scoreboard import ScoreBoard
turtle = Turtle()
screen = Screen()

screen.listen()
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

scoreboard = ScoreBoard()

screen.exitonclick()