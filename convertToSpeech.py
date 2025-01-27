#convertToSpeech
import pyttsx3

def convertToSpeech(speech):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1
    engine.say(speech)
    engine.runAndWait()
