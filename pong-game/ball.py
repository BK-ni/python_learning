from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("slowest")
        self.penup()

    def move(self):
        direction = random.randint(0, 360)
        self.setheading(direction)
        self.goto(300,100)

    def reflect(self):
        insert_angle = self.heading()
        reflect_angle = 180 - (insert_angle % 90) + insert_angle // 90 * 90
        self.setheading(reflect_angle)
        self.fd(400)


