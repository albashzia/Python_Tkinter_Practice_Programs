from tkinter import *

window = Tk()

listbox = Listbox(window)
listbox.pack()

listbox.insert(0,"Pizza")
listbox.insert(1,"Pasta")
listbox.insert(2,"Garlic Bread")
listbox.insert(3,"Soup")
listbox.insert(4,"Salad")

window.mainloop()