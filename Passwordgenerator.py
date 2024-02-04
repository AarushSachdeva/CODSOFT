import tkinter
from tkinter import *
import random
import string

Aarush_root = Tk()
Aarush_root.title("Password-Generator")
Aarush_root.geometry("500x360")
Aarush_root.attributes("-toolwindow", 3)
Header = StringVar()
label = Label(Aarush_root, textvariable=Header, anchor=N, pady=15).pack()
Header.set("Password Complexity-")

def selector():
    selection = option.get()

option = IntVar()
c1 = Radiobutton(Aarush_root, text="WEAK", variable=option, value=1, command=selector()).pack(anchor=CENTER)
c2 = Radiobutton(Aarush_root, text="MID", variable=option, value=2, command=selector()).pack(anchor=CENTER)
c3 = Radiobutton(Aarush_root, text="STRONG", variable=option, value=3, command=selector()).pack(anchor=CENTER)
labeloption = Label(Aarush_root)
labeloption.pack()
length_label = StringVar()
length_label.set("Length of Password-")
length_title = Label(Aarush_root, textvariable=length_label).pack()
value = IntVar()
spin_lenghth = Spinbox(Aarush_root, from_=8, to_=32, textvariable=value, width=13).pack()
def back_call():
    lower_sum.config(text=password_generator())

def password_generator():
    if option.get() == 1:
        return "".join(random.sample(lower_upper, value.get()))
    elif option.get() == 2:
        return "".join(random.sample(lower_number, value.get()))
    elif option.get() == 3:
        return "".join(random.sample(all, value.get()))

password_generatorButton = Button(Aarush_root, text="Password-Generation", relief=RIDGE, bd=7, height=3, command=back_call, pady=5)
password_generatorButton.pack()
passcode = str(back_call)
lower_sum = Label(Aarush_root, text="")
lower_sum.pack(side=BOTTOM)

lower_number = string.ascii_uppercase + string.digits + string.ascii_lowercase
lower_upper = string.ascii_uppercase + string.ascii_lowercase
special_character = """`~@#$%^!&*()_-+={}[]|;:"',.?<>/"""
all = special_character + lower_upper + lower_number



Aarush_root.mainloop()
