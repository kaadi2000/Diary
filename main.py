import os
import tkinter
from assets import backup, editor, first

windows_path = os.environ['USERPROFILE'].split('\\')
username = windows_path[-1]
windows_wd = windows_path[0][0]

os.chdir(os.environ['USERPROFILE'])
if not os.path.exists("Diary"):
    os.makedirs("Diary")
if not os.path.exists("Diary/data"):
    os.makedirs("Diary/data")
os.chdir("Diary")
if not os.path.exists("auth.key"):
    first.create_auth()
while 1:
    if not os.path.exists("user_Data.data"):
        first.create_user()
        exit()
    else:
        break

window = tkinter.Tk()
window.title('Diary')

window.mainloop()