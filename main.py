import pyttsx3
# module for speach recongnition
import pyaudio
# module for getting current time 
import datetime
# module for speech recognition
import speech_recognition as sr
# for searching things on wikipedia
import wikipedia
# for opening web applications
import webbrowser
# for getting current time
import datetime
import os



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# selecting voice 
engine.setProperty('voice',voices[0].id)

# this function wishes user on startup
def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour <12):
        speak("good morning")
    elif(hour>=12 and hour<10):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("tell me how can i help you")


# function for speaking the audio given to it 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#  function converts speach to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=0.2
        audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio)
        print(f"User Said: {query}")
    except Exception as e:
        print("Can't recognise could you please say it again")
        return "None"
    return query
    
    



if __name__=="__main__":
    wish()
    while(True):
        query=takecommand().lower()

        # for basic searching tasks
        if 'wikipedia' in query.lower():
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(f"According to wikipedia {results}")
        # for opening web sites
        sites=[["youtube","http://youtube.com"],["wikipedia"],["http://wikipedia.com"],["google","http://google.com"]]
        for site in sites:
            if(f"open {site[0]}".lower() in query.lower()):
                speak(f"opening {site[0]} ...")
                webbrowser.open(site[1])

        # for current time
        if("the time" in query.lower()):
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
            print(f"Time:{time}")

        #opens desktop applications
        if("vs code" in query.lower()):
            speak("opening vs code")
            codepath="C:\\Users\\ay964\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)       
