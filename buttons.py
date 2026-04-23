from tkinter import *

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
                activebackground='black'
                )
button.pack()

window.mainloop()