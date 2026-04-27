from tkinter import *

food = ["pizza","hamburger","hotdog"]

pizza = PhotoImage('pizza_40px.png')
burger = PhotoImage('burger_40px.png')
hotdog = PhotoImage('hotdog_40px.png')

window = Tk()

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               pady=15,
                               font=('Impact',30)
                               )
    radio_button.pack(anchor=W)

window.mainloop()