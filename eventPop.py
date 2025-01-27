#eventPop

def eventPop(eventName):
    from retriveSchedule import retriveSchedule
    schedule = retriveSchedule()
    for i in range (0, int(len(schedule))):
        if(schedule[i][0]==eventName):
            break
    schedule.pop(i)
    from postScheduleWithoutArg import postScheduleWithoutArg
    postScheduleWithoutArg(schedule)
