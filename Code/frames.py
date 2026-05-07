from tkinter import *

window = Tk()

Button(window,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(window,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(window,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(window,text="D",font=("Consolas",25),width=3).pack(side=LEFT)


window.mainloop()