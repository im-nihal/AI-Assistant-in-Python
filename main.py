import os
import pyttsx3#librabry for text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit #librabry for youtube

engine = pyttsx3.init('espeak') #for windows use 'sapi5' and voice id 0(M) or 1(F)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)
engine.setProperty("rate", 170) #voice speed


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    #upon starting it will greet you.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("How may I help you?")


def tellDay():
    #This function is for telling the day of the week
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def command():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") #prints listening so that we'll know its listening
        r.pause_threshold = 1
        r.energy_threshold = 300
        voice = r.listen(source, 0, 5) #for 0 to 5 sec it will take the query

    try:
        print("Recognizing...") #prints recognizing so that we'll know its processing
        query = r.recognize_google(voice, language='en-in') #you can change language accordingly
        print(f"You said: {query}\n")

    except Exception as e:
        speak("Pardon me master, I don't get you. Could you please repeat?") #when it does not understand the query
        return "None"

    return query


if __name__ == "__main__":
    greet()
    while True:
        query = command().lower() #most queries match to lower case.

        # Logic for executing tasks based on queries
        if 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            continue

        elif 'what day' in query:
            tellDay()
            continue

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master, the time is {strTime}")
            continue

        elif 'who are you' in query:
            speak("I am Alfred. Your desktop assistant.")

        elif 'play music' in query:
            os.system("rhythmbox-client --play") #linux command for playing music

        elif 'stop' in query:
            speak("very well master. Should you need my help, I am at your service.")
            exit()

        elif 'youtube' in query:
            query = query.replace("youtube", "")
            print('playing' + query + 'On Youtube')
            speak('playing' + query + 'On Youtube')
            pywhatkit.playonyt(query)

        elif 'recite quran' in query: #plays quran recitations videos from youtube
            speak("Excellent choice Master.")
            webbrowser.open("https://www.youtube.com/watch?v=UDvh63xHVa0&list=PLoqNzfHlA__knCeUoKUHjQfZpUL6mj64w")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)  # prints & speaks 4 sentences
            speak("According to Wikipedia")
            print(results)
            speak(results)
