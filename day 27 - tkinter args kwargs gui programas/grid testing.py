import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300) #minimum size
window.config(padx=200, pady=200)

my_label = tkinter.Label(text="this is my label", font=("Arial", 24, "bold")) #can't see label
my_label.config(text="New Text")

my_label.grid(column=0, row=0)

my_label2 = tkinter.Label(text="this is my label", font=("Arial", 24, "bold")) #can't see label
my_label2.config(text="New Text", padx=20, pady=20)

my_label2.grid(column=1, row=0)

button = tkinter.Button(text="Click Me")
button.grid(column=3, row=0)
window.mainloop() #while true, stays at very end.