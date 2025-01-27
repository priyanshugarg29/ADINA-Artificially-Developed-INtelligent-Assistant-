#displayWikiResults
from tkinter import * #GUI MODULE
import os

def displayWikiResults(res):
    def backToWelcomePage():
        from welcomePage import welcomePage
        dwiki.destroy()
        welcomePage()

    def voiceResult():
        from convertToSpeech import convertToSpeech
        convertToSpeech(res)

    
    dwiki = Tk()
    dwiki.title("ADINA")
    L1 = Label(dwiki, text = res)
    L1.grid(row = 0, column = 0)
    B1 = Button(dwiki, text = "LISTEN TO RESULT", width = 25, command = voiceResult)
    B1.grid(row = 1, column = 0)
    B2 = Button(dwiki, text = "OK", width = 10, command = backToWelcomePage)
    B2.grid(row = 2, column = 0)
    dwiki.mainloop()
