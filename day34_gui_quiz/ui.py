import tkinter

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")
SCORE_FONT = ("Arial", 14, "bold")


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quiz")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)
        self.window.option_add("*Background", THEME_COLOR)
        self.label = tkinter.Label(self.window, text="Score:0", fg="white", font=SCORE_FONT)
        self.label.grid(column=1, row=0)
        self.question_canvas = tkinter.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.text_id = self.question_canvas.create_text(150, 125, text=self.quiz_brain.next_question(), font=FONT,
                                                        justify="center",
                                                        width=280)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=20)
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, command=self.press_true)
        self.true_button.grid(column=0, row=2)
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, command=self.press_false)
        self.false_button.grid(column=1, row=2)
        self.window.mainloop()

    def game_over(self):
        text = f"Game Over!\nYour final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}"
        self.question_canvas.itemconfig(self.text_id, text=text)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def press_true(self):
        is_correct = self.quiz_brain.check_answer("True")
        new_score = self.quiz_brain.score
        self.label.configure(text=f"Score:{new_score}")
        self.update_color(is_correct)
        self.window.after(1000, self.next_question)

    def next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            new_question_text = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.text_id, text=new_question_text)
        else:
            self.game_over()

    def update_color(self, is_correct_answer):
        if is_correct_answer:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

    def press_false(self):

        is_correct = self.quiz_brain.check_answer("False")
        new_score = self.quiz_brain.score
        self.label.configure(text=f"Score:{new_score}")
        self.update_color(is_correct)
        self.window.after(1000, self.next_question)
