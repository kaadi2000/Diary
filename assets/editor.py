import os
from tkinter import *
from datetime import datetime
from tkinter import messagebox

def run():
    root=Tk("New Entry")
    text=Text(root)
    text.grid()
    def close():
        root.destroy()
    def saveas():
        t = text.get("1.0", "end-1c")
        now = datetime.now()
        filename = now.strftime("%d%m%Y%H%M%S") + ".data"
        with open(filename, 'w') as file1:
            file1.write(t)
        file1.close()
        messagebox.showinfo("+ New Entry", "File Save Successful")
        root.destroy()
    button=Button(root, text="Save", command=saveas)
    button.grid()
    button1 = Button(root, text = "Cancel", command= close)
    button1.grid()

    root.title("+ New Entry")
    root.mainloop()
