from tkinter import *

window = Tk()

window.geometry("300x300")
carImage = PhotoImage(file="../Icons/racecar40px.png")
label = Label(window,image=carImage)
label.place(x=0,y=0)

window.mainloop()