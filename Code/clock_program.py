from tkinter import *
from time import *
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)


window = Tk()

time_label = Label(window,font=("Arial",50),bg="black",fg="green")
time_label.pack()

update()

window.mainloop()