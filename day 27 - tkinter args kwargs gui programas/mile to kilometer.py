from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100) #minimum size
window.config(padx=20, pady=20)

def mile_to_km():
    change_label = kilometers.config(text=round(float(entry.get())*1.609))
    return change_label


entry = Entry(width=5)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 10, "bold")) #can't see label
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "bold")) #can't see label
is_equal_to.grid(column=0, row=1)

kilometers = Label(text="0", font=("Arial", 10, "bold")) #can't see label
kilometers.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 10, "bold")) #can't see label
km.grid(column=2, row=1)


button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)
window.mainloop() #while true, stays at very end.