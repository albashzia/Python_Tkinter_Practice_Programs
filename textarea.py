from tkinter import *

window = Tk()

text = Text(window)

text.pack()

button = Button(window,
                text="Submit")
button.pack()
window.mainloop()