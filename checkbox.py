from tkinter import *

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You disagree")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)


check_button.pack()

window.mainloop()