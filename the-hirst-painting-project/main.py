import colorgram
import turtle
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('spot_painting.jpg', 30)
# # r = colors.rgb.r
# # g = colors.rgb.g
# # b = colors.rgb.b
# # print(colors[0].r)
# color_list = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_list.append((r,g,b))

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]
tim = Turtle()
screen = Screen()
turtle.colormode(255)

turtle.setworldcoordinates(-55, -55,55, 55)
tim.penup()
x = -45
y = -45
for _ in range(0, 10):
    tim.teleport(x, y)
    for _ in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.fd(10)
    y += 10

screen.exitonclick()