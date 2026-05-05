from tkinter import *

window = Tk()
def open():
    print("You opened a file")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=open)
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Exit")

window.mainloop()