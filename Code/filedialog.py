from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("150x100")
button = Button(window,
                text="Open File")

button.pack()
window.mainloop()