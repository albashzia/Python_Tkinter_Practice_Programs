from tkinter import *
from tkinter.constants import ACTIVE


def click():
    print("You clicked the button!")

window = Tk()

window.geometry("300x200")
window.title("Buttons")

button = Button(
                window,
                text="Click Me!",
                command=click,
                font=("Comic Sans",30),
                fg='green',
                bg='black',
                activeforeground='green',
                activebackground='black',
                state=ACTIVE
                )
button.pack()

window.mainloop()