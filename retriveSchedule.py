#retriveSchedule

def retriveSchedule():
    from retriveUserInfo import retriveUserInfo
    user_info = retriveUserInfo()
    fName = user_info[0] + "_Calendar"
    loc = fName.index("_")-1
    fName = fName[0:loc]+fName[loc+1:]
    temp = []
    f = open(fName, "r")
    schedule = f.read()
    if schedule == "":
        return(temp)
    else:
        schedule = eval(schedule)
        return(schedule)
