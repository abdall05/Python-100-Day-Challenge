import tkinter

HEIGHT = 100
WIDTH = 180


def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    label2.config(text=f'{km:.2f}')


def validate_input(new_value):
    return new_value.isdigit() or new_value == "" or new_value.replace(".", "", 1).isdigit()


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20, bg="white")

validate_cmd = window.register(validate_input)
# row0

entry = tkinter.Entry(window, width=10, bg="white", validate="key", validatecommand=(validate_cmd, "%P"))
entry.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles', bg="white")
miles_label.grid(column=2, row=0)

# row1
label1 = tkinter.Label(text='is equal to', bg="white")
label1.grid(column=0, row=1)

label2 = tkinter.Label(text='', bg="white")
label2.grid(column=1, row=1)

label3 = tkinter.Label(text='Km', bg="white")
label3.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', bg="white", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
