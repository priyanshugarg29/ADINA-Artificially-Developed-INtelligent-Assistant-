import speech_recognition as sr     # import the library
def speechRecognition():
    r = sr.Recognizer()                 # initialize recognizer
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)# use recognizer to convert our audio into text part.
            return text
        except:
            from speechRecognitionFailed import speechRecognitionFailed
            speechRecognitionFailed()
