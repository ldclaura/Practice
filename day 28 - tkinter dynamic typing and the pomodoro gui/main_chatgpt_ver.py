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
        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg=YELLOW)

        # Time variables
        self.seconds = 0
        self.minutes = 0
        self.seconds2 = 0
        self.minutes2 = 0
        self.fivemin = False

        # UI setup
        self.tomato = PhotoImage(file="tomato.png")
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=2, row=2)

        # Timer text
        self.canvas2 = Canvas(width=200, height=100, bg=YELLOW, highlightthickness=0)
        self.timetext = self.canvas2.create_text(100, 50, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
        self.canvas2.grid(column=2, row=1)

        # Start and reset buttons
        self.start_button = Button(text="Start", command=self.my_countdown)
        self.start_button.grid(column=1, row=3)

        self.reset_button = Button(text="Reset", command=self.timer_reset)
        self.reset_button.grid(column=3, row=3)

        # Tick mark
        self.canvas3 = Canvas(width=200, height=100, bg=YELLOW, highlightthickness=0)
        self.canvas3.create_text(100, 50, text="✓", fill=GREEN, font=(FONT_NAME, 15, "bold"))
        self.canvas3.grid(column=2, row=3)

    def timer_reset(self):
        # Reset all time variables and update the display
        self.seconds = 0
        self.minutes = 0
        self.seconds2 = 0
        self.minutes2 = 0
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.on = False

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def my_countdown(self):
        self.on = True
        self.timetext = self.canvas2.itemconfig(self.timetext, text="Work")

        # Update the timer display
        self.canvas.itemconfig(self.timer_text, text=f"{self.minutes2}{self.minutes}:{self.seconds2}{self.seconds}")

        # Increment seconds and manage overflow
        if self.on == True:
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

            # Stop the countdown at 25 minutes (Pomodoro duration)
            if self.minutes2 == 0 and self.minutes == 1 and self.seconds == 1 and self.fivemin == False:
                self.timetext = self.canvas2.itemconfig(self.timetext, text="Break")
                print("25 mins")
                self.fivemin = True
                self.timer_reset()
                # return
            #5 MINUTES
            if self.minutes == 5 and self.seconds == 1 and self.fivemin == True:
                self.timetext = self.canvas2.itemconfig(self.timetext, text="Work")
                print("5 minutes")
                self.fivemin = False
                self.timer_reset()
                self.my_countdown()
                # return
            else:
                # Schedule the next update after 1 second
                self.after(1000, self.my_countdown)

# Start the countdown timer application
start_countdown = Countdown()
start_countdown.mainloop()