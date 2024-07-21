# when you use this code first time you should install all libraries
# form setup file so first run setup.py 
# for automatically updating and installing all libraries


import pyttsx3 # for converting taxt to voies 
import speech_recognition as sr # for take a command
import datetime # for date and time
import os # fro open files and applications
from requests import get # your ip address
import webbrowser # for open website from web browser
import cv2 # for camera module install cv2
import wikipedia # for wikipedia article
import pywhatkit # for sent msg to whatsapp

engine = pyttsx3.init('sapi5') # initialize pyttsx3 engine
voices  = engine.getProperty('voices') 
engine.setProperty('voices',voices[0].id)

# this function for text generate voice output
def speak(audio):
    engine.say(audio)
    print (audio)
    engine.runAndWait()

# this function for voice input and generate text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait a moment while I listen...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("say that again please...")
        return "None"
    
    return query

#this function for wishes
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Jarvis. Please tell me how can I help you today.")

if __name__ == '__main__':
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query :# like open any application and file system
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query :
            os.system("start cmd")

        elif "open youtube" in query : # like open any website form webbrowser module
            webbrowser.open("HTTPS://youtube.com")
            speak("opening youtube!")

        elif "open camera" in query : # open camera module 
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50) 
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "pley music" in query : # play music from your file system
            music_dir = '<Choosh Your Music file path>'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("playing music!")

        # elif " IP address" in query :
        #     ip = get('https://api.ipify.org').text
        #     speak(f"Your IP address is {ip}")
        
        elif "wikipedia" in query : # search for wikipedia say "<your inpute> according to wikipedia"
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print (results)

        elif "open google"  in query :
            speak("sir, what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query : # for this use you are login in whatsapp web
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            speak("sir, please enter the recipient's mobile number:")
            Mobile_no = input("Enter mobile number:")
            speak("sir, please say your message.")
            msg = takecommand().lower()
            print(f"Sending message to {Mobile_no} at {hour}:{minute+2}")  # to send message 2 minutes after current time. Because whatsapp api has 60 seconds interval.
            pywhatkit.sendwhatmsg(Mobile_no,msg,hour,minute+2,59)  
            speak("message sent!")
            print ("message sent!")  

        elif "shut down" or "shutdown"in query:
            speak("Sure, Jarvis will be shutting down. have a nice day sir.")
            break

        else:
            speak("I'm not able to perform this task at the moment. Please try again.")
