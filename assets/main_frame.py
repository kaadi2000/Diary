from tkinter import*
import sys, os

bground = "#00003f"

def run(first_name, second_name, email,phone, dob, cwd):
    global main_frame, temp
    temp = cwd[0:-9]

    main_frame = Tk()
    main_frame.title("Diary")
    main_frame.geometry("550x400")
    main_frame.configure(bg = bground)

    icon = PhotoImage(file = cwd)

    name_label = Label(main_frame, text="Welcome, "+first_name + " " + second_name, bg = bground, fg = "white", font = ("Century",22)).grid(row = 0, column=0)
    email_label = Label(main_frame, text = "Email: " + email,bg = bground, fg = "white", font = ("Goudy Old Style",15)).grid(row = 1, column=0,sticky="w", pady = 5)
    phone_label = Label(main_frame, text = "Phone: " + phone,bg = bground, fg = "white", font = ("Goudy Old Style",15)).grid(row = 2, column=0,sticky="w", pady =5)
    dob_label = Label(main_frame, text = "DOB: " + dob,bg = bground, fg = "white", font = ("Goudy Old Style",15)).grid(row = 3, column=0,sticky="w", pady = 5)
    
    ne_button = Button(main_frame,text = "+ New Entry",command = new_entry, fg = "white", bg = "green", font = ("Goudy Old Style",15)).grid(row = 4, column=0,sticky="w", pady = 5)
    oe_button = Button(main_frame,text = "* Old Entries",command = old_entries, fg = "white", bg = "green", font = ("Goudy Old Style",15)).grid(row = 5, column=0,sticky="w", pady = 5)
    lo_button = Button(main_frame,text = "Log Out",command = logout, fg = "white", bg = "red", font = ("Goudy Old Style",14)).grid(row = 0, column=1,sticky="w", pady = 5, padx = 5)
    e_button = Button(main_frame,text = "Exit",command = ex, fg = "white", bg = "black", font = ("Goudy Old Style",14)).grid(row = 0, column=2,sticky="w", pady = 5, padx = 5)
    
    main_frame.iconphoto(False,icon)
    main_frame.resizable(False, False)
    main_frame.mainloop()

def new_entry():
    os.chdir("data")
    from assets import editor
    editor.run()

def old_entries():
    pass

def logout():
    os.chdir(temp)
    main_frame.destroy()
    import main

def ex():
    sys.exit()
