#gameover
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
    def take_score(self, score):
        if score == "score1":
            self.score1 += 1
        elif score == "score2":
            self.score2 += 1
    def score(self):
        self.clear()
        self.goto(100, 250)
        self.write(f"{self.score1}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(-100, 250)
        self.write(f"{self.score2}", move=False, align=ALIGNMENT, font=FONT)