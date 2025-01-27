from tkinter import *

def displayWolframResult(query, result):
    def goBackToWelcomePage():
        from welcomePage import welcomePage
        searchResult.destroy()
        welcomePage()

    def listenResult():
        from convertToSpeech import convertToSpeech
        convertToSpeech(result)
        
    searchResult = Tk()
    searchResult.title("ADINA")
    query = "QUERY: " + query
    L0 = Label(searchResult, text = query)
    L0.grid(row = 0, column = 0)
    L1 = Label(searchResult, text = "The result for your query is: ")
    L1.grid(row = 1, column = 0)
    L2 = Label(searchResult, text = result)
    L2.grid(row = 2, column = 0)
    B1 = Button(searchResult, text = "GO BACK",  width = 10, command = goBackToWelcomePage)
    B1.grid(row = 4, column = 0)
    B2 = Button(searchResult, text = "LISTEN TO RESULT",  width = 20, command = listenResult)
    B2.grid(row = 3, column = 0)
    searchResult.mainloop()
