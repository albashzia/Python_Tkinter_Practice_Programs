from tkinter import *

window = Tk()

entry = Entry(window,
              font=('Arial',50))
entry.pack()


submit_button = Button(window,
                       text="Submit")

submit_button.pack()

window.mainloop()