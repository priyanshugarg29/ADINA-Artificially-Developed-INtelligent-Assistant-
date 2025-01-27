#AccessUserAttributes
import os
from retriveUserInfo import retriveUserInfo
import ast

def accessUserAttributes():
    user_info = retriveUserInfo()
    f = open(user_info[0], "r")
    user_attribute = f.read()
    user_attribute = eval(user_attribute)
    return(user_attribute)

