import random
import string
from tkinter import *
from tkinter import ttk
import time
import pyperclip

# Create the main window for the generator
# Tkinter is completely new to me so i'm learning this as I go and read the documentation
m = Tk()
m.title("Password Generator")


# Calculating center as well
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
# Calculate x, y center coords
x_axis = (screen_width // 2) - (800 // 2)
y_axis = (screen_height // 2) - (600 // 2)

# Resize the window to be larger and postion it
m.geometry(f"800x600+{x_axis}+{y_axis}")


# Copy password straight to clipboard
def copyPassword(password):
    pyperclip.copy(password)


def is_valid_pass(password):
    if lcletters_var.get() and not any(c in string.ascii_lowercase for c in password):
        return False
    if ucletters_var.get() and not any(c in string.ascii_uppercase for c in password):
        return False
    if numbers_var.get() and not any(c in string.digits for c in password):
        return False
    if symbols_var.get() and not any(c in "!@#$%^&*" for c in password):
        return False
    return True


# function to generate password
# I want to have a selection of choices to make the password that is generated, how the user wants
def generate_password():
    # This is where I tested all the values to make surew I was using them correctly

    # print(length_slider.get())
    # if lcletters_var.get():
    #     print("Lowercase Checked!")
    # if ucletters_var.get():
    #     print("Uppercase Checked!")
    # if numbers_var.get():
    #     print("Numbers Checked!")
    # if symbols_var.get():
    #     print("Symbols Checked!")

    # Variable holds length
    length = length_slider.get()

    # all available characters depending on inputs
    characters = ""

    # If statements to gather which characters the user wants
    if lcletters_var.get():
        characters += string.ascii_lowercase
    if ucletters_var.get():
        characters += string.ascii_uppercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += "!@#$%^&*"

    # If statement to check that atleast one value was checked
    if not characters:
        print("Please select atleast one character type")
        return

    # Adding progress bar because I just found it
    progress_bar = ttk.Progressbar(m, orient=HORIZONTAL, length=200, mode="determinate")
    progress_bar.pack(pady=10)
    progress_bar["value"] = 0
    for i in range(101):
        progress_bar["value"] = i
        m.update_idletasks()
        time.sleep(0.005)
        if i == 100:
            progress_bar.destroy()

    # Generate password AND validate it!
    while True:
        password = "".join(random.choice(characters) for eachChar in range(length))
        if is_valid_pass(password):
            break

    print(f"Generated Password: {password}")

    copy_btn = Button(m, text="Copy Password", command=lambda: copyPassword(password))
    copy_btn.pack()


# Label for length slider
length_label = Label(m, text="Length:")
length_label.pack()

# Slider or as tkinter calls it scale widget
length_slider = Scale(m, from_=8, to=32, orient=HORIZONTAL, length=200, tickinterval=24)
length_slider.set(16)
length_slider.pack()

# Variables to hold if checkbox is checked or not
# Will add radio buttuns eventually to toggle between Passphrase, and Password
lcletters_var = BooleanVar()
ucletters_var = BooleanVar()
numbers_var = BooleanVar()
symbols_var = BooleanVar()

# Checkboxes
Checkbutton(m, text="a-z", variable=lcletters_var).pack()
Checkbutton(m, text="A-Z", variable=ucletters_var).pack()
Checkbutton(m, text="0-9", variable=numbers_var).pack()
Checkbutton(m, text="!@#$%^&*", variable=symbols_var).pack()


# Generate button
generate_btn = Button(m, text=f"Generate Password", command=generate_password)
generate_btn.pack()

m.mainloop()
