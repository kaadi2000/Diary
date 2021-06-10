from tkinter import *
import os
from functools import partial

def view(file_name):
    entry_view = Tk()
    entry_view.title(file_name[:-5])
    file_content = open(file_name,'r').read()
    Message(entry_view, text = file_content).grid()
    entry_view.mainloop()

def old_entries(cwd):
    files = os.listdir()
    old_e = Tk()
    old_e.title("* Old Entries")
    old_e.minsize(650,550)

    imj = PhotoImage(file = cwd, master = old_e)

    k = 0
    j = 0
    for i in files:
        Button(old_e, text = i[:-5], command = partial(view, i)).grid(row = k, column = j)
        j += 1
        if j == 6:
            k += 1
            j = 0

    old_e.iconphoto(False,imj)
    old_e.resizable(False, False)
    old_e.mainloop()
