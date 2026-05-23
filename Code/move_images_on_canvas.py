from tkinter import *

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