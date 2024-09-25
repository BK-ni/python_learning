from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
TEXT_FONT = ("Arial", 60, "bold")


try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
    print(original_data)
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


def is_known():
    to_learn.remove(current_card)
    data_remain = pd.DataFrame(to_learn)
    print(data_remain)
    data_remain.to_csv('data/words_to_learn.csv', index=False)
    next_card()


root = Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, flip_card)

# create images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


# canvas.create_image(400, 400, image= card_back_img)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Language", fill="black", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 253, text="Text", fill="black", font=TEXT_FONT)


canvas.grid(row=0, column=0, columnspan=2)
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()
root.mainloop()

# 如果都沒有答對則不會開新檔案