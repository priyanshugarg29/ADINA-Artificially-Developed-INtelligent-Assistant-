def updateUserAttributes(user_attribute):
    from retriveUserInfo import retriveUserInfo
    user_info = retriveUserInfo()
    f = open(user_info[0], "w")
    f.write(str(user_attribute))
    f.close
