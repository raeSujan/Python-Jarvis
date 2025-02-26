import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Mornning")
    
    elif hour >=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello I am a voice assistant How can I help you ")


def takeCommand():

    r = sr.Recognizer()    
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said :{query} \n ")

    except Exception as e:       
        print ("Say again please...")
        return "None"
    return query
    
if __name__=="__main__":
    greetMe()

    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedis....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            print (results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open messenger' in query:
            webbrowser.open("messenger.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open deep seek' in query:
            webbrowser.open("deepseek.com")

        elif 'open gpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

            