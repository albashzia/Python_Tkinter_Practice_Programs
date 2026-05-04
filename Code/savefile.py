from tkinter import *
from tkinter import filedialog

window = Tk()

text = Text(window)
text.pack()

button = Button(window,
                text="Save")
button.pack()

window.mainloop()