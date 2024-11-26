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
# for controlling system volume
import pyautogui
# for peforming system tasks
import os
# allow to send https request to websites
import requests
# parse html document and extract specific data
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews

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
        sites=[["youtube","http://youtube.com"],["wikipedia"],["http://wikipedia.com"],["google","http://google.com"],["lc","https://leetcode.com"],["greek for greek","https://www.geeksforgeeks.org"],["stack overflow","https://stackoverflow.com"]]
        for site in sites:
            if(f"open {site[0]}".lower() in query.lower()):
                speak(f"opening {site[0]} ...")
                webbrowser.open(site[1])

        # for current time
        if("the time" in query.lower()):
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
            print(f"Time:{time}")

        # volume control feature
        if('increase volume' in query.lower()):
            pyautogui.press('volumeup')
        elif('decrease volume' in query.lower()):
            pyautogui.press('volumedown')
        elif('volume mute' in query.lower()):
            pyautogui.press('volumemute')

        # fn for saving the reminder
        if 'remember that' in query:
            message=query.replace("remember that","")
            speak("message saved successfully")
            remember=open('data.txt','w')
            remember.write(message)
            remember.close()

        if('tell the last message' in query):
            remember=open("data.txt",'r')
            speak("you tell me that"+remember.read())
            remember.close()
        
       
        if 'news' in query:
            googlenews = GoogleNews()
            googlenews = GoogleNews(lang='en')
            googlenews.search('Tech')
            results = googlenews.get_texts()
            if not results:
                speak("Sorry, I couldn't fetch the news right now.")
            else:
                speak("Here are the latest tech news headlines:")
                for i, headline in enumerate(results[:3]):  # Limiting to 5 headlines
                    speak(f"{i+1}. {headline}")
                    print(f"{i+1}. {headline}")
        

        #opens desktop applications
        if("vs code" in query.lower()):
            speak("opening vs code")
            codepath="C:\\Users\\ay964\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)   

        # tells current temperature
        if("temperature" in query.lower()):
            # construct url for search
            url=f"https://www.google.com/search?q={query}"
            r=requests.get(url)
            # parse r.text to html code
            data=BeautifulSoup(r.text,"html.parser")
            # locate div with class BNeawe
            temp=data.find("div",class_="BNeawe").text
            print(f"Temperature is :{temp}")
            speak(f"current temperature is {temp}")
            
        if("stop" in query.lower()):
            break;
