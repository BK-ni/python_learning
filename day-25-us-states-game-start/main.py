import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
data_list = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_list = []


t = turtle.Turtle()
t.hideturtle()
t.penup()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State ({len(guessed_list)}/{len(data)})",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_list = [state for state in data.state if state not in guessed_list]
        missed_state = pd.DataFrame(missed_list)
        missed_state.to_csv("missed states.csv")
        break

    if answer_state in data_list and answer_state not in guessed_list:
        state_data = data[data.state == answer_state]
        t.teleport(state_data.x.item(), state_data.y.item())
        t.pendown()
        t.write(answer_state, align="center")
        guessed_list.append(answer_state)

    if len(guessed_list) == len(data):
        t.penup()
        t.home()
        t.write("MISSION COMPLETED",align="center",font=("Arial", 20, "bold"))
        game_is_on = False
screen.exitonclick()


