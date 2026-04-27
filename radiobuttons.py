from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()


pizzaImage = PhotoImage(file='pizza_40px.png')
burgerImage = PhotoImage(file='burger_40px.png')
hotdogImage = PhotoImage(file='hotdog_40px.png')

foodImages = [pizzaImage,burgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               pady=15,
                               font=('Impact',30),
                               image= foodImages[index],
                               compound='left'
                               )
    radio_button.pack(anchor=W)

window.mainloop()