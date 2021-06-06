import tkinter

def run(first_name, second_name, email, phone, dob):
    window = tkinter.Tk()
    window.title("Diary-"+first_name + " " + second_name)
    window.minsize(1000,720)
    window.mainloop()