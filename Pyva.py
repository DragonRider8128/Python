import datetime
import webbrowser
import wikipedia
import pyttsx3

#Speaking function
def speak(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

#Introduction
print("Hello, I am Pyva - Python Virtual Assistant. I can search the web, get Wikipedia articles, tell you the date and say things aloud for you. Here are my commands:")
speak("Hello, I am Pyva - Python Virtual Assistant. I can search the web, get Wikipedia articles, tell you the date and say things aloud for you. Here are my commands:")
print("\nDate\nWikipedia\nWeb\nSpeak\n")

#Handle input
while True:
    #Ask for input and check if it is valid
    choice = input("\nWhat do you want me to do? ")
    while choice.upper() not in ["DATE","WIKIPEDIA","WEB","SPEAK"]:
        speak("Sorry, I didn't get that.")
        choice = input("Sorry, I didn't get that. ")

    #Do task instructed by user
    if choice.upper() == "WIKIPEDIA":
        speak("What do you want to find out? ")
        topic = input("What do you want to find out? ")
        try:
            summary = wikipedia.summary(topic)
            print("\n"+summary)
            speak(summary)
        except:
            print("Sorry, your query does not match any results.")
            speak("Sorry, your query does not match any results.")
    elif choice.upper() == "WEB":
        speak("What do you want to search?")
        search = input("What do you want to search? ")
        webbrowser.open("https://google.co.uk/search?q=" + str(search))

    elif choice.upper() == "DATE":
        now = datetime.date.today()
        print(now)
        speak("Today is the " + str(now))
    else:
        speak("What do you want me to say?")
        user_text = input("What do you want me to say? ")
        speak(user_text)
