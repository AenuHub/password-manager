from tkinter import *
import random, string, os

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Validate input
    if not website or not email or not password or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        popup = Toplevel()
        popup.title("Error")
        error_label = Label(popup, text="Please fill in all the fields correctly.")
        error_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
        ok_button = Button(popup, text="Ok", command=popup.destroy)
        ok_button.grid(column=1, row=1, padx=10, pady=10)
        return

    # Create data.txt if it doesn't exist and check if the combination already exists
    if not os.path.exists("data.txt"):
        with open("data.txt", "w") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
    else:
        with open("data.txt", "r") as data_file:
            data = data_file.readlines()
            if any(website in line and email in line and password in line for line in data):
                popup = Toplevel()
                popup.title("Error")
                error_label = Label(popup, text="Username, email, password combination already exists.\nPlease try again.")
                error_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
                ok_button = Button(popup, text="Ok", command=popup.destroy)
                ok_button.grid(column=1, row=1, padx=10, pady=10)
            else:
                with open("data.txt", "a") as data_file:
                    popup = Toplevel()
                    popup.title("Are you sure?")
                    confirmation_label = Label(popup, text=f"Are you sure you want to save this password?\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
                    confirmation_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
                    yes_button = Button(popup, text="Yes", command=lambda: [popup.destroy(), data_file.write(f"{website} | {email} | {password}\n")])
                    yes_button.grid(column=0, row=1, padx=10, pady=10)
                    no_button = Button(popup, text="No", command=popup.destroy)
                    no_button.grid(column=1, row=1, padx=10, pady=10)
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# Generate a random password with at least 2 symbols, 3 digits and is 12 characters long
def generate_password():
    symbols = random.sample(string.punctuation, min(2, len(string.punctuation)))
    digits = random.sample(string.digits, min(3, len(string.digits)))
    letters = random.sample(string.ascii_letters, 12 - len(symbols) - len(digits))
    password_list = symbols + digits + letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="we")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="we")
email_entry.insert(0, "mail@example.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="we")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="e", padx=(5,0))

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="we", pady=(5,0))

window.mainloop()