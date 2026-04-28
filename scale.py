from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+" degree Celsius")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              tickinterval=10,
              font=('Consolas',10),
              showvalue=0,
              resolution=5,
              troughcolor='#69EAEE',
              fg='#FF1C00',
              bg='#111111')

scale.set(50)
scale.pack()
button = Button(window,
                text="Submit",
                command=submit)

button.pack()

window.mainloop()