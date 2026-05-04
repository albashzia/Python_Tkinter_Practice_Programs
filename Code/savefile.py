from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt")
    file_text = text.get("1.0",END)
    file.write(file_text)
    file.close()

window = Tk()

text = Text(window)
text.pack()

button = Button(window,
                text="Save",
                command=save_file)
button.pack()

window.mainloop()