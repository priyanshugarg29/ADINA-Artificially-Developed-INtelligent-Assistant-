#import modules
from tkinter import * #GUI MODULE
import os



#main program after validating user to login
def welcomePage():

       def webSearch():
              from webSearches import webSearches
              hello.destroy()
              webSearches()

       def wikiSearch():
              from wikipediaBasedSearches import wikipediaBasedSearches
              hello.destroy()
              wikipediaBasedSearches()

       def calendar():
              from calendarSchedule import calendarSchedule
              hello.destroy()
              calendarSchedule()


       
       hello = Tk()
       hello.title("ADINA")
       from retriveUserInfo import retriveUserInfo
       user_info = retriveUserInfo()
       L1 = Label(hello, text = "welcome "+ user_info[0])
       L1.grid(row = 0, column = 0)
       L2 = Label(hello, text = "what would you like to do?")
       L2.grid(row = 1, column = 0)
       B1 = Button(hello, text = "make internet search", width = 25, command = webSearch)
       B1.grid(row = 2, column = 0)
       B2 = Button(hello, text = "make wikipedia search", width = 25, command = wikiSearch)
       B2.grid(row = 3, column = 0)
       B3 = Button(hello, text = "Calender and Schedule Planner", width = 25, command = calendar)
       B3.grid(row = 4, column = 0)
       hello.mainloop()



