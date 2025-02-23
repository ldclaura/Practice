#snakeclass
from turtle import Screen, Turtle
import time
#what are constants??
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.squares = []
        self.snakebody()
        self.game_is_on = True
        self.head = self.squares[0]


    def snakebody(self):
        xcoord = 0
        for snek in range(3):
            square = Turtle()
            square.penup()
            square.color("white")
            square.shape("square")
            square.goto(x=xcoord, y=0)
            self.squares.append(square)
            xcoord -= 20
        return square
    def add_segment(self, position):
            square = Turtle()
            square.penup()
            square.color("white")
            square.shape("square")
            square.goto(position)
            self.squares.append(square)
         
    def extend(self):
        self.add_segment(self.squares[-1].position())
    


    def move_snake(self):
        # while self.game_is_on == True:
        #     screen.update()
        #     time.sleep(0.1)
        #     # for seg in squares:
        #     #     seg.forward(20)
                for seg_num in range(len(self.squares) - 1, 0, -1):
                    #for seg_num in range(start=2, stop=0, step=-1):
                    newx = self.squares[seg_num-1].xcor()
                    newy = self.squares[seg_num-1].ycor()
                    self.squares[seg_num].goto(newx, newy)
                self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # newx = self.head.xcor()
        # newy = self.head.ycor() + 1


        # self.head.setheading(self.head.towards(newx, newy))
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # newx = self.head.xcor()
        # newy = self.head.ycor() - 1


        # self.head.setheading(self.head.towards(newx, newy))
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # newx = self.head.xcor() - 1
        # newy = self.head.ycor()


        # self.head.setheading(self.head.towards(newx, newy))

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # newx = self.head.xcor() + 1
        # newy = self.head.ycor()


        # self.head.setheading(self.head.towards(newx, newy))
