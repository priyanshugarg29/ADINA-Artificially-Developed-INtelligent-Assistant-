#todayAgenda
from datetime import date
from tkinter import *

def todayAgenda():
    def allSchedule():
        from displaySchedule import displaySchedule
        ta.destroy()
        displaySchedule()


    
    today = date.today()
    today = str(today)
    today = today[8:]+"/"+today[5:7]+"/"+today[0:4]
    from retriveSchedule import retriveSchedule
    schedule = retriveSchedule()
    agenda = []
    for i in range(0, len(schedule)):
        if(schedule[i][1]==today):
            agenda.append(schedule[i])
    c = 0

    ta = Tk()
    ta.title("ADINA")
    if(len(agenda) == 0):
        L1 = Label(ta, text = "NO EVENT SCHEDULED FOR TODAY")
        L1.grid(row = c, column = 0)
        c+=1
    else:
        for i in range (0, len(agenda)):
            L1 = Label(ta, text = "EVENT NAME: " + agenda[i][0] + "\nSTART TIME: "+ agenda[i][2][0:2]+":"+agenda[i][2][2:] + "\nEND TIME: "+ agenda[i][3][0:2]+":"+agenda[i][3][2:])
            L1.grid(row = c, column = 0)
            c+=1
            L1 = Label(ta, text = "--------------------------------------------------------------------------------------")
            L1.grid(row = c, column = 0)
            c+=1

    B1 = Button(ta, text = "VIEW ALL SCHEDULE", command = allSchedule)
    B1.grid(row = c, column = 0)
            
