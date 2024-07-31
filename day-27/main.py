from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New text")


# Button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)


button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click me second", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

window.mainloop()

