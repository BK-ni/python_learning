import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()

answer_list = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State ({len(answer_list)}/{len(data)})",
                                    prompt="What's another state's name?")
    for i in data.state:
        if answer_state.lower() == i.lower() and answer_state.lower() not in answer_list:
            t.penup()
            x = data[data.state == i].x.iloc[0]
            y = int(data[data.state == i].y.iloc[0])
            t.teleport(x, y)
            t.pendown()
            t.write(i, align="center")
            answer_list.append(i.lower())
    if len(answer_list) == len(data):
        game_is_on = False
        t.penup()
        t.home()
        t.write("MISSION COMPLETED",align="center",font=("Arial", 20, "bold"))

screen.exitonclick()


