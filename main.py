import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found.")

    else:
        if website in data:
            messagebox.showinfo(
                title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            )
        else:
            messagebox.showinfo(title=website, message="No details for the website exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Entry
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

# Search Button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

# Email/Username Label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Email/Username Entry
username_entry = Entry(width=35)
username_entry.insert(0, "myemail@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

# Password Label
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Password Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
