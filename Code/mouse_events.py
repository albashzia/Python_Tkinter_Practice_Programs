from tkinter import *

def act(event):
    print("Cursor Coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>",act)
window.bind("<Button-3>",act)


window.mainloop()