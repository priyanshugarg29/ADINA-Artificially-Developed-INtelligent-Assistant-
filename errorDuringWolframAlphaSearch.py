from tkinter import *


def errorDuringWolframAlphaSearch():
    def goingBackToWelcomePage():
        from welcomePage import welcomePage
        wf.destroy()
        welcomePage()
        
    
    wf = Tk()
    wf.title("ADINA")
    L1 = Label(wf,text = "Sorry could not make your search right now, please try again after sometime")
    L1.grid(row = 0, column = 0)
    B1 = Button(wf, text = "GO BACK", width = 15, command = goingBackToWelcomePage)
    B1.grid(row = 1, column = 0)
    wf.mainloop()
