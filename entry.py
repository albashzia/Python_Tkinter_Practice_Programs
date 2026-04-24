from tkinter import *

window = Tk()
def submit():
    user_input = entry.get()
    print(user_input)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

entry = Entry(window,
              font=('Arial',50),
              fg='Green')
entry.pack(side=LEFT)


submit_button = Button(window,
                       text="Submit",
                       command=submit)

submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)

delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="Backspace",
                       command=backspace)

backspace_button.pack(side=RIGHT)

window.mainloop()