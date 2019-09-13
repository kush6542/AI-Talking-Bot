import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import requests as rq
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    name = "Kushagra Parashar "
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! " + name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! " + name)

    else:
        speak("Good Evening!  " +  name)

    speak("I am your personal Artificial intelligence assistant . Please tell me how may I help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #print (f"User said: {query}\n")
        print("Command  --->>  " + query + "\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #Adding credentials for sending the E-mail. Please
    server.login('kush.6542@gmail.com', 'googlepassword')
    server.sendmail('kush.6542@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'info' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'BAAD ME BADAL DENA YE WALA'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is " + strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\1506211\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kush.6542@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'exit' in query:
            try:
                speak("Bye Bye, See yaaa soon !")
                sys.exit()
            except Exception as e:
                print(e)

        elif 'fuck' in query:
            try:
                speak("Well,  go to hell  !! Huh ! I am going , bye!")
                sys.exit()
            except Exception as e:
                print(e)

        elif 'joke' in query:
            try:
                url = 'https://sv443.net/jokeapi/category/dark'
                data = rq.get(url)
                joke = data.json()
                print(joke)
                speak(joke["setup"])
                speak(joke["delivery"])

            except Exception as e:
                print(e)















