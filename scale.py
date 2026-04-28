from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+" degree Celsius")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              tickinterval=20,
              font=('Consolas',20))

scale.pack()
button = Button(window,
                text="Submit",
                command=submit)

button.pack()

window.mainloop()