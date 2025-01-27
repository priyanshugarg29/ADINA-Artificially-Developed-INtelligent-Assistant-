#importing required modules
import csv
from tkinter import *
import os

#main program
def newUser():
    def ENTRY():
        from welcomePage import welcomePage
        temp = [E1.get(),E2.get(),int(E3.get()), E4.get(), E5.get()]
        top.destroy()
        print(temp)
        with open('UserCredentials.csv', 'a', newline = '') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(temp)
        csvFile.close()
        f = open(str(temp[0]),"w")
        keywords = [["what",0],["why",0],["how",0],["does",0]]
        f.write(str(keywords))
        f.close()
        f = open("currentuserCache","w")
        f.write(str(temp))
        f.close()
        cal = str(temp[0])+"_Calendar"
        f = open(str(cal),"w")
        f.close()
        welcomePage()
    top = Tk()
    top.title("ADINA")
    L1 = Label(top, text = "Name")
    L1.grid(row = 0, column = 0)
    E1 = Entry(top)
    E1.grid(row = 0, column = 1)
    L2 = Label(top, text = "Gender")
    L2.grid(row = 1, column = 0)
    E2 = Entry(top)
    E2.grid(row = 1, column = 1)
    L3 = Label(top, text = "Age")
    L3.grid(row = 2, column = 0)
    E3 = Entry(top)
    E3.grid(row = 2, column = 1)
    L4 = Label(top, text = "Username")
    L4.grid(row = 3, column = 0)
    E4 = Entry(top)
    E4.grid(row = 3, column = 1)
    L5 = Label(top, text = "Password")
    L5.grid(row = 4, column = 0)
    E5 = Entry(top)
    E5.grid(row = 4, column = 1)
    MyButton1 = Button(top, text="Submit", width=10, command = ENTRY)
    MyButton1.grid(row=5, column=1)


    top.mainloop()
