from tkinter import *
from tkinter import messagebox
import pandas
import random
import time
# import string
# import pyperclip
# import json
def flip_card(pick):
    flashcard.delete("all") #deletes all, including title background, so i add it again.
    flashcard.create_image(400, 263, image=flashcardback) #half of logocanvas width and height
    flashcard.create_text(400, 150, font="Ariel 40 italic", text="English")
    flashcard.create_text(400, 263, font="Ariel 60 bold", text=pick[1])
    print(pick)
    print(pick[0])
    print(pick[1])

def random_french_eng():
    with open("data\\french_words.csv", "r") as file:
        data = pandas.read_csv(file)
        french_eng_dict = {row.French: row.English for (index, row) in data.iterrows()}
        random_french_english = random.choice(list(french_eng_dict.items()))
        print(random_french_english)
        flashcard.delete("all") #deletes all, including title background, so i add it again.
        flashcard.create_image(400, 263, image=flashcardfront) #half of logocanvas width and height
        flashcard.create_text(400, 150, font="Ariel 40 italic", text="French")
        flashcard.create_text(400, 263, font="Ariel 60 bold", text=random_french_english[0])
        return random_french_english



BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#FLASHCARD
flashcardfront = PhotoImage(file="images\\card_front.png")
flashcardback = PhotoImage(file="images\\card_back.png")
flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

rando = random_french_eng()

# flashcard.create_image(400, 263, image=flashcardfront) #half of logocanvas width and height
# flashcard.create_text(400, 150, font="Ariel 40 italic", text="French")
# flashcard.create_text(400, 263, font="Ariel 60 bold", text=french_eng_pick)

#X
x = PhotoImage(file="images\\wrong.png")
wrong = Button(window, image=x, command=random_french_eng, borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR)


#TICK
tick = PhotoImage(file="images\\right.png")
right = Button(window, image=tick, command=random_french_eng, borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR)
# right = Canvas(width=200, height=200, highlightthickness=0, bg=BACKGROUND_COLOR)
# right.create_image(100, 100, image=tick)
#= 0 start of entry, 0th character, you can also use END which is the last character, if you have something already there
#SEARCH BUTTON
searchbutton = Button(text="Search")
#PASSWORD TEXT
passwordtext = Label(text="Password:", bg="white")
passwordentry = Entry()

#GENERATE BUTTON AND ADD BUTTON
generate = Button(text="Generate Password") #command=action
add = Button(text="Add")

#GRID
#logo
flashcard.grid(column=0, row=0, columnspan=2, sticky="EW")

#websitetext and website entry
wrong.grid(column=0, row=1)

right.grid(column=1, row=1)

window.mainloop()