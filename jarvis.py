import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import random
import os
import subprocess

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[28].id)
engine.setProperty('rate',140)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Afternoon!')
    elif hour >= 12 and hour < 18:
        speak('Good AFternoon!')
    else:
        speak('Good Evening!')
    
    speak("I am Jarvis Sir, how may I help you?")

def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f'You said: {query}')
    except Exception as e:
        print("Pleasy say again....")
        return 'None'
    
    return query

if __name__ == '__main__':
    greetMe()
    while True:
        q = takeCommand().lower()

        if 'about' in q:
            q = q.replace('about','').replace('tell me','')
            try:
                result = wikipedia.summary(q, sentences=2)
                print(result)
                speak(result)

            except Exception as e:
                speak('No information found!')

        elif 'open youtube' in q:
            webbrowser.open('https://youtube.com')
        elif 'open google' in q:
            webbrowser.open('https://google.com')
        elif 'open github' in q:
            webbrowser.open('https://github.com')

        elif 'play music' in q:
            music_dir = '/home/sandip/Music/Bhajan'
            songs = os.listdir(music_dir)

            random_song = random.choice(songs)

            song_to_play = os.path.join(music_dir, random_song)

            subprocess.Popen(['xdg-open', song_to_play])
        elif 'stop music' in q:
            subprocess.call(['pkill','totem'])

        elif 'the time' in q:
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            speak(f'Sir, the time is: {hour} point {minute}')

        
            
