from tkinter import *

mystring = ""

def button_clicked():
    kilometers = input.get()
    convert["text"] = int(kilometers) * 1.6

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)

input = Entry(width=15)
input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 15, "bold"))
miles.grid(column=2, row=0)
miles.config(padx=20, pady=10)

equal = Label(text="is equal to ", font=("Arial", 15, "bold"))
equal.grid(column=0, row=1)
equal.config(padx=20, pady=10)

convert = Label(text=0, font=("Arial", 15, "bold"))
convert.grid(column=1, row=1)
convert.config(padx=20, pady=10)

km = Label(text="Km", font=("Arial", 15, "bold"))
km.grid(column=2, row=1)
km.config(padx=20, pady=10)

button = Button(text="click me!", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=20, pady=10)

window.mainloop()