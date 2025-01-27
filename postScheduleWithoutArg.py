#postScheduleWithoutArg

def postScheduleWithoutArg(schedule):
    from retriveUserInfo import retriveUserInfo
    user_info = retriveUserInfo()
    fName = user_info[0]+"_Calendar"
    loc = fName.index("_")-1
    fName = fName[0:loc]+ fName[loc+1:]
    f = open(fName, "w")
    f.write(str(schedule))
    f.close
