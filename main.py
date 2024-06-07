from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():

    password_entry.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure u haven't let any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():

    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"\nEmail: \n{email}"
                                                           f"\nPassword: \n{password}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
# email_entry.insert(0, "youremail@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W)

#buttons
generate_password_button = Button(text="Gen PWd", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#since linux has messed up padding i had to add few spaces to fit button visually since using width would mess it up
search_button = Button(text="  Search  ", command=find_password)
search_button.grid(column=2, row=1, sticky=N)


window.mainloop()



