import random
import string
from tkinter import *

# Create the main window for the generator
# Tkinter is completely new to me so i'm learning this as I go and read the documentation
m = Tk()
m.title("Password Generator")


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

    if lcletters_var.get():
        characters += string.ascii_lowercase
    if ucletters_var.get():
        characters += string.ascii_uppercase
    if numbers_var.get():
        


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
