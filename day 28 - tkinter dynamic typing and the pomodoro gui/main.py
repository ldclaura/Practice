from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
class Countdown(Tk):
    def __init__(self):
        super().__init__()
        self.seconds = 00
        self.minutes = 00
        self.seconds2 = 00
        self.minutes2 = 00

    def timer_reset(self):

        self.seconds = 00
        self.minutes = 00
        self.seconds2 = 00
        self.minutes2 = 00
        return self.seconds, self.minutes, self.seconds2, self.minutes2


    # ---------------------------- TIMER MECHANISM ------------------------------- # 

        #i won't use this func i just thought i would add itanyway
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

    def my_countdown(self):
        count = True
        print(f"{self.minutes2}{self.minutes}:{self.seconds2}{self.seconds}")
        canvas.itemconfig(timertext, text=f"{self.minutes2}{self.minutes}:{self.seconds2}{self.seconds}")

        self.seconds += 1
        if self.seconds == 10:
            self.seconds2 += 1
            self.seconds = 0

        if self.seconds2 == 6:
            self.minutes += 1
            self.seconds2 = 0

        if self.minutes == 10:
            self.minutes2 += 1
            self.minutes = 0

        if self.minutes2 == 2 and self.minutes == 5 and self.seconds == 1:
            count = False
        elif count == True:
            window.after(1000, Countdown.my_countdown)
start_countdown = Countdown()
    # def countdown():
    #     window.after(1000, say_something, "Hello2")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(thing):
#     print(thing)
# window.after(1000, say_something, "Hello")

tomato = PhotoImage(file="tomato.png")
#TOMATO AND TIME
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timertext = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.itemconfig(1000, text="hello")
#TIMER TEXT
canvas2 = Canvas(width=200, height=100, bg=YELLOW, highlightthickness=0)
canvas2.create_text(100, 50, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
#START
startbutton = Button(text="Start", command=start_countdown.my_countdown) #command=action)
#TICK
canvas3 = Canvas(width=200, height=100, bg=YELLOW, highlightthickness=0)
canvas3.create_text(100, 50, text="✓", fill=GREEN, font=(FONT_NAME, 15, "bold"))
#RESET
resetbutton = Button(text="Reset", command=start_countdown.timer_reset) #command=action)
#ON GRID
canvas.grid(column=2, row=2)
canvas2.grid(column=2, row=1)
startbutton.grid(column=1, row=3)
canvas3.grid(column=2, row=3)
resetbutton.grid(column=3, row=3)

window.mainloop()