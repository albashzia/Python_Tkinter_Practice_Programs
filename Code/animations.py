from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

x_velocity = 1
y_velocity = 1

window = Tk()

canvas = Canvas(window, width= WIDTH, height= HEIGHT)
canvas.pack()

background_image = PhotoImage(file="../Icons/space_background_500px.png")
canvas_background = canvas.create_image(0,0,image=background_image,anchor=NW)

ufo_image = PhotoImage(file="../Icons/ufo_80px.png")
canvas_image = canvas.create_image(0,0,image=ufo_image,anchor=NW)

while True:
    coordinates = canvas.coords(canvas_image)
    print(coordinates)
    canvas.move(canvas_image,x_velocity,y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()