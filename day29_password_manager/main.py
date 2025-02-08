import tkinter
from tkinter import messagebox
import password_generator
import pyperclip

LOGO_HEIGHT = 200
LOGO_WIDTH = 200

DEFAULT_EMAIL = "myemail@gmail.com"
DATA_FILE_PATH = "data.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = password_generator.generate()
    pyperclip.copy(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if website.strip() == "" or username.strip() == "" or password.strip() == "":
        tkinter.messagebox.showinfo(title="Oops", message="Please fill all fields")

    else:
        message = f"These are the details entered: \nEmail: {username}\nPassword: {password}\n Is it ok to save?"
        is_ok = tkinter.messagebox.askokcancel(title=website, message=message)
        if is_ok:
            with open(DATA_FILE_PATH, "a") as f:
                data_line = f"{website} | {username} | {password}\n"
                f.write(data_line)
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(bg='white', padx=40, pady=20)

window.option_add("*Background", "white")

logo = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT, highlightthickness=0)
canvas.create_image(75, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2, sticky="w")

website_label = tkinter.Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = tkinter.Entry(width=45)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

username_label = tkinter.Label(text='Email/Username:')
username_label.grid(column=0, row=2)
username_entry = tkinter.Entry(width=45)
username_entry.insert(0, DEFAULT_EMAIL)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=24)
password_entry.grid(column=1, row=3, sticky="w")
generate_button = tkinter.Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text='Add', width=38, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
