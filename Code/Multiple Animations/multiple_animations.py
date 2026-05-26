from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width= WIDTH, height= HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,5,2,"white")
tennis_ball = Ball(canvas,0,0,50,4,5,"red")
basket_ball = Ball(canvas,0,0,125,8,6,"orange")


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()