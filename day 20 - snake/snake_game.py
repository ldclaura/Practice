#snake_game
from turtle import Screen
import time
from snakeclass import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
scoreboard.refresh_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    scoreboard.reset()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor () < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    #detect collision with tail other than head
    #SLICING
    for segment in snake.squares[1:]: #SLICING, any segment other than first segment (head),
        #this is so the game doesn't just stop at the start from head touching itself
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
