from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Exit")

window.mainloop()