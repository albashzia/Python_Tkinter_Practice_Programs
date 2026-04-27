from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()


pizzaImage = PhotoImage(file='pizza_40px.png')
burgerImage = PhotoImage(file='burger_40px.png')
hotdogImage = PhotoImage(file='hotdog_40px.png')

foodImages = [pizzaImage,burgerImage,hotdogImage]

x = IntVar()

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif (x.get()==1):
        print("You ordered burger")
    elif (x.get()==2):
        print("You ordered hotdog")

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               pady=15,
                               font=('Impact',30),
                               image= foodImages[index],
                               compound='left',
                               indicatoron=0,
                               width=275,
                               command=order
                               )
    radio_button.pack(anchor=W)

window.mainloop()