from role_turtle import Screen
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.update()
time.sleep(0.1)



screen.exitonclick()
