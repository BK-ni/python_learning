from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles = Label(text="Miles")
is_equal_to = Label(text="is equal to")
km = Label(text="KM")

miles.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
km.grid(column=2, row=1)

km_answer = Label()
km_answer.grid(column=1, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)


def calculate():
    answer = float(input.get())*1.609344
    km_answer.config(text=f"{answer}")


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
