import speech_recognition as sr  #library recognize speech
import os 
import pyttsx3
import webbrowser
import openai
import datetime
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
def takeCommandFromUser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Sorry!"


while True:
    if __name__ == '__main__':
        speak("Jarvis AI")
        print("Listening...")
        query = takeCommandFromUser()
        sites = [["youtube", "https://www.youtube.com"], ["Iskcon", "https://www.iskcon.org"],
                 ["Wikipedia", "https://www.wikipedia.com"], ["Spiritual Books", "https://vedabase.io/"]]
        # speak(query)
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} Dear Devotee...")
                webbrowser.open(site[1])
        if "open music" in query:
            # musicPath = "C:\\Users\\harsh\\Downloads\\summer-walk-152722.mp3"
            musicPath = "C:/Users/harsh/Desktop/summer-walk-152722.mp3"
            os.system(f"start {musicPath}")
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strfTime}")
        if "open pictures".lower() in query.lower():
            os.system(f"start notepad")
