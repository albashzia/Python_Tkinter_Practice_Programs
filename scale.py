from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+" degree Celsius")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0)

scale.pack()
button = Button(window,
                text="Submit")

button.pack()

window.mainloop()