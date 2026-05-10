from tkinter import *

window = Tk()
window.geometry("220x220")
first_name_label = Label(window,text="First Name: ").grid(row=0,column=0)
first_name_entry = Entry(window).grid(row=0,column=1)

window.mainloop()