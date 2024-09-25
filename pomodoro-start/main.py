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
reps = 0
timer = None
mark = []
# ---------------------------- TIMER RESET ------------------------------- # 


def time_reset():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
    else:
        rest()


def rest():
    global reps
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 != 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark.append("✔")
        mark_out = ''.join(mark)
        label_checkmark.config(text=mark_out)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)


start = Button(text="start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="reset", command=time_reset)
reset.grid(column=2, row=2)
window.mainloop()

# bug: start 可以重複按，導致timer錯亂