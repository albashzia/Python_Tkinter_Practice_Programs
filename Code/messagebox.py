from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo("Info Box", "This is an Info Box")
    #messagebox.showwarning("Warning Box", "This is a warning")
    #messagebox.showerror("Error Box", "This is error")
    # if(messagebox.askokcancel("Ask Okay/Cancel","Do you want to select it?")):
    #     print("You selected it")
    # else:
    #     print("You did not select it")
    # if(messagebox.askretrycancel("Ask Retry/Cancel","Do you want to retry?")):
    #     print("You Retried")
    # else:
    #     print("You canceled")
    # if (messagebox.askyesno("Ask Yes/No", "Do you like Avocadoes?")):
    #     print("You like avocadoes :) ")
    # else:
    #     print("You don't like avocadoes :(")
    #print(messagebox.askquestion("Ask Question","Do you code?"))
    answer =  (messagebox.askyesnocancel("Ask Yes/No/Cancel", " Do you like to code?"))
    if(answer==True):
        print("You like to code")
    elif (answer==False):
        print("You don't like to code")
    else:
        print("You don't code")

window = Tk()
window.title("Message Box")
window.geometry("300x100")

button = Button(window,
                command=click,
                text="Click Me")
button.pack()

window.mainloop()