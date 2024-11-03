# module for speach recongnition
import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# selecting voice 
engine.setProperty('voice',voices[0].id)

def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour <12):
        speak("good morning")
    elif(hour>=12 and hour<10):
        speak("good afternoon")
    else:
        speak("good evening")


# function for speaking the audio given to it 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("hello")