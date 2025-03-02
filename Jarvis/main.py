import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import webbrowser
import musics

def speak(msg):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(msg)
    engine.runAndWait()

def performTask(cmd):
    if 'open youtube' in cmd.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'open linkedin' in cmd.lower():
        webbrowser.open("https://www.linkedin.com")
    elif 'open instagram' in cmd.lower():
        webbrowser.open("https://www.instagram.com")
    elif cmd.lower().startswith("play"):
        song = " ".join(cmd.lower().split(" ")[1:])
        link = musics.music[song]
        print(link)
        webbrowser.open(link)

if __name__ == "__main__":
    r = sr.Recognizer()
    while True:
        print('Say Jarvis to command.')
        
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                
                if command.lower() == 'jarvis':
                    print("Now Command.")
                    print(f"You said: {command}")
                    speak("Yes, Sir.")
                    with sr.Microphone() as source:
                        audio  = r.listen(source)
                        command = r.recognize_google(audio)
                        print(f"You said: {command}")
                        performTask(command)
                
        except Exception as e:
            print(e)
