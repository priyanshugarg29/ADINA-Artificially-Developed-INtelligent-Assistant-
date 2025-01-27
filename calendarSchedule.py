#calendarSchedule
from tkinter import *

def calendarSchedule():
    def calendar():
        from calendarInformation import calendarInformation
        cs.destroy()
        calendarInformation()

    def schedule():
        from displaySchedule import displaySchedule
        cs.destroy()
        displaySchedule()

    
    cs = Tk()
    cs.title("ADINA")
    L1 = Label(cs, text = "WHAT WOULD YOU LIKE TO DO? \n (VIEW CALENDAR/VIEW MY SCHEDULE)")
    L1.grid(row = 0, column = 0)
    B1 = Button(cs, text = "VIEW CALENDAR", command = calendar)
    B1.grid(row = 1, column = 0)
    B2 = Button(cs, text = "MY SCHEDULE", command = schedule)
    B2.grid(row = 2, column = 0)
    cs.mainloop()


    
