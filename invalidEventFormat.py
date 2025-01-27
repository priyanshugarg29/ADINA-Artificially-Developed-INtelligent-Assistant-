#invalidEventFormat
from tkinter import *

def invalidEventFormat():
    def tryAgain():
        from setSchedule import setSchedule
        error.destroy()
        setSchedule()

    def welcome():
        from welcomePage import welcomePage
        error.destroy
        welcomePage()

    
    error = Tk()
    error.title("ADINA")
    L1 = Label(error,text =  "INVALID FORMAT OF INPUT DATA")
    L1.grid(row = 0 , column = 0)
    B1 = Button(error,text =  "TRY AGAIN",width = 20, command = tryAgain)
    B1.grid(row = 1, column = 0)
    B2 = Button(error,text =  "BACK TO WELCOME PAGE",width = 20, command = welcome)
    B1.grid(row = 1, column = 1)
    error.mainloop()
