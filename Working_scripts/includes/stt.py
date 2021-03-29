import speech_recognition as sr
import threading

r = sr.Recognizer()
mic  = sr.Microphone();

#using google speech recogniton

while True :
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except:
            print("Sorry, we did not recognize your voice")

