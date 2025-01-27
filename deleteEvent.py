#deleteEvent
from tkinter import *


def deleteEvent():
    def remove():
        event = str(variable.get())
        from eventPop import eventPop
        eventPop(event)
        from displaySchedule import displaySchedule
        de.destroy()
        displaySchedule()




    
    from retriveSchedule import retriveSchedule
    schedule = retriveSchedule()
    eventName = []
    for i in range(0, len(schedule)):
        eventName.append(schedule[i][0])
    de = Tk()
    de.title("ADINA")
    variable = StringVar(de)
    variable.set(eventName[0])

    L1 = Label(de, text="SELECT EVENT TO BE REMOVED FROM YOUR SCHEDULE")
    L1.grid(row = 0, column = 0)
    O1 = OptionMenu(de, variable, *eventName)
    O1.grid(row = 0, column = 1)
    B1 = Button(de, text = "REMOVE EVENT", command = remove)
    B1.grid(row = 1, column = 1)

    de.mainloop()

