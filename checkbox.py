from tkinter import *

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0)


check_button.pack()

window.mainloop()