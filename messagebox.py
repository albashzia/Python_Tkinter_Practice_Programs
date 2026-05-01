from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Message Box")
window.geometry("300x100")

button = Button(window,
                command=click,
                text="Click Me")
button.pack()

window.mainloop()