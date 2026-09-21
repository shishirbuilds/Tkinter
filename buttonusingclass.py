from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOk = Button(window, text = 'OK', fg = 'red', bg = 'white', command = self.ProcessOK)
        btCancel = Button(window, text="Cancel", fg='Purple', bg='white', command= self.ProcessCancel)
        btOk.pack()
        btCancel.pack()
        
        window.mainloop()
    def ProcessOK(self):
        print('Ok Button is pressed')
    def ProcessCancel(self):
            print('Cancel Button is pressed')
ProcessButtonEvent()