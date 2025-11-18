import speech_recognition as sr
import webbrowser
import pyttsx3
from AppOpener import open as open_app
import os
import musiclib

recognizer = sr.Recognizer()
ttsx= pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processcmnd(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        open_app("whatsapp")
    elif "play song" in c.lower():
        song= c.lower().replace("play song", "").strip()
        if song in musiclib.music:
            speak(f"Playing {song}")
            os.startfile(musiclib.music[song])
        else :
            speak("sorry, i dont have this song")



g= input("Your Good Name: ")
speak(f"Hi {g} , i am jarvis, how may i help you?")

while True:   
    print("RECOGNITIZING..")
    
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)
        text = recognizer.recognize_google(audio_data)
        print(f"Heard: {text}")
        
        if text.lower()=="jarvis":
            speak(f"yes {g}")
            
            with sr.Microphone() as source:
                print("Activated...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio_data)
            print(f"Command: {command}")
            speak(f"okk {g}")
            processcmnd(command)

    except sr.UnknownValueError:
        print("Clear bolo yaar")
    except sr.RequestError:
        print("Could not connect to Google API.")    

   