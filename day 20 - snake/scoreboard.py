from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open("high_score.txt", mode="r") as readfile:
            self.high_score = int(readfile.read())
    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
    def update_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score - 1}")

        # self.score = 0
        # self.refresh_score()
