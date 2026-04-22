from tkinter import *

window = Tk()
window.geometry("300x300")
label = Label(window,
              text="Hello World",
              font=('Arial',20,'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)

label.place(x=0,y=0)
#label.pack()

window.mainloop()