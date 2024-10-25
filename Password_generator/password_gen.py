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
    # Code in here
    print("Password Generate")


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
