#voiceBasedWolframSearch
from tkinter import *

def voiceBasedWolframSearch():
    def startSearch():
        L3 = Label(vbws, text = "listening")
        L3.grid(row = 2, column = 0)
        from wolframBasedSearches import wolframBasedSearches
        from speechRecognition import speechRecognition
        vbws.destroy()
        query = speechRecognition()
        wolframBasedSearches(query)
    
    vbws = Tk()
    vbws.title("ADINA")
    L1 = Label(vbws, text = "Press the speak button and speak your query please")
    L1.grid(row = 0, column = 0)
    B1 = Button(vbws, text = "speak", width = 10, command = startSearch)
    B1.grid(row = 1, column = 0)
    vbws.mainloop()

