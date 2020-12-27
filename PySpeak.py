#Set up text to speech
import pyttsx3
speaker = pyttsx3.init()
repeat = True
#Introduction
print("Welcome to PySpeak, text to speech. Just enter some text and hear the computer read it aloud to you.")

while repeat == True:
    #Read text
    print("\n")
    text = input("Enter some text: ")
    speaker.say(text)
    print("READING...")
    speaker.runAndWait()
    #Ask to repeat
    print("\n")
    repeat = input("Do you want to run PySpeak again? y/n ")
    while repeat.upper() != "Y" and  repeat.upper() != "N":
        repeat = input("What?! I do not understand.")
    if repeat.upper() == "Y":
        repeat = True
    else:
        repeat = False
print("\n")
print("Sad to see you go! Bye! :(")
