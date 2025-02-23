from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
# ---------------------------- SEARCH JSON ------------------------------- #
#json.dump() (write)
#json.load() (read)
#json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    size = 10
    letter = string.ascii_letters
    dig = string.digits
    symbol = string.punctuation
    #---
    password = ''.join(random.choice(letter + dig + symbol) for x in range(size))
    pyperclip.copy(password)
    passwordentry.delete(0, END)
    passwordentry.insert(0, password) 
# ---------------------------- SAVE PASSWORD ------------------------------- #
#save into data.txt
def add_to_file():
    website = websiteentry.get()
    email = emailentry.get()
    password = passwordentry.get()
    if website == "":
        messagebox.showinfo(title="ERROR", message="No Website Entered")
    if email == "":
        messagebox.showinfo(title="ERROR", message="No Email Entered")
    if password == "":
        messagebox.showinfo(title="ERROR", message="No Password Entered")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}\nIs this correct?")
        if is_ok == True:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
        else:
            pass
        websiteentry.delete(0, END) #0 is first character, END is last character
        passwordentry.delete(0, END)


#Amazon | lauracain12345@gmail.com | jejcn299s!

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

#LOGO
mypasslogo = PhotoImage(file="logo.png")
logocanvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logocanvas.create_image(100, 100, image=mypasslogo) #half of logocanvas width and height

#WEBSITE ENTRY
websitetext = Label(text="Website:", bg="white")
websiteentry = Entry()
websiteentry.focus() #automatically selects websiteentry

#EMAIL ENTRY
emailtext = Label(text="Email/Username:", bg="white")
emailentry = Entry()
emailentry.insert(0, "gmail@gmail.com") 
#= 0 start of entry, 0th character, you can also use END which is the last character, if you have something already there

#PASSWORD TEXT
passwordtext = Label(text="Password:", bg="white")
passwordentry = Entry()

#GENERATE BUTTON AND ADD BUTTON
generate = Button(text="Generate Password", command=generate_password) #command=action
add = Button(text="Add", command=add_to_file)

#GRID
#logo
logocanvas.grid(column=1, row=0, sticky="EW")

#websitetext and website entry
websitetext.grid(column=0, row=1)
websiteentry.grid(column=1, row=1, columnspan=2, sticky="EW")

#email text and email entry
emailtext.grid(column=0, row=2)
emailentry.grid(column=1, row=2, columnspan=2, sticky="EW") #sticky ew sticks to east and west

#pass text pass entry
passwordtext.grid(column=0, row=3)
passwordentry.grid(column=1, row=3, sticky="EW")

#generate and add
generate.grid(column=2, row=3)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()