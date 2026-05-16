from tkinter import *

def act(event):
    print("Left key pressed")

window = Tk()

window.bind("<Button-1>",act)


window.mainloop()