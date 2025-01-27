#eventCreated
from tkinter import *

def eventCreated():
    def Welcome():
        from welcomePage import welcomePage
        ec.destroy()
        welcomePage()

    def schedule():
        from setSchedule import setSchedule
        ec.destroy()
        setSchedule()

    def calendar():
        from calendarInformation import calendarInformation
        ec.destroy()
        calendarInformation()

    def display():
        from displaySchedule import displaySchedule
        ec.destroy()
        displaySchedule()


    
    ec = Tk()
    ec.title("ADINA")
    L1 = Label(ec, text = "Event successfully created and added to your schedule")
    L1.grid(row = 0, column = 0)
    B1 = Button(ec, text = "GO BACK TO WELCOME PAGE", width = 30, command = Welcome)
    B1.grid(row = 1, column = 0)
    B2 = Button(ec, text = "CREATE ANOTHER EVENT", width = 30, command = schedule)
    B2.grid(row = 2, column = 0)
    B3 = Button(ec, text = "VIEW CALENDAR", width = 30, command = calendar)
    B3.grid(row = 3, column = 0)
    B4 = Button(ec, text = "VIEW MY SCHEDULE", command = display)
    B4.grid(row = 4, column = 0)
    ec.mainloop()
