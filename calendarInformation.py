#calendarInformation
from tkinter import *

def calendarInformation():

    def checkCal():
        m = Month.index(var_month.get()) + 1
        y = E1.get()  
        from displayCalendar import displayCalendar
        cal.destroy()
        displayCalendar(int(m),int(y))

    def display():
        from calendarSchedule import calendarSchedule
        cal.destroy()
        calendarSchedule()


    
    cal = Tk()
    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    var_month = StringVar(cal)
    var_month.set(Month[0])

    L1 = Label(cal, text = "MONTH: ")
    L1.grid(row = 0, column = 0)
    O1 = OptionMenu(cal, var_month, *Month)
    O1.grid(row = 0, column = 1)
    L2 = Label(cal, text = "YEAR: ")
    L2.grid(row = 0 ,column = 2)
    E1 = Entry(cal)
    E1.grid(row = 0, column = 3)
    B1 = Button(cal, text = "CHECK CALENDAR", command = checkCal)
    B1.grid(row = 1, column = 0)
    B2 = Button(cal, text = "BACK", command = display)
    B2.grid(row = 2, column = 0)
    cal.mainloop()

