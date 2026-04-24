from tkinter import *

window = Tk()
def submit():
    user_input = entry.get()
    print(user_input)

entry = Entry(window,
              font=('Arial',50))
entry.pack()


submit_button = Button(window,
                       text="Submit",
                       command=submit)

submit_button.pack()

window.mainloop()