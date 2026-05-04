from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile()

window = Tk()

text = Text(window)
text.pack()

button = Button(window,
                text="Save",
                command=save_file)
button.pack()

window.mainloop()