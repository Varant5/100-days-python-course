from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 13, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            for line in file:
                pass
            self.high_score = line
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", "w") as file:
                self.high_score = self.score
                file.write(f"\n{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()