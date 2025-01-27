#speechRecognitionFailed
from tkinter import *

def speechRecognitionFailed():
    def goBack():
        from welcomePage import welcomePage
        speechFail.destroy()
        welcomePage()
        
    speechFail = Tk()
    speechFail.title("ADINA")
    L1 = Label(speechFail, text = "Sorry could not understand what you said, kindly try again")
    L1.grid(row = 0, column = 0)
    B1 = Button(speechFail, text = "GO BACK", width = 15, command = goBack)
    B1.grid(row = 1, column = 0)
    speechFail.mainloop()

