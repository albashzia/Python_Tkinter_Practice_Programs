from tkinter import *
from tkinter.constants import ACTIVE

count = 0
def click():
    global count
    count+=1
    print(count)

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