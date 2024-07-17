from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High ScoreL {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        with open("data.txt", "r") as file:
            file.read()
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_scoreboard()
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
