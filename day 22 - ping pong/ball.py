from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        # self.paddles.append(pad)
        self.x_move = 10
        self.y_move = 10
    def move_ball_start(self):

        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        #print(newx, newy)
        self.goto(newx, newy)
            #-
        #     if self.ycor() == 280:
        #         ball_not_hit_wall = False
        # while ball_not_hit_wall == False:
        #     newx = self.xcor() + 10
        #     newy = self.ycor() - 10
        #     self.goto(newx, newy)
        #     if self.ycor() == -280:
        #         ball_not_hit_wall = True
    def bounce(self):
        self.y_move *= -1
    def hit_paddle(self):
        self.x_move *= -1
            
        # if newy == 290:
        #     ball_not_hit_wall = False
        # elif newy == -290:
        #     ball_not_hit_wall = True
        # else:
        #     while ball_not_hit_wall:
        #         newx = self.ball.xcor() + 10
        #         newy = self.ball.ycor() + 10
        #     else:
        #         newx = self.ball.xcor() + 10
        #         newy = self.ball.ycor() - 10

            
            # if newy == 290:
            #     ball_not_hit_wall = False
            #     while ball_not_hit_wall == False:
            #         newx = self.ball.xcor() + 10
            #         newy = self.ball.ycor() - 10
            # if newy == -290:
            #     newy = self.ball.ycor() + 10
            # self.ball.goto(newx, newy)



