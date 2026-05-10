from tkinter import *

window = Tk()
window.geometry("220x220")
first_name_label = Label(window,text="First Name: ").pack()
first_name_entry = Entry(window).pack()

window.mainloop()