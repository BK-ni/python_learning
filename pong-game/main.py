from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle
import time


screen = Screen()
scoreboard = ScoreBoard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

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

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    else:
        if ball.distance(r_paddle) > ball.distance(l_paddle):
            scoreboard.player_b += 1
            ball.__init__()
        else:
            scoreboard.player_a += 1
            ball.__init__()
screen.exitonclick()
