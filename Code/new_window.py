from tkinter import *

def create_window():

window = Tk()

Button(window,text="Create New Window",command=create_window).pack()

window.mainloop()