import tkinter as tk

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SETUP_CLOSED = False

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


def create_setup_window():
    def submit():
        global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, SETUP_CLOSED

        if entry1.get().strip() and entry2.get().strip() and entry3.get().strip():
            try:
                WORK_MIN = int(entry1.get())
                SHORT_BREAK_MIN = int(entry2.get())
                LONG_BREAK_MIN = int(entry3.get())
                SETUP_CLOSED = True
                setup_window.destroy()

            except ValueError:
                error_label.config(text="Please enter valid numbers.")
        else:
            error_label.config(text="all fields are required.")

    setup_window = tk.Tk()
    setup_window.title("Setup Window")
    setup_window.geometry("400x300")
    setup_window.config(bg=YELLOW)

    tk.Label(setup_window, text="Working minutes:", font=("Arial", 14), bg=YELLOW).pack(pady=10)
    entry1 = tk.Entry(setup_window)
    entry1.insert(0, str(WORK_MIN))
    entry1.pack(pady=5)

    tk.Label(setup_window, text="Short break minutes:", font=("Arial", 14), bg=YELLOW).pack(pady=10)
    entry2 = tk.Entry(setup_window)
    entry2.insert(0, str(SHORT_BREAK_MIN))
    entry2.pack(pady=5)

    tk.Label(setup_window, text="Long break minutes:", font=("Arial", 14), bg=YELLOW).pack(pady=10)
    entry3 = tk.Entry(setup_window)
    entry3.insert(0, str(LONG_BREAK_MIN))
    entry3.pack(pady=5)

    error_label = tk.Label(setup_window, text="", fg="red")
    error_label.pack(pady=5)

    submit_button = tk.Button(setup_window, text="Submit", command=submit)
    submit_button.pack()

    setup_window.mainloop()

    return WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
