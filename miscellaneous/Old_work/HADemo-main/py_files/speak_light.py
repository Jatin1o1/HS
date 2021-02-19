import pyttsx3
engine = pyttsx3.init()
def say(text):
    engine.say(text)
    engine.runAndWait()
say("lights have been turned off ")
