from tkinter import *
def act(event):
    print("You pressed a key")

window = Tk()

window.bind("<Key>", act)

label = Label(window,"Helvetica", 100)
label.pack()

window.mainloop()