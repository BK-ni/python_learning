from turtle import Turtle

ALIGN = "left"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL {self.level}", False, align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
