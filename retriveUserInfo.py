def retriveUserInfo():
    f = open("currentuserCache", "r")
    user_info = f.read()
    temp_string = ""
    info_list = []
    count = 0
    for i in user_info:
        if (i =="[" or i== "]" or i==","):
            continue
        elif(i == "'"):
            count+=1
            if(count%2 != 0):
                if(temp_string != ""):
                    info_list.append(temp_string)
                temp_string = ""
        else:
            temp_string = temp_string + i
    return(info_list)

