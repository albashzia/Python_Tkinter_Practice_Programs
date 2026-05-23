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
        percent.set(str(int((x/tasks)*100))+"%")
        task.set(str(x)+"/"+str(tasks)+" tasks completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
task = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(padx=10,pady=10)

percent_label = Label(window,textvariable=percent).pack()
tasks_label = Label(window,textvariable=task).pack()

Button(window,text="Download", command=start).pack()

window.mainloop()