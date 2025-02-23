FONT = ("Courier", 24, "normal")
DELAY = 0.1
ALIGNMENT = "left"
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level1 = 1
        self.score1 = 0.1
    def level(self):
        self.level1 += 1
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level1}", move=False, align=ALIGNMENT, font=FONT)
    def score(self, currentdelay):
        newdelay = currentdelay / 10
        return newdelay
    def reset_level(self):
        self.clear()
        self.level1 = 1
        self.goto(-280, 250)
        self.write(f"Level: {self.level1}", move=False, align=ALIGNMENT, font=FONT)

    


