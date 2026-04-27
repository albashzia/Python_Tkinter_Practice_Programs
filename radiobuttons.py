from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index])
    radio_button.pack()

window.mainloop()