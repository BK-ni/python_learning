from tkinter import *
import math
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

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count_down(WORK_MIN*60)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

label_checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)


start = Button(text="start", command=count_down)
start.grid(column=0, row=2)

reset = Button(text="reset")
reset.grid(column=2, row=2)
window.mainloop()
