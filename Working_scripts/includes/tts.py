import pyttsx3
import threading 

def speech_output(sentence=''):
    # Initialize the engine 
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 150) # Sets speed percent, Can be more than 100 
    engine.setProperty('volume', 1.0)  # Set volume 0-1 

    ''' # for male voice  '''
    #engine.setProperty('voice','english')
    '''  for female voice'''
    #engine.setProperty('voice','english+f1')  # for female voice 1
    #engine.setProperty('voice','english+f2') # for female voice 2
    #engine.setProperty('voice','english+f3') # for female voice 3
    #engine.setProperty('voice','english+f4') # for female voice 4
    engine.setProperty('voice','bulgarian+f4') # for female voice 4

    engine.say(sentence)
    #engine.say("hello_world")      # speak hello_world
    engine.runAndWait()



def speak(sentence):
    t=threading.Thread(target=speech_output,args=(sentence,))
    t.start()
    
    

if __name__ == "__main__":
    #speech_output("Hi, I am you home, speaking through if main, lights turned off, lights turned on, concealed turned off, switch turned on")
    speak("Hi, I am you home, speaking through if main, lights turned off, lights turned on, concealed turned off, switch turned on")
    

    
