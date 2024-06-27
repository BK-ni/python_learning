import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
### turtle painting shapes

# tim.shape('turtle')
# for i in range(3, 10):
#     tim.color(random.choice(colors))
#     num_sides = i
#     angle = 360 / i
#     for _ in range(num_sides):
#         tim.right(angle)
#         tim.fd(50)

### random walk
# tim.pensize(5)
# tim.speed(3)
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# angle = [0 , 90, 180, 270]
#
# for i in range(100):
#     tim.color(random_color())
#     tim.right(random.choice(angle))
#     tim.fd(30)

turtle.colormode(255)
tim.speed(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)




screen.exitonclick()