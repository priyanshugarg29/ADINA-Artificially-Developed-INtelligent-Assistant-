#sortSchedule

def sortSchedule():
    from retriveSchedule import retriveSchedule
    schedule = retriveSchedule()
    l = len(schedule)
    for i in range(0, l):
        schedule[i][1] = schedule[i][1].replace("/","")
        schedule[i][1] = schedule[i][1][4:]+schedule[i][1][2:4]+schedule[i][1][0:2]
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (schedule[j][1] > schedule[j+1][1]):
                temp = schedule[j]
                schedule[j] = schedule[j+1]
                schedule[j+1] = temp
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (schedule[j][1] == schedule[j+1][1]):
                if(schedule[j][2] > schedule[j+1][2]):
                    temp = schedule[j]
                    schedule[j] = schedule[j+1]
                    schedule[j+1] = temp
    for i in range(0, l):
        schedule[i][1] = schedule[i][1][6:]+"/"+schedule[i][1][4:6]+"/"+schedule[i][1][0:4]
    
    from postScheduleWithoutArg import postScheduleWithoutArg
    postScheduleWithoutArg(schedule)
            
