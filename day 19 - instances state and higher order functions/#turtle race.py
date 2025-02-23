#turtle race
#turtle.listen()
from turtle import Turtle, Screen
import random

orange = Turtle()
blue = Turtle()
purple = Turtle()
yellow = Turtle()
red = Turtle()
orange.name = "orange"
blue.name = "blue"
purple.name = "purple"
yellow.name = "yellow"
red.name = "red"
turtles = [orange, blue, purple, yellow, red]
orange.penup()
blue.penup()
purple.penup()
yellow.penup()
red.penup()
orange.shape("turtle")
blue.shape("turtle")
purple.shape("turtle")
yellow.shape("turtle")
red.shape("turtle")
orange.color("orange")
blue.color("blue")
purple.color("purple")
yellow.color("gold")
red.color("red")

screen = Screen()
screen.setup(width=500, height=400)

def betting():
   yourbet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
   return yourbet
def start():
    orange.goto(x=-200, y=0)
    blue.goto(x=-200, y=20)
    purple.goto(x=-200, y=40)
    yellow.goto(x=-200, y=-20)
    red.goto(x=-200, y=-40)
# def moving():
#     move = True
#     if orange.pos() == (200, 0):
#         move = False
#     if blue.pos() == (200, 20):
#         move = False
#     if purple.pos() == (200, 40):
#         move = False
#     if yellow.pos() == (200, -20):
#         move = False
#     if red.pos() == (200, -40):
#         move = False
#     return move
# aretheturtlesmoving = moving()
def race(yourbet):
    moving = True
    while moving == True:
        movingturtle = random.choice(turtles)
        print(movingturtle.name)
        movingturtle.forward(1)
        print(movingturtle.xcor())
        if movingturtle.xcor() >= 200.0:
            moving == False
            if movingturtle.name == yourbet:
                screen.textinput(title=f"{movingturtle.name} wins", prompt=f"{movingturtle.name} wins! You won!")
                break
            else:
                screen.textinput(title=f"{movingturtle.name} wins", prompt=f"{movingturtle.name} wins! You lost!")
                break
    else:
        pass



    # tim.color("orange")
    # tom.color("blue")
    # jim.color("purple")
    # jom.color("gold")
    # jam.color("red")




thebet = betting()
gotostart = start()
therace = race(thebet)
screen.listen()

screen.exitonclick()