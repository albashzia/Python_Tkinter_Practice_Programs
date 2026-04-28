from tkinter import *

window = Tk()

scale = Scale(window,
              from_=100,
              to=0)

scale.pack()
button = Button(window)

button.pack()

window.mainloop()