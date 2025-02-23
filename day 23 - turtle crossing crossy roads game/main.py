import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
cars = []
my_list = [f'{i}' for i in range(1, 21)]
moving_cars = [0]
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

you = Player()
thescore = Scoreboard()

screen.onkeypress(you.up, "Up")
screen.onkeypress(you.down, "Down")

game_is_on = True
my_dict = {}
for i in my_list:
    my_dict[i+'_data'] = CarManager()
    print(my_dict[i+'_data'])
#https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python
delay = 0.1
thescore.reset_level()
while game_is_on:
    
    # increase = 0.1 * delay
    for i in my_list:
        my_dict[i+'_data'].move()
        if my_dict[i+'_data'].xcor() <= -320:
            my_dict[i+'_data'] = CarManager()
        if you.distance(my_dict[i+'_data']) < 20:
            you.return_to_start()
            thescore.reset_level()
            delay = 0.1
            break
    if you.ycor() >= 300:
        you.return_to_start()
        thescore.level()
        delay = thescore.score(delay)

        # increase = 0.01 * delay
    time.sleep(delay)
    print(delay)
    #NOTE maybe make function inside player class that increases the delay?
    screen.update()




screen.exitonclick()