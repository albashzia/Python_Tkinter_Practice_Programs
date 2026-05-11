from tkinter import *
from tkinter.ttk import *
import time

window = Tk()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(padx=10,pady=10)
Button(window,text="Download").pack()
window.mainloop()