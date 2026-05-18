from tkinter import *

def drag_start(event):
    label.startX = event.x
    label.startY = event.y

window = Tk()

label = Label(window,bg='red',width=10,height=5)
label.place(x=0,y=0)

label.bind("<Button-1>",drag_start)

window.mainloop()