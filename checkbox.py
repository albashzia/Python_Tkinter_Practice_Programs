from tkinter import *

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x)


check_button.pack()

window.mainloop()