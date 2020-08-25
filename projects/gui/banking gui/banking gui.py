from tkinter import *
import os
from PIL import ImageTk, Image

master = Tk()
master.title("Banking App")

def toggle_password():
    if check_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def register():
    register_window = Toplevel(master)
    register_window.title("Register")

    temp_name = StringVar()
    temp_age = StringVar()
    temp_password = StringVar()

    txt_label = Label(register_window, text="Please enter your information down below", font=("Calibri", 12))
    txt_label.grid(row=0, sticky=W, pady=10, padx=5)
    name_label = Label(register_window, text="Name :", font=("Calibri", 12))
    name_label.grid(row=1, sticky=W)
    age_label = Label(register_window, text="Age :", font=("Calibri", 12))
    age_label.grid(row=2, sticky=W)
    password_label = Label(register_window, text="Password :", font=("Calibri", 12))
    password_label.grid(row=3, sticky=W)

    global password_entry
    global toggle_check
    global check_var
    check_var = IntVar()
    name_entry = Entry(register_window, textvariable=temp_name)
    name_entry.grid(row=1, column=0)
    age_entry = Entry(register_window, textvariable=temp_age)
    age_entry.grid(row=2, column=0)
    password_entry = Entry(register_window, textvariable=temp_password, show="*")
    password_entry.grid(row=3, column=0)
    toggle_check = Checkbutton(register_window, text="Show", variable=check_var,
                               onvalue=1, offvalue=0, command=toggle_password)
    toggle_check.grid(row=3, sticky=E)
    Button(register_window, text="Register", command=finish_regis, font=("Calibri", 12)).grid(row=4, sticky=N, pady=10)




def finish_regis():
    pass

def login():
    pass

img = Image.open("banking.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

Label(master, text="Custom Banking Beta", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=5)
Label(master, text="Basic Banking App", font=("Calibri", 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N)

Button(master, text="Register", font=("Calibri", 12), width=15, command=register).grid(row=3, sticky=N)
Button(master, text="Login",  font=("Calibri", 12), width=15, command=login).grid(row=4, sticky=N, pady=10)
master.mainloop()