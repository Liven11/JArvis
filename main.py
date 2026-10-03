# pip install SpeechRecognition
import speech_recognition as sr
# pip install pyttsx3
import pyttsx3
import datetime
# pip install wikipedia
import wikipedia
import webbrowser
import os
# pip install pillow
from PIL import ImageGrab
import time
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeScreenshot():
    image = ImageGrab.grab()
    image.show()


def wishAccordingToTime():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("How Can I Help You?")


def takeCommand():  # This command take input from user with microphone

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-In')
        print("You Said :", query)

    except Exception as e:
        # print(e)
        return "None"

    return query

def sendEmail(to, message):
    """Send mail using credentials from environment variables.

    Never hardcode the address or password here. Set them once per session:
        setx JARVIS_EMAIL "you@gmail.com"
        setx JARVIS_APP_PASSWORD "your-16-char-app-password"
    """
    email = os.environ.get('JARVIS_EMAIL')
    password = os.environ.get('JARVIS_APP_PASSWORD')
    if not email or not password:
        print("Email not configured. Set JARVIS_EMAIL and JARVIS_APP_PASSWORD.")
        return

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    try:
        server.login(email, password)
        server.sendmail(email, to, message)
    finally:
        server.quit()

if __name__ == '__main__':
    wishAccordingToTime()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening Youtube...")
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/')

        elif 'open vs code' in query:
            print("Opening Visual Studio Code...")
            speak("opening Visual Studio Code")
            webbrowser.open('code')

        elif 'open stack overflow' in query:
            print("opening StackOver Flow...")
            speak("opening stack over flow")
            webbrowser.open('https://stackoverflow.com/')

        elif 'open google' in query:
            print("opening Google...")
            speak("opening google")
            webbrowser.open('https://www.google.com/')

        elif 'who are you' in query:
            speak("I'am Jarvis , A Voice Assistant")

        elif "take screenshot" in query:
            speak("Taking screenshot")
            time.sleep(2)
            takeScreenshot()
            speak("screenshot taked")

        elif 'open chrome' in query:
            print("Opening Chrome Browser...")
            speak("opening chrome browser")
            chrome = os.path.join(
                os.environ.get('ProgramFiles', r'C:\Program Files'),
                'Google', 'Chrome', 'Application', 'chrome.exe')
            os.startfile(chrome)

        elif 'close chrome' in query:
            print("closing Chrome Browser...")
            speak("closing chrome browser")
            os.system('TASKKILL /F /IM chrome.exe')



        elif 'open pycharm' in query:
            print("opening PyCharm...")
            speak("opening pycharm")
            pycharm = os.path.join(
                os.environ.get('LOCALAPPDATA', ''),
                'JetBrains', 'Toolbox', 'apps', 'PyCharm')
            os.startfile(pycharm)

        elif 'go to sleep' in query:
            speak("Okay , I'am Going")
            sys.exit(0)

        elif "what time is" in query:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir , The Time Is {now}")

        elif "hello jarvis" in query:
            speak("Hello Sir")

        elif "how are you" in query:
            speak(
                "I'am Fine, but i don't know when my house is upgrade, when python 4 is release")

        elif "shut down" in query:
            print("Shuting Down Computer...")
            speak("Shuting Down Computer")
            os.system("shutdown /s /t 1")

        elif "play music list" in query:
            musicR = os.path.join('E:', 'music')
            songs = os.listdir(musicR)
            os.startfile(os.path.join(musicR, songs[0]))

        elif "send mail" in query:
            try:
                recipient = os.environ.get('JARVIS_CONTACT')
                if not recipient:
                    print("No contact set. Set JARVIS_CONTACT to a recipient address.")
                    continue
                speak("What Message Should I Send")
                message = takeCommand()
                sendEmail(recipient, message)
                speak("E-Mail Sent")
            except Exception as e:
                print(e)

        elif "you are mad" in query:
            speak("Sir , First Think That , Who made me")

    
