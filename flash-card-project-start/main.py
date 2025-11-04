from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# window
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

# images
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=front_image)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
button_right = Button(image=right_image, highlightthickness=0)
button_right.grid(column=0, row=1)
button_wrong = Button(image=wrong_image, highlightthickness=0)
button_wrong.grid(column=1, row=1)


window.mainloop()
