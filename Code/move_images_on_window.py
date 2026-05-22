from tkinter import *

def move_up(event):
    label.place(x = label.winfo_x(),y= label.winfo_y()-10)

window = Tk()

window.geometry("300x300")
carImage = PhotoImage(file="../Icons/racecar40px.png")
label = Label(window,image=carImage)
label.place(x=0,y=0)

window.bind("<w>",move_up)

window.mainloop()