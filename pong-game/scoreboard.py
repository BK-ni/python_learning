from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=280)
        self.write(f"A:B", move=False, align="center", font=("Arial", 24, "normal"))
