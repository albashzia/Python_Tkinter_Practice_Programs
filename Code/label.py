from tkinter import *

window = Tk()
window.geometry("1000x1000")

photo = PhotoImage(file='../Icons/python.png')

label = Label(window,
              text="Hello World",
              font=('Arial',20,'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

#label.place(x=0,y=0)
label.pack()

window.mainloop()