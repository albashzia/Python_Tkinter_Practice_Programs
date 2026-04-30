from tkinter import *

def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered:")
    for foods in food:
        print(foods)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#F7FFDE',
                  font=('Constantia',30),
                  width = 12,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(0,"Pizza")
listbox.insert(1,"Pasta")
listbox.insert(2,"Garlic Bread")
listbox.insert(3,"Soup")
listbox.insert(4,"Salad")
listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

add_button = Button(window,
                text="Add",
                command=add)
add_button.pack()

delete_button = Button(window,
                text="delete",
                command=delete)
delete_button.pack()

submit_button = Button(window,
                text="Submit",
                command=submit)
submit_button.pack()

window.mainloop()