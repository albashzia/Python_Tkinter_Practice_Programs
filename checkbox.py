from tkinter import *

def display():
    if(x.get()):
        print("You agree")
    else:
        print("You disagree")

window = Tk()

x = BooleanVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial',25),
                           fg='green',
                           bg='black',
                           activeforeground='green',
                           activebackground='black',
                           padx=20,
                           pady=20)


check_button.pack()

window.mainloop()