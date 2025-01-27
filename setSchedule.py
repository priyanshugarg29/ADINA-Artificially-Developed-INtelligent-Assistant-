#setSchedule
from tkinter import *

def setSchedule():
    def validateEvent():
#First we are going to validate all data format
        EventDetails = []
        eventName = str(Event.get())
        EventDetails.append(eventName)
#date validation
        eventDate = str(date.get())
        if eventDate.count("/")==2 and len(eventDate) == 10:
            if eventDate[0:2].isdigit and eventDate[3:5].isdigit and eventDate[6:].isdigit:
                EventDetails.append(eventDate)
            else:
                from invalidEventFormat import invalidEventFormat
                ss.destroy()
                invalidEventFormat()
        else:
            from invalidEventFormat import invalidEventFormat
            ss.destroy()
            invalidEventFormat()
#start time validation
        eventStart = str(startTime.get())
        if eventStart.count(":") == 1 and len(eventStart) == 5:
            if eventStart[0:2].isdigit and (int(eventStart[0:2])>= 0 and int(eventStart[0:2])<=23) and eventStart[3:].isdigit and (int(eventStart[3:])>= 0 and int(eventStart[3:])<=59):
                eventStart = eventStart[0:2]+eventStart[3:]
                EventDetails.append(eventStart)
            else:
                from invalidEventFormat import invalidEventFormat
                ss.destroy()
                invalidEventFormat()
        else:
                from invalidEventFormat import invalidEventFormat
                ss.destroy()
                invalidEventFormat()
#end time validation
                
        eventEnd = str(endTime.get())
        if eventEnd.count(":") == 1 and len(eventEnd) == 5:
            if eventEnd[0:2].isdigit and (int(eventEnd[0:2])>= 0 and int(eventEnd[0:2])<=23) and eventEnd[3:].isdigit and (int(eventEnd[3:])>= 0 and int(eventEnd[3:])<=59):
                eventEnd = eventEnd[0:2]+eventEnd[3:]
                EventDetails.append(eventEnd)
            else:
                from invalidEventFormat import invalidEventFormat
                ss.destroy()
                invalidEventFormat()
        else:
                from invalidEventFormat import invalidEventFormat
                ss.destroy()
                invalidEventFormat()
#now finally comparing this data with other events to check anamolies
        from compareEvent import compareEvent
        flag = compareEvent(EventDetails)
# if flag = 1  ==> event clash
# if flag = 0  ==> event does not clash
        if flag == 1:
            from reportEventClash import reportEventClash
            ss.destroy()
            reportEventClash()

        else:
            from postEvent import postEvent
            postEvent(EventDetails)
            from eventCreated import eventCreated
            ss.destroy()
            eventCreated()


    
    ss = Tk()
    ss.title("ADINA")
    L1 = Label(ss, text = "Enter Details of the event you want to access")
    L1.grid(row = 0, column = 0)
    L2 = Label(ss, text = "Event Name")
    L2.grid(row = 2, column = 0)
    Event = Entry()
    Event.grid(row = 2, column = 1)
    L2 = Label(ss, text = "date (dd/mm/yyyy):")
    L2.grid(row = 3, column = 0)
    date = Entry()
    date.grid(row = 3, column = 1)
    L3 = Label(ss, text = "Event start time (24hrs format[hh:min]): ")
    L3.grid(row = 4, column = 0)
    startTime = Entry()
    startTime.grid(row = 4, column = 1)
    L4 = Label(ss, text = "Event end time (24hrs format [hh:min]): ")
    L4.grid(row = 5, column = 0)
    endTime = Entry()
    endTime.grid(row = 5, column = 1)
    B1 = Button(ss, text = "Post Event To My Schedule", width = 30, command = validateEvent)
    B1.grid(row = 6, column = 0)
    ss.mainloop()
