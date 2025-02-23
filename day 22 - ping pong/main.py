from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from text import Text
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# screen.tracer(0)


# game_is_on = True
# while game_is_on:
#     pass


screen.tracer(0)
ball = Ball()
text = Text()
paddle1 = Paddle()
paddle2 = Paddle()

paddle1.goto(x=350, y=0)
paddle2.goto(x=-350, y=0)
screen.update()
screen.tracer(1)
screen.listen()

game = True

#it doesnt take inputs unless i use lambda?

while game:
    screen.onkey(paddle1.up, "Up")
    screen.onkey(paddle1.down, "Down")
    screen.onkey(paddle2.up, "w")
    screen.onkey(paddle2.down, "s")
    # time.sleep(0.1)
    # screen.update()
    ball.move_ball_start()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() > 330 and ball.distance(paddle1) < 50:  # 50 is half of paddle's height
        ball.hit_paddle()

    # Check if ball hits paddle2
    if ball.xcor() < -330 and ball.distance(paddle2) < 50:  # 50 is half of paddle's height
        ball.hit_paddle()

    if ball.xcor() < -400:
        # game = False
        text.take_score("score1")
        screen.tracer(0)
        # text.gameover()
        text.score()
        screen.update()

        ball.goto(0, 0)
        paddle1.goto(x=350, y=0)
        paddle2.goto(x=-350, y=0)
        ball.hit_paddle()
        screen.tracer(1)
        # ball.move_ball_start()

    if ball.xcor() > 400:
        # game = False
        text.take_score("score2")
        screen.tracer(0)
        # text.gameover()
        text.score()
        screen.update()
        ball.goto(0, 0)
        paddle1.goto(x=350, y=0)
        paddle2.goto(x=-350, y=0)
        ball.hit_paddle()
        screen.tracer(1)
        # ball.move_ball_start()


screen.exitonclick()