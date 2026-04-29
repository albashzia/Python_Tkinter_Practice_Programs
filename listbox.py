from tkinter import *

def submit():
    print(listbox.get(listbox.curselection()))
window = Tk()

listbox = Listbox(window,
                  bg='#F7FFDE',
                  font=('Constantia',30),
                  width = 12)
listbox.pack()
listbox.insert(0,"Pizza")
listbox.insert(1,"Pasta")
listbox.insert(2,"Garlic Bread")
listbox.insert(3,"Soup")
listbox.insert(4,"Salad")
listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

submit_button = Button(window,
                text="Submit",
                command=submit)
submit_button.pack()

window.mainloop()