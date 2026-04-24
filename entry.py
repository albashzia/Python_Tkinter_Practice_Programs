from tkinter import *

window = Tk()
def submit():
    user_input = entry.get()
    print(user_input)

def delete():
    entry.delete(0,END)

entry = Entry(window,
              font=('Arial',50))
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
                       text="Backspace")

backspace_button.pack(side=RIGHT)

window.mainloop()