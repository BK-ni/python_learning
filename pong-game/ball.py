from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        direction = random.randint(0, 360)
        self.setheading(direction)
        self.goto(new_x, new_y)

    # def reflect(self):
    #     insert_angle = self.heading()
    #     reflect_angle = 180 - (insert_angle % 90) + insert_angle // 90 * 90
    #     self.setheading(reflect_angle)
    #     self.fd(400)


