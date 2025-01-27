#reportEventClash
from tkinter import *

def reportEventClash():
    def newEvent():
        from setSchedule import setSchedule
        clash.destroy()
        setSchedule()

    def welcome():
        from welcomePage import welcomePage
        clash.destroy()
        welcomePage()


    
    clash = Tk()
    clash.title("ADINA")
    L1 = Label(clash, text = "YOUR NEW EVENT CLASHES WITH AN EXISTING EVENT YOU HAVE SCHEULED, KINDLY RESCHEDULE EITHER OF THE EVENT")
    L1.grid(row = 0, column = 0)
    B1 = Button(clash, text = "Enter New event", command = newEvent)
    B1.grid(row = 1, column = 0)
    B2 = Button(clash, text = "Back to welcome page", command = welcome)
    B2.grid(row = 2, column = 0)
    clash.mainloop()
