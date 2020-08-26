from tkinter import *
from tkinter import messagebox
import os
from PIL import ImageTk, Image

master = Tk()
master.title("Banking App")
master.geometry("250x330")
master.resizable(0, 0)

def toggle_password():
    if check_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def register():
    register_window = Toplevel(master)
    register_window.title("Register")
    global temp_name
    global temp_age
    global temp_password
    temp_name = StringVar()
    temp_age = StringVar()
    temp_password = StringVar()

    txt_label = Label(register_window, text="Please enter your information down below", font=("Calibri", 12))
    txt_label.grid(row=0, sticky=W, pady=10, padx=5)
    name_label = Label(register_window, text="Name :", font=("Calibri", 12))
    name_label.grid(row=1, sticky=W)
    password_label = Label(register_window, text="Password :", font=("Calibri", 12))
    password_label.grid(row=2, sticky=W)
    age_label = Label(register_window, text="Age :", font=("Calibri", 12))
    age_label.grid(row=3, sticky=W)

    global password_entry
    global toggle_check
    global check_var
    check_var = IntVar()
    name_entry = Entry(register_window, textvariable=temp_name)
    name_entry.grid(row=1, column=0)
    password_entry = Entry(register_window, textvariable=temp_password, show="*")
    password_entry.grid(row=2, column=0)
    age_entry = Entry(register_window, textvariable=temp_age)
    age_entry.grid(row=3, column=0)

    toggle_check = Checkbutton(register_window, text="Show", variable=check_var,
                               onvalue=1, offvalue=0, command=toggle_password)
    toggle_check.grid(row=2, sticky=E)
    Button(register_window, text="Register", command=finish_regis, font=("Calibri", 12)).grid(row=4, sticky=N, pady=10)

def finish_regis():
    name = temp_name.get()
    age = temp_age.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or password == "":
        messagebox.showwarning("Warning", "All fields required")
        return

    for name_check in all_accounts:
        if name == name_check:
            messagebox.showwarning("Warning", "Account already exists")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name + "\n")
            new_file.write(password + "\n")
            new_file.write(age + "\n")
            new_file.write("0")
            new_file.close()
    messagebox.showinfo("Completed", "Account has been created!")

def login():
    global temp_login_username
    global temp_login_password
    global login_screen

    temp_login_username = StringVar()
    temp_login_password = StringVar()

    login_screen = Toplevel(master)
    login_screen.title("Login")

    Label(login_screen, text="Fill all fields to login to your account", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10, padx=5)
    Label(login_screen, text="Username:", font=("Calibri", 12)).grid(row=1, sticky=W, padx=5)
    Label(login_screen, text="Password:", font=("Calibri", 12)).grid(row=2, sticky=W, padx=5)

    Entry(login_screen, textvariable=temp_login_username).grid(row=1, padx=80)
    Entry(login_screen, textvariable=temp_login_password, show="*").grid(row=2, padx=80, pady=5)

    Button(login_screen, text="Login", command=login_session, width=8, height=1, font=("Calibri", 12)).grid(row=3, sticky=N, pady=5)

def login_session():
    global login_username
    all_accounts = os.listdir()
    login_username = temp_login_username.get()
    login_password = temp_login_password.get()

    if temp_login_username.get() == "" or temp_login_password.get() == "":
        messagebox.showwarning("Warning", "All fields required")

    for name in all_accounts:
        if name == login_username:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            if login_password == password:
                login_screen.destroy()
                account_screen = Toplevel(master)
                account_screen.title("My Account")

                Label(account_screen, text="My Account", font=("Calibri", 12)).grid(row=0, sticky=N, pady=5, padx=5)
                Label(account_screen, text="Welcome " + name, font=("Calibri", 12)).grid(row=1, sticky=N, pady=5, padx=5)

                Button(account_screen, text="Personal Details", font=("Calibri", 12), width=30, command=personal_details)\
                    .grid(row=2, sticky=N, pady = 5, padx=10)
                Button(account_screen, text="Deposit", font=("Calibri", 12), width=30, command=deposit)\
                    .grid(row=3, sticky=N, pady=5, padx=10)
                Button(account_screen, text="Withdraw", font=("Calibri", 12), width=30, command=withdraw)\
                    .grid(row=4, sticky=N, pady=5, padx=10)
                return
            else:
                messagebox.showerror("Incorrect", "Incorrect username or password")
                return

def personal_details():
    file = open(login_username, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    detail_name = user_details[0]
    detail_age = user_details[2]
    detail_balance = user_details[3]

    details_screen = Toplevel(master)
    details_screen.title("Personal Details")

    Label(details_screen, text="Personal Details", font=("Calibri", 16)).grid(row=0, sticky=N, pady=10, padx=5)
    Label(details_screen, text="Name : " + detail_name, font=("Calibri", 12)).grid(row=1, sticky=W, pady=5, padx=5)
    Label(details_screen, text="Age : " + detail_age, font=("Calibri", 12)).grid(row=2, sticky=W, pady=5, padx=5)
    Label(details_screen, text="Balance : " + detail_balance, font=("Calibri", 12)).grid(row=3, sticky=W, pady=5, padx=5)

def deposit():
    pass

def withdraw():
    pass

img = Image.open("banking.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

Label(master, text="Custom Banking Beta", font=("Calibri", 14)).pack(pady=5)
Label(master, text="Basic Banking App", font=("Calibri", 12)).pack(pady=5)
Label(master, image=img).pack(pady=5)
Button(master, text="Register", font=("Calibri", 12), width=15, command=register).pack(pady=5)
Button(master, text="Login",  font=("Calibri", 12), width=15, command=login).pack(pady=5)

master.mainloop()