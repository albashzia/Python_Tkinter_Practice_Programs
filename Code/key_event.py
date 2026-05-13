from tkinter import *
def act(event):
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", act)

label = Label(window,font=("Helvetica", 100))
label.pack()

window.mainloop()