from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
#CANVAS
        self.canvas1 = Canvas(width=130,bg=THEME_COLOR, highlightthickness=0)
        self.canvas2 = Canvas(width=130,bg=THEME_COLOR, highlightthickness=0) #Score: 0
        self.canvas3 = Canvas(width=300, height=250, bg="white", highlightthickness=0) #text
        self.canvas4 = Canvas(width=150, height=250, bg="white", highlightthickness=0)
        self.canvas5 = Canvas(width=130,bg=THEME_COLOR, highlightthickness=0) #img
        self.canvas6 = Canvas(width=130,bg=THEME_COLOR, highlightthickness=0) #img
#TEXT BUTTONS ETC
        self.question_text = self.canvas3.create_text(150, 125, width=280, text=self.get_next_question, fill=THEME_COLOR, font=FONT)
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false)
        self.scoretext = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "italic"))
#GRID
        # self.canvas1.grid(column=0, row=0)
        self.scoretext.grid(column=1, row=0, sticky="E", padx=10, pady=10)
        self.canvas3.grid(column=1, row=1)
        # self.canvas4.grid(column=1, row=1, sticky="EW")
        self.true_button.grid(column=1, row=2, sticky="W", padx=20, pady=20)
        self.false_button.grid(column=1, row=2, sticky="E", padx=20, pady=20)
        
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas3.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas3.itemconfig(self.question_text, text=q_text)
        #self.canvas3.configure(bg="white")
        self.scoretext.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "italic"))

    def true(self):

        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer("True"))

        else:
            self.canvas3.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

             
    def false(self):
        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer("False"))

        else:
            self.canvas3.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
    # def give_feedback(self, is_right):
    #     if is_right:
    #         self.canvas3.config(bg="green")
    #         self.window.after(1000, self.canvas3.config(bg="white"))
    #     else:
    #         self.canvas3.config(bg="red")
    #         self.window.after(1000, self.canvas3.config(bg="white"))
    #         # self.window.after(1000, self.canvas3.config(bg="white"))
            

    def give_feedback(self, is_right):
        if is_right:
            self.canvas3.config(bg="green")
        else:
            self.canvas3.config(bg="red")
        self.window.after(1000, self.get_next_question)

        