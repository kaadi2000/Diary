import os, sys
import tkinter
from tkinter.constants import CENTER, TOP
from assets import auth, main_frame

cwd = os.getcwd()+"\icon.png"

os.chdir(os.environ['USERPROFILE'])

if not os.path.exists("Diary"):
    os.makedirs("Diary")

if not os.path.exists("Diary/data"):
    os.makedirs("Diary/data")

os.chdir("Diary")

if not os.path.exists("auth.key"):
    auth.create_auth()
while 1:
    if not os.path.exists("user_Data.data"):
        auth.create_user()
        exit()
    else:
        break

user_data = open('user_Data.data', 'r').read()
user_data=user_data.split()
first_name = user_data[0]
second_name = user_data[1]
email = user_data[2]
phone = user_data[3]
dob = user_data[4]

window = tkinter.Tk()
window.title('Diary')
window.minsize(500,400)
icon = tkinter.PhotoImage(file = cwd)

def destroy():
    window.destroy()

password = tkinter.StringVar()

def verify_login():
    if auth.verify(password.get()):
        destroy()
        main_frame.run(first_name, second_name, email, phone, dob, cwd)
    else:
        wpl = tkinter.Label(text = "Wrong password!!", fg = "red").pack()

def ex():
    sys.exit()

user_Label = tkinter.Label(window, text = "Welcome, " + first_name + " " + second_name,font =("Bahnschrift", 15) ,anchor = CENTER).pack()
password_entry = tkinter.Entry(window, show = "*", textvariable=password, width = 40).pack()
login_button = tkinter.Button(window, text="Login", command = verify_login,bg = "green",font =("Bahnschrift", 12), anchor = CENTER).pack()
exit_button = tkinter.Button(window, text="Exit", command = ex,bg = "red",font =("Bahnschrift", 12), anchor = CENTER).pack()

window.iconphoto(False,icon)
window.resizable(False, False)
window.mainloop()
