from tkinter import *
from tkinter import filedialog
def open_file():
    file_path = filedialog.askopenfilename()
    file = open(file_path,'r')
    print(file.read())
    file.close()

window = Tk()
window.geometry("150x100")
button = Button(window,
                text="Open File")

button.pack()
window.mainloop()