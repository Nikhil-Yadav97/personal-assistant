# module for speach recongnition
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# selecting voice 
engine.setProperty('voice',voices[0].id)

# function for speaking the audio given to it 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("hello")