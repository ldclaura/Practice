from turtle import Screen, Turtle
import csv
import pandas
from text import ScreenText

screen = Screen()
screen.setup(width=725, height=491)
screen.title("Name the States")
screen.bgpic("blank_states_img.gif")

def guess_state_prompt(state):
   guesspopup = screen.textinput(title=f"{state}/50 States Correct", prompt="What's another state name?").lower()
   return guesspopup
def check_guess(guess):
    for _ in unguessed_states:
        if _ != guess:
            pass
        else:
            unguessed_states.remove(_)
            return True
def create_state_list():
    all_states = pandas.read_csv("50_states.csv")
    americuh = all_states["state"].to_list()
    americuh = [x.lower() for x in americuh]
    return americuh
def win_screen():
    write_win = Turtle()
    write_win.hideturtle()
    write_win.penup()
    write_win.color("black")

def get_mouse_click_coor(x, y):
    print(x, y)





youwon = ScreenText()
unguessed_states = create_state_list()
game_is_on = True
# screen.onscreenclick(get_mouse_click_coor)
state = 0
while game_is_on:
    bet = guess_state_prompt(state)
    states = check_guess(bet)
    if states == True:
        state += 1
        youwon.state_text(bet)
    if state == 50:
        youwon.win()
        game_is_on = False


screen.mainloop()

# screen.exitonclick()