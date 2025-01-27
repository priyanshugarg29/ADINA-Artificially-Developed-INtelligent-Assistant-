#displaySchedule
from tkinter import *

def displaySchedule():
    def addEvent():
        from setSchedule import setSchedule
        ds.destroy()
        setSchedule()

    def delete():
        from deleteEvent import deleteEvent
        ds.destroy()
        deleteEvent()

    def agenda():
        from todayAgenda import todayAgenda
        ds.destroy()
        todayAgenda()

    def welcome():
        from welcomePage import welcomePage
        ds.destroy()
        welcomePage()
        
    from sortSchedule import sortSchedule
    sortSchedule()
    from retriveSchedule import retriveSchedule
    schedule = retriveSchedule()

    ds = Tk()
    ds.title("ADINA")
    c = 0
    if(int(len(schedule))==0):
        L1 = Label(ds, text = "-----------------NO EVENT SCHEDULED---------------------")
        L1.grid(row = c, column = 0)
        c+=1
    else:
          
        for i in range (0, int(len(schedule))):
            L1 = Label(ds, text = "event: " + schedule[i][0]+"\t event date: "+schedule[i][1])
            L1.grid(row = c, column = 0)
            c+=1
            L1 = Label(ds, text = "start time: " + schedule[i][2][0:2]+":"+schedule[i][2][2:]+"\t end time: "+schedule[i][3][0:2]+":"+schedule[i][3][2:])
            L1.grid(row = c, column = 0)
            c+=1
            L1 = Label(ds, text = "--------------------------------------------------------")
            L1.grid(row = c, column = 0)
            c+=1
    B1 = Button(ds, text = "ADD AN EVENT", command = addEvent)
    B1.grid(row = c, column = 0)
    c+=1
    B2 = Button(ds, text = "REMOVE AN EVENT", command = delete)
    B2.grid(row = c, column = 0)
    c+=1
    B3 = Button(ds, text = "VIEW TODAY'S AGENDA", command = agenda)
    B3.grid(row = c, column = 0)
    c+=1
    B4 = Button(ds, text = "BACK TO WELCOME PAGE", command = welcome)
    B4.grid(row = c, column = 0)
    ds.mainloop()
