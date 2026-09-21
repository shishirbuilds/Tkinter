from tkinter import *
def processok():
    print('OK button is clicked')
def processCancel():
    print('Cancel button is clicked')

window = Tk()
btOK = Button(window, text='OK', fg='red', bg='black', command= processok)
btcancel = Button(window, text='cancel', fg='green', command= processCancel)

btOK.pack()
btcancel.pack()
window.mainloop()
