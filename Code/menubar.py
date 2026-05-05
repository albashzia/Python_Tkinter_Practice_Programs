from tkinter import *

window = Tk()
def open():
    print("You opened a file")

def save():
    print("You saved a file")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Exit", command=quit)

window.mainloop()