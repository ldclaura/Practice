import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300) #minimum size

#components
#labels
my_label = tkinter.Label(text="this is my label", font=("Arial", 24, "bold")) #can't see label
my_label.config(text="New Text")
# my_label.pack(expand="true") #can see label expand is middle of screen
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#update properties
# my_label["text"] = "New Text"


#button
def button_clicked():
    # my_label["text"] = "Button Got Clicked"
    my_label.config(text="Button Got Clicked")
    print("I got clicked")


#button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack(expand="true")

#entry

input = tkinter.Entry(width=10)
input.pack(expand="True")
print(input.get())

def return_entry(event):
    change_label = my_label.config(text=input.get())
    return change_label

window.bind('<Return>', return_entry)
window.mainloop() #while true, stays at very end.
