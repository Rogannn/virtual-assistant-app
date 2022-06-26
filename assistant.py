from widgets import text_box, INSERT, END, window
from webbrowser import open

import speech_recognition as sr
import pyttsx3 as tts
import random
import datetime
import pywhatkit
import wikipedia

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
# voices[0] = male, voices[1] = female
speaker.setProperty('voice', voices[0].id)

# todo_list = ['Go shopping', 'Clean room', 'Record video']


def hello():
    list = [
        "Hello, what can I do for you?",
        "Greetings, what can I do for you?",
        "Hi, what can I do for you?"
    ]
    chosen_statement = random.choice(list)
    aiResponse(chosen_statement)


def howisit():
    list = [
        "I'm fine, thank you.",
        "I'm good, thank you for asking."
    ]
    chosen_statement = random.choice(list)
    aiResponse(chosen_statement)


def playYt():
    global recognizer
    # ask what to play on youtube
    aiResponse("What do you want to play on youtube?")

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                # get user message
                audio = recognizer.listen(mic)
                message = recognizer.recognize_google(audio)
                message = message.lower()

                # start to open youtube and play the video
                response = "Playing " + message
                pywhatkit.playonyt(message)
                aiResponse(response)
                done = True
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            aiResponse("Sorry, I did not understand you! Please try again")


def timeCheck():
    time = datetime.datetime.now().strftime('%I:%M %p')
    response = "The current time is " + time
    aiResponse(response)


def searchWiki():
    global recognizer
    # ask what to search
    aiResponse("What do you want to search in wikipedia?")

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                # get user message
                audio = recognizer.listen(mic)
                message = recognizer.recognize_google(audio)
                message = message.lower()

                # start to open youtube and play the video
                response = "Searching and information about " + message
                aiResponse(response)
                # get 3 line only of information
                result = wikipedia.summary(message, 3)
                aiResponse(result)
                done = True
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            aiResponse("Sorry, I did not understand you! Please try again")


def gratitude():
    list = [
        "Your welcome.",
        "No problem."
    ]
    chosen_statement = random.choice(list)
    aiResponse(chosen_statement)


def register():
    aiResponse("To register, go to the registrar of the school. You can then ask more questions to the person assigned there.")


def enrollment():
    aiResponse("To enroll, you can go to the Administrative room. You can then ask the person in charge for further inquiries.")


def teachersToAsk():
    aiResponse(
        "You can go to the Faculty room of the school to see the teachers or you can go to their own office.")


def lookForLocation():
    global recognizer
    aiResponse("What do you want to find in the google maps?")
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                # get user message
                audio = recognizer.listen(mic)
                message = recognizer.recognize_google(audio)
                message = message.lower()

                # start to open youtube and play the video
                response = "Starting the search of " + message + " through google maps."
                aiResponse(response)
                # get 3 line only of information
                open("http://www.google.com/maps/place/" + message)
                done = True
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            aiResponse("Sorry, I did not understand you! Please try again")


def exitApp():
    list = ["Good bye!",
            "See you soon!",
            "Have a nice day!"
            ]
    chosen_statement = random.choice(list)
    aiResponse(chosen_statement)


def aiResponse(response):
    aiSaid = text_box.insert(INSERT, response + "\n")
    speaker.say(response)
    speaker.runAndWait()


mappings = {
    "look_for_location": lookForLocation,
    "to_register": register,
    "to_enroll": enrollment,
    "ask_teacher": teachersToAsk,
    "greeting": hello,
    "gratitude": gratitude,
    "howisit": howisit,
    "play_yt": playYt,
    "time_check": timeCheck,
    "search_wiki": searchWiki,
    "exit": exitApp
}
