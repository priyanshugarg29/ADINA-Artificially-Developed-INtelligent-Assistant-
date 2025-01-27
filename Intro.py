# import module necessary for the program
from tkinter import *  #GUI
import os              #general file handling
#commands in correspondance to button
def newUser():
    from newUser import newUser
    root.destroy()
    newUser()

def validateUser():
    from validateUser import validateUser
    root.destroy()
    validateUser()

#main program
root = Tk() #initialize GUI window
root.title("ADINA") #GUI title
root.geometry("800x800") #GUI window size
L1 = L1 = Label(root, text = "Welcome to your first hand expiernce with Adina, lets begin")
L1.grid(row = 0, column = 0)
MyButton1 = Button(root, text="new user", width=10, command = newUser)
MyButton1.grid(row=1, column=0)
MyButton1 = Button(root, text="existing user", width=10, command = validateUser )
MyButton1.grid(row=1, column=1)
root.mainloop()
