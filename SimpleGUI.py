#creating and visulaizing a screen and a button using Tkinter

from tkinter import *

window = Tk()
label = Label(window, text='Welcome to python')
button = Button(window, text='Click me')
label.pack()
button.pack()

window.mainloop()
