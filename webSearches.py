#import necessary modules
from tkinter import *
import os
from retriveUserInfo import retriveUserInfo
#main program
def webSearches():
    def SearchButton():
        from wolframBasedSearches import wolframBasedSearches 
        query = E1.get()
        wolf.destroy()
        wolframBasedSearches(query)
        
    def VoiceSearchButton():
        from voiceBasedWolframSearch import voiceBasedWolframSearch
        wolf.destroy()
        voiceBasedWolframSearch()

    
    wolf = Tk()
    wolf.title("ADINA")
    user_info = retriveUserInfo()
    L1 = Label(wolf, text = "Hello "+ user_info[0]+ " what can I search for you?")
    L1.grid(row = 0, column = 0)
    E1 = Entry(wolf)
    E1.grid(row = 1, column = 0)
    B1 = Button(wolf, text = "Search", width = 10, command = SearchButton)
    B1.grid(row = 2, column = 0)
    B2 = Button(wolf, text = "make voice search instead", width = 25, command = VoiceSearchButton)
    B2.grid(row = 2, column = 1)
    wolf.mainloop()

