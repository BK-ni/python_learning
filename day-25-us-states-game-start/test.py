import pandas

data = pandas.read_csv("50_states.csv")

answer_state = input("state?")
for i in data.state:
    if answer_state.lower() == i.lower():
        x = data[data.state == i].x
        y = data[data.state == i].y
        print(int(x), int(y))
