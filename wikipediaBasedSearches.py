#wikipediaBasedSearches
from tkinter import * #GUI MODULE
import os
import wikipedia

def wikipediaBasedSearches():
    def wikiSearchButton():
        from wikipediaSearching import wikipediaSearching
        query = E1.get()
        wiki.destroy()
        wikipediaSearching(query)

    def wikiVoiceSearchButton():
        wiki.destroy()
        

    wiki = Tk()
    wiki.title("ADINA")
    L1 = Label(wiki, text = "what wikipedia seach do you want to make ")
    L1.grid(row = 0, column = 0)
    E1 = Entry(wiki)
    E1.grid(row = 1, column = 0)
    B1 = Button(wiki, text = "Search", width = 10, command = wikiSearchButton)
    B1.grid(row = 2, column = 0)
    B2 = Button(wiki, text = "make voice search instead", width = 25, command = wikiVoiceSearchButton)
    B2.grid(row = 2, column = 1)
    L2 = Label(wiki, text = "NOTE: Under upgradation may take time to retrieve result")
    L2.grid(row = 3, column = 0)
    wiki.mainloop()

