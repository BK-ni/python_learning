from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# frm = ttk.Frame(root,padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_new_account():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if not check_required_field(website, email, password):
        return

    double_check = messagebox.askokcancel(
        title=website,
        message=f"Your info are: \nEmail: {email_entry}\n"f"Password: {password_entry}")

    if double_check:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", 'w') as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                json.dump(new_data, data_file, indent=4)
                print("New account built successfully")
                for i in info:
                    i.delete(0, END)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                json.dump(data, data_file, indent=4)
                print("New account built successfully")
        finally:
            for i in info:
                i.delete(0, END)
# 有重複的帳號要通知已經註冊
# 由於目前json的格式為{
#       website: {
#       'email': email,
#       'password': password
#       }
# }
# 這種寫法會導致如果我一個網站有多個帳密會無法儲存，所以要修正成以下structure，且新增新user以及網站的寫法要更改:
# data = {
#   website: [
#   {
#       'email': email1,
#       'password': password1
#   },
#   {   'email': email2,
#       'password': password2
#   }
#   ]
# }


def check_required_field(website, email, password):
    if website == "":
        messagebox.showwarning(message="Please enter your website name")
        return False
    elif email == "":
        messagebox.showwarning(message="Please enter your email")
        return False
    elif password == "":
        messagebox.showwarning(message="Please enter your password")
        return False
    return True


def find_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            for website, new_details in new_data.items():
                if website in data:
                    details = data[website]
                    if new_details['email'] == details['email']:
                        messagebox.showinfo(title="Account Information",
                                            message=f"Website: {website}\n"
                                                    f"Username: {details['email']}\n"
                                                    f"Password: {details['password']}")
                    else:
                        messagebox.showwarning(title="Hint", message="No Data File Found")
                else:
                    messagebox.showwarning(title="Hint", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showwarning(title="Hint", message="No details for the website exists")
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Hint", message="No Data")


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx= 20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="W")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W")

# Entry
website_entry = Entry(root, width=25)
website_entry.grid(row=1, column=1, sticky="EW")
email_entry = Entry(root, width=25)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry(root, width=25)
password_entry.grid(row=3, column=1, sticky="EW")

# Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="W")
add_input = Button(root, width=36, text="Add", command=add_new_account)
add_input.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

email_entry.insert(0, "abc123456@gmail.com")

info = [website_entry, password_entry]

root.mainloop()


