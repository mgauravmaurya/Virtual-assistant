import pywhatkit as pwk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import os
import webbrowser
from googlesearch import search


master= ("Gaurav")


# functions of project
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def listentome():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)
        
    try:
        print("Recognizing")
        action = r.recognize_google(audio,language="en-in")
        print(f"working on: {action}\n")
        action=action.lower()
        return action
    except Exception as e:
        speak("I am unable to recognize. Please say again..")
        listentome()


def phonebook(action):
    Aneesh=8417999600
    Dev=7880715118
    Dopa=6387366412
    return action


def speak(something):
    engine.say(something)
    engine.runAndWait()


def wishes():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning"+ master + "Hope you had peacefull dreams.")
    elif hour>=12 and hour<=16:
        speak("Good   afternoon" + master + "Hope you had fresh morning today.")
    elif hour>16 and hour<=22:
        speak("Good evening" + master + "Hope you had great day today.")
    elif hour<22 and hour<=24:
        speak("Good night" + master + "Hope you had great day today.")



#I am writing main program from here
speak(" Hello.....  Initialising Jarvis. Please Wait........")

wishes()

listentome()
speak("Tell me" + master + "How are you feeling today?")

action=listentome()
if 'good' in action:
 speak("Great!! ")

elif 'bored' in action:
    speak("Can I play music for you"+master)
    action=listentome()
    if 'yes' in action:
        file_dir="C:\\Users\\ansh6\\Music"
        file=os.listdir(file_dir)
        os.startfile(os.path.join(file_dir,file[1]))
    else:
        pass

speak("How may I help you?" + master)

action = listentome()
chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"

for i in range(100):
 if 'wikipedia' in action:
    action = action.replace("according to Wikipedia", "")
    action = action.replace("Jarvis", "")
    speak(f"Searching on wikipedia for {action}\n")
    result = wikipedia.summary(action, sentences = 3)
    speak(result)
    

 elif 'youtube' in action:
    action = action.replace("open","")
    action = action.replace("YouTube","")
    action = action.replace("and","")
    action = action.replace("search","")
    action = action.replace("for","")
    action = action.replace("on","")
    action = action.replace("in","")
    action = action.replace("Jarvis","")
    action = action.replace("play","")

    pwk.playonyt(action)
    
 
 elif 'wish birthday' in action:
     action = action.replace("send message","")
     action = action.replace("to","")
     action = action.replace("birthday wish","")
     phonebook(action)
     number=action
     
     pwk.sendwhatmsg(f"+91{number}","Happy Birthday!!",23,59)

 elif 'open my pc' in action:
    speak("Can you please specify me in which drive do you wanna work?")
    action=listentome()
    if 'c' in action:
         os.startfile("C:")
    elif 'd' in action:
         os.startfile("D:")
    
    else: 
         pass
 elif 'open paint' in action:
     file_dir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
     file=os.listdir(file_dir)
     os.startfile(os.path.join(file_dir,file[2] ))

  
 elif 'mini project' in action:
     os.startfile("D:\\Mini project")

 elif 'google'  in action:
    
    action = action.replace("open","")
    action = action.replace("Google","")
    action = action.replace("and","")
    action = action.replace("search","")
    action = action.replace("for","")
    action = action.replace("Jarvis","")
    pwk.search(action)

 else:
     pass



 speak("Can I do something else for you?")
 action=listentome()
 
 if 'no' in action:
    break

speak("It was great helping you!! Hope to see you soon Sir.")











