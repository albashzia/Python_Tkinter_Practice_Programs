from tkinter import *

def move_up(event):
    canvas.move(carPic,0,-10)

def move_down(event):
    canvas.move(carPic, 0, 10)

def move_left(event):
    canvas.move(carPic, -10,0)

def move_right(event):
    canvas.move(carPic, 10, 0)


window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

carImage = PhotoImage(file="../Icons/racecar40px.png")
carPic = canvas.create_image(0,0,image=carImage,anchor=NW)
window.mainloop()