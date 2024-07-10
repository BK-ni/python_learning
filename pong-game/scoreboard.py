from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=240)
        self.player_a = 0
        self.player_b = 0
        self.write(f"{self.player_a} : {self.player_b}", move=False, align=ALIGN, font=FONT)
