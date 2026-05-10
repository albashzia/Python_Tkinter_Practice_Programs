from tkinter import *

window = Tk()
window.geometry("220x220")
first_name_label = Label(window,text="First Name: ").grid(row=0,column=0)
first_name_entry = Entry(window).grid(row=0,column=1)

last_name_label = Label(window,text="Last Name: ").grid(row=1,column=0)
last_name_entry = Entry(window).grid(row=1,column=1)

email_label = Label(window,text="Email: ").grid(row=2,column=0)
email_entry = Entry(window).grid(row=2,column=1)

window.mainloop()