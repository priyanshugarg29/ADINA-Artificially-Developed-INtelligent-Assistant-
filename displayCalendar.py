#displayCalendar
from tkinter import *
import calendar

def displayCalendar(mm, yy):
    def schedule():
        from setSchedule import setSchedule
        c.destroy()
        setSchedule()

    def back():
        from welcomePage import welcomePage
        c.destroy()
        welcomePage()

    
    c = Tk()
    c.title("ADINA")
    cal = calendar.month(yy, mm)
    L1 = Label(c, text = cal)
    L1.grid(row = 0, column = 0)
    B1 = Button(c, text = "CREATE NEW SCHEDULE",width = 30, command = schedule)
    B1.grid(row = 1, column = 0)
    B2 = Button(c, text = "BACK", command = back)
    B2.grid(row= 2, column = 0)
    c.mainloop()


