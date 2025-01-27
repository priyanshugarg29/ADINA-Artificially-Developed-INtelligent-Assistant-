#compareEvent
def compareEvent(currentEvent):
    from accessUserSchedule import accessUserSchedule
    events = accessUserSchedule()
    if(len(events)==0):
        return 0
    else:
        for i in events:
            if (i[1] == currentEvent[1]):
                if(currentEvent[2]>= i[2] and currentEvent[2]<= i[3] or currentEvent[3]>= i[2] and currentEvent[3]<= i[3]):
                    return 1
    return 0
                    
