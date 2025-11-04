from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

    next_card()


# window
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
# 3 secs call flip_card
flip_timer = window.after(3000, func=flip_card)

# images
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# text
card_background = canvas.create_image(400, 263, image=front_image)
card_word = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_title = canvas.create_text(400, 263, text="", font=("Ariel", 40, "italic"))

# buttons
button_right = Button(image=right_image, highlightthickness=0, command=is_known)
button_right.grid(column=0, row=1)
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=1)

next_card()

window.mainloop()
