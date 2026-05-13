from tkinter import *
def act(event):
    print("You pressed a key")

window = Tk()

window.bind("<Key>", act)
window.mainloop()