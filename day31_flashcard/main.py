import random
import tkinter
import pandas

from words_manager import WordsManager

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000
FLASHCARD_HEIGHT = 526
FLASHCARD_WIDTH = 800
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")
COUNTDOWN = 3000
future_function_id = None
current_word_index = None

words_manager = WordsManager()


def on_close():
    words_manager.save_data()
    window.destroy()


def flip_card(word_to_reveal):
    flash_card.itemconfig(flash_card_image, image=card_back_image)
    flash_card.itemconfig(text1, text="Explanation", fill="white")
    flash_card.itemconfig(text2, text=word_to_reveal, fill="white")


def recognised_word():
    global current_word_index
    words_manager.update_weight(current_word_index)
    show_card()


def show_card():
    global future_function_id, current_word_index
    if future_function_id:
        window.after_cancel(future_function_id)
    flash_card.itemconfig(flash_card_image, image=card_front_image)
    current_word_index = words_manager.next_word_index()
    word_pair = words_manager.next_word(current_word_index)
    flash_card.itemconfig(text1, text="French", fill="black")
    flash_card.itemconfig(text2, text=word_pair[0], fill="black")
    future_function_id = window.after(COUNTDOWN, flip_card, word_pair[1])


window = tkinter.Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
window.option_add("*Background", BACKGROUND_COLOR)
window.option_add("*highlightThickness", 0)

# Flashcard
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
flash_card = tkinter.Canvas(width=FLASHCARD_WIDTH, height=FLASHCARD_HEIGHT)
flash_card_image = flash_card.create_image(FLASHCARD_WIDTH / 2, FLASHCARD_HEIGHT / 2, image=card_front_image)
flash_card.grid(row=0, column=0, columnspan=2)
text1 = flash_card.create_text(400, 150, font=FONT1, text="text1")
text2 = flash_card.create_text(400, 263, font=FONT2, text="text2")

# Buttons
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(window, image=wrong_image, command=show_card)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(window, image=right_image, command=recognised_word)
right_button.grid(row=1, column=1)

window.protocol("WM_DELETE_WINDOW", on_close)

show_card()

window.mainloop()
