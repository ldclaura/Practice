from turtle import Turtle
import csv
import pandas

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
class ScreenText(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
    def win(self):
        self.goto(-125 , 0)
        self.write(f"You Win!", move=False, align=ALIGNMENT, font=("Courier", 50, "normal"))
    def state_text(self, state):
        state = state.title()
        americanstates = pandas.read_csv("50_states.csv")
        # americanstates.style.hide(axis='index')
        selectedstate = americanstates[americanstates.state == f"{state}"]
        x = selectedstate.x.values[0]
        y = selectedstate.y.values[0]

        self.goto(x, y)
        self.write(f"{state}")
        # self.goto()
        # self.write(f"{state}")