from tkinter import *
from tkinter import colorchooser
def click():
    print("Hello")
window = Tk()
window.geometry("420x420")

button = Button(window, text="Click Here",command=click)
button.pack()
window.mainloop()