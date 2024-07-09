from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=250)
        self.write(f"A:B", move=False, align=ALIGN, font=FONT)
