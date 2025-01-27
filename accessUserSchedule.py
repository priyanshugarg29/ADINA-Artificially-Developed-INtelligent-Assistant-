#accessUserSchedule

def accessUserSchedule():
    from retriveUserInfo import retriveUserInfo
    userInfo = retriveUserInfo()
    fName = userInfo[0]+"_Calendar"
    loc = fName.index("_")-1
    fName = fName[0:loc] + fName[loc+1:]
    f = open(fName, "r")
    scheduleDetail = f.read()
    if scheduleDetail == "":
        scheduleDetail = []
        scheduleDetail = list(scheduleDetail)
    else:
        scheduleDetail = eval(scheduleDetail)
    return(scheduleDetail)


    
