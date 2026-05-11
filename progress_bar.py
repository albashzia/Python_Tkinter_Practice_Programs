from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1

window = Tk()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(padx=10,pady=10)
Button(window,text="Download").pack()
window.mainloop()