from turtle import Turtle

FONT = ("Courier", 24, "normal")
COORDINATES = (-260, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(COORDINATES)
        self.write(f"Level: {self.level}", font=FONT)
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-70,0)
        self.write(f"GAME OVER", font=FONT)

