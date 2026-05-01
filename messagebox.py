from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo("Info Box", "This is an Info Box")

window = Tk()
window.title("Message Box")
window.geometry("300x100")

button = Button(window,
                command=click,
                text="Click Me")
button.pack()

window.mainloop()