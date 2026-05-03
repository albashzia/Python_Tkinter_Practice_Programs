from tkinter import *
from tkinter import filedialog
def open_file():
    file_path = filedialog.askopenfilename(title="Select a File",
                                           filetypes=(('Text','*.txt'),
                                                      ("All File","*.*")))
    file = open(file_path,'r')
    print(file.read())
    file.close()

window = Tk()
window.geometry("150x100")
button = Button(window,
                text="Open File",
                command=open_file)

button.pack()
window.mainloop()