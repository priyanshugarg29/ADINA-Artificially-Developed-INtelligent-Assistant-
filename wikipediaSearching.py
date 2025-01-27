#wikipediaSearching
from tkinter import * #GUI MODULE
import os
import wikipedia

def wikipediaSearching(query):
    wk = wikipedia.page(query)
    temp = wk.content
    res = ""
    res = ""
    for i in temp:
        if (i == "." or i ==";" or i ==","):
            res = res + i + " \n"
        elif(i != "\n"):
            res = res + i
        else:
            break
    from displayWikiResults import displayWikiResults
    displayWikiResults(res)
