from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo("Info Box", "This is an Info Box")
    #messagebox.showwarning("Warning Box", "This is a warning")
    #messagebox.showerror("Error Box", "This is error")
    if(messagebox.askokcancel("Ask Okay/Cancel","Do you want to select it?")):
        print("You selected it")
    else:
        print("You did not select it")

window = Tk()
window.title("Message Box")
window.geometry("300x100")

button = Button(window,
                command=click,
                text="Click Me")
button.pack()

window.mainloop()