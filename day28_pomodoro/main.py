import time
import tkinter

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 200
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 32, "bold")
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
iteration = 1
pause = True
reset = False
finished_countdown = False


def format_time(minutes, seconds=0):
    return f"{minutes:02}:{seconds:02}"


def clear_check_marks():
    check_mark_label.config(text='')


def add_check_mark():
    text = check_mark_label["text"]
    text = text + '✅'
    check_mark_label.config(text=text)


def get_time():
    current_time = canvas.itemcget(timer_text, "text")
    minutes, seconds = current_time.split(':')
    return int(minutes), int(seconds)


def reset_pomodoro():
    global reset
    reset = True


def clean_after_reset():
    global iteration
    clear_check_marks()
    canvas.itemconfig(timer_text, text=format_time(WORK_MIN))
    label.config(text="Timer", fg=GREEN)
    start_pause_button.config(text='Start')

    iteration = 1


def pause_pomodoro():
    global pause
    pause = True
    start_pause_button.config(text='Start')


def start_pomodoro():
    global pause
    pause = False
    start_pause_button.config(text='Pause')
    window.update()
    minutes, seconds = get_time()
    start_pomodoro_cycles(minutes, seconds)


def start_pause_pomodoro():
    global pause, iteration
    if pause:
        start_pomodoro()

    else:
        pause_pomodoro()


def start_pomodoro_cycles(current_minutes, current_seconds):
    global reset, pause, iteration, finished_countdown
    if iteration % 8 == 0:
        label.config(text="Long Break", fg=RED)
    elif iteration % 2 == 1:
        label.config(text="Working Session", fg=GREEN)

    else:
        label.config(text="Short Break", fg=PINK)

    countdown(current_minutes, current_seconds)
    if finished_countdown:
        if iteration % 2 == 1:
            add_check_mark()

        iteration += 1
        finished_countdown = False

    while not reset:
        if not pause:
            if iteration % 8 == 0:
                label.config(text="Long Break", fg=RED)
                countdown(LONG_BREAK_MIN)
            elif iteration % 2 == 1:
                label.config(text="Working Session", fg=GREEN)
                countdown(WORK_MIN)

            else:
                label.config(text="Short Break", fg=PINK)
                countdown(SHORT_BREAK_MIN)

            if finished_countdown:
                if iteration % 2 == 1:
                    add_check_mark()

                iteration += 1
                finished_countdown = False
        else:
            window.update()

    if reset:
        clean_after_reset()
        reset = False
        pause = True


def countdown(minutes, seconds=0):
    global finished_countdown
    total_seconds = minutes * 60 + seconds
    while total_seconds >= 0 and not reset and not pause:
        minutes, seconds = divmod(total_seconds, 60)
        time_left = format_time(minutes, seconds)
        canvas.itemconfig(timer_text, text=time_left)
        window.update_idletasks()
        window.update()

        time.sleep(0.1)

        total_seconds -= 1
    if total_seconds < 0:
        finished_countdown = True


window = tkinter.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=50, pady=50)

label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=FONT,width=15)
label.pack()

image = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(102, 130, text=format_time(WORK_MIN), fill="white", font=FONT)
canvas.pack()

check_mark_label = tkinter.Label(text="", bg=YELLOW, fg=GREEN)
check_mark_label.pack()

start_pause_button = tkinter.Button(text="Start", command=start_pause_pomodoro)
start_pause_button.pack(side=tkinter.LEFT)

reset_button = tkinter.Button(text="reset", command=reset_pomodoro)
reset_button.pack(side=tkinter.RIGHT)

window.mainloop()
