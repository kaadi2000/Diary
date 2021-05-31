import string
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from cryptography.fernet import Fernet

def create_auth():
    key = Fernet.generate_key()
    with open("auth.key", "wb") as key_file:
        key_file.write(key)
    key_file.close()
    
def new_user():
    key = open("auth.key", "rb").read()
    fernet = Fernet(key)
    data = [fname.get(), lname.get(), email.get(), contact_number.get(), date.get()]
    with open("master.key", "wb") as key_file:
        key_file.write(fernet.encrypt(pswd.get().encode()))
    key_file.close()
    f = open("user_Data.data", "w")
    for i in data:
        f.write(i+ " ")
    f.close()
    messagebox.showinfo('USER CREATED', "Kindly re-reun the program to access and login with password created!!!")
    exit()

def create_user():
    global fname, lname, email, contact_number, date,pswd
    temp_win = Tk()
    fname = StringVar()
    lname = StringVar()
    email = StringVar()
    contact_number = StringVar()
    date = StringVar()
    pswd = StringVar()
    temp_win.title("New User Registration")
    a = Label(temp_win ,text = "First Name:").grid(row = 0,column = 0)
    ae = Entry(temp_win , textvariable=fname, width = 30).grid(row = 0, column = 1)
    b = Label(temp_win ,text = "Last Name:").grid(row = 1, column = 0)
    be = Entry(temp_win , textvariable=lname, width = 30).grid(row = 1, column = 1)
    c = Label(temp_win ,text = "Email Id:").grid(row = 2, column = 0)
    ce = Entry(temp_win , textvariable=email, width = 30).grid(row = 2, column = 1)
    d = Label(temp_win ,text = "Contact Number:").grid(row = 3, column = 0)
    de = Entry(temp_win , textvariable=contact_number, width = 30).grid(row = 3, column = 1)
    e = Label(temp_win ,text = "Date of Birth:").grid(row = 4, column = 0)
    ee = DateEntry(temp_win,textvariable = date, selectmode = "day", method = 2, width = 27).grid(row = 4, column = 1)
    g = Label(temp_win ,text = "Password:").grid(row = 5, column = 0)
    de = Entry(temp_win , textvariable=pswd, width = 30).grid(row = 5, column= 1)
    f = Button(text="Submit",command = new_user).grid(row = 6,column=0,columnspan=2)
    temp_win.mainloop()
