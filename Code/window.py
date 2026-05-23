#importing package
from tkinter import *

#instantiating a window
window = Tk()

#defining the size of the window
window.geometry("500x500")

#defining the title of the window
window.title("First Frame ")

#creating a photo icon and setting it as window's icon
icon = PhotoImage(file='../Icons/pic.png')
window.iconphoto(True,icon)

#setting the background of the window to black
window.config(background="black")

#making the window visible
window.mainloop()