from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               pady=15)
    radio_button.pack(anchor=W)

window.mainloop()