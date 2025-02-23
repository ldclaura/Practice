from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#create and move cars
#import random?
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        color = random.choice(COLORS)
        y = random.randint(-250, 290)
        x = random.randint(310, 1000)
        self.goto(x, y)
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
