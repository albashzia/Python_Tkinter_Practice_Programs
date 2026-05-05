from tkinter import *

window = Tk()
def open():
    print("You opened a file")

def save():
    print("You saved a file")

def cut():
    print("You cutted some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Exit", command=quit)

edit_menu = Menu(menubar)
menubar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)

window.mainloop()