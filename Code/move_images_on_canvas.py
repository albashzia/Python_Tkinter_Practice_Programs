from tkinter import *

window = Tk()

canvas = Canvas(window,width=500,height=500)
canvas.pack()

carImage = PhotoImage(file="../Icons/racecar40px.png")
carPic = canvas.create_image(0,0,image=carImage,anchor=NW)
window.mainloop()