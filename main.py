from tkinter import *
from dat import Word

BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Arial", 40, "italic")
FONT_2 = ("Arial", 60, "bold")

# The Word object has the data from csv files and can generate word(s), give english translation for the
# corresponding words and removes the word(s) from the list if known
new_word = Word()


# ----------------------------- CREATE WORD TO LEARN (X) -------------------------------#
def create_text():
    global new_word, flip_timer
    screen.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(fr_word, text=new_word.generate_word(), fill="black")
    canvas.itemconfig(canvas_image, image=image_f)
    flip_timer = screen.after(3000, en_translate)


# -------------------------------- REMOVE WORD IF KNOWN (✔) ---------------------------------#
def remove_text():
    create_text()
    new_word.remove_word()


# --------------------------------- EN TRANSLATION --------------------------------------#
def en_translate():
    global new_word
    canvas.itemconfig(canvas_image, image=image_b)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(fr_word, text=new_word.return_meaning(), fill="white")


# ----------------------------------- UI SETUP ----------------------------------------#
screen = Tk()
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
screen.title("Flash Card")
flip_timer = screen.after(3000, func=en_translate)
# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_f = PhotoImage(file="./images/card_front.png")
image_b = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_f)
card_title = canvas.create_text((400, 150), text="", font=FONT_1)
fr_word = canvas.create_text((400, 263), text="", font=FONT_2)
canvas.grid(column=0, row=0, columnspan=2)
# BUTTONS
image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=image_x, highlightthickness=0, bg=BACKGROUND_COLOR, command=create_text)
button_x.grid(row=1, column=0)

image_c = PhotoImage(file="./images/right.png")
button_c = Button(image=image_c, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_text)
button_c.grid(column=1, row=1)

create_text()  # to have the first word generated

screen.mainloop()
