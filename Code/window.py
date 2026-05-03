from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("First Frame ")

icon = PhotoImage(file='../Icons/pic.png')
window.iconphoto(True,icon)

window.config(background="black")

window.mainloop()