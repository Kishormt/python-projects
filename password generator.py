import string
from tkinter import *
import pyperclip
import random

root = Tk()

root.geometry("800x600")

input_pass = StringVar()
pass_len = IntVar()
pass_len.set(0)


def generate():
    combinations = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                    '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password = ""

    for i in range(pass_len.get()):
        password = password + random.choice(combinations)

    input_pass.set(password)

def CopyToClipboard():
    input_password = input_pass.get()
    pyperclip.copy(input_password)

Label(root, text="Password Generator Application", font="jost 30 bold").pack()

Label(root, text="Enter password length", font="jost 20").pack(pady=7)

Entry(root, textvariable=pass_len, font='20').pack(pady=3)

Button(root, text="Generate Password", command=generate).pack(pady=7)

Entry(root, textvariable=input_pass, font='20').pack(pady=3)

Button(root, text="Copy", command=CopyToClipboard).pack()

root.mainloop()

