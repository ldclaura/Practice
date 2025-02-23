from turtle import Screen, Turtle

screen = Screen()
UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        x = self.xcor()
        y = self.ycor()


        self.goto(x, y=y+20)

    def down(self):
        x = self.xcor()
        y = self.ycor()

        #self.paddles[0].setheading(DOWN)
        self.goto(x, y=y-20)


#width = 20
#height = 100
#x_pos = 350
#y_pos = 0