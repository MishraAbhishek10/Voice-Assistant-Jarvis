from datetime import datetime
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    speak(c)
    print(c)

    if("date and time" in c.lower()):
        now = datetime.now()
        speak(f"The current time is {now.strftime('%I:%M %p')}")
        speak(f"The current date is {now.strftime('%B %d, %Y')}")
        
    elif("open google" in c.lower()):
        webbrowser.open("https://www.google.com")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://www.facebook.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com")
    
    elif("open amazon" in c.lower()):
        webbrowser.open("https://www.amazon.in/")
    elif(c.lower().startswith("play")):
        try:
            song = c.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        except KeyError:
            speak("Song not found in your music library.")
            

if(__name__ == "__main__"):
    speak("Initializing Jarvis.......")
    # Listen only when name called Jarvis 
    # take audio from microphone as input
    while (True):
        r = sr.Recognizer()
        
        # recognize speech
        print("recognizing ...")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                #speak("Listening...")
                #audio = r.listen(source) 
                audio= r.listen(source,timeout= 5,phrase_time_limit=3) #listen for 5 sec and fast response 

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes !")
                #listen for command 
                with sr.Microphone() as source:
                    print("Jarvis active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("error; {0}".format(e))
        except sr.RequestError as e:
            print("API error; {0}".format(e))




