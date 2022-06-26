from neuralintents import GenericAssistant
from assistant import recognizer, speaker, mappings
from widgets import window, text_box, INSERT

from threading import *
from tkinter import Label, PhotoImage, Canvas, messagebox, END

import speech_recognition as sr

recognizer = sr.Recognizer()


assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.load_model()


def threading():
    global stop_threads
    stop_threads = False
    t1 = Thread(target=run, args=(lambda: stop_threads, ))
    t1.start()
    if stop_threads:
        t1.join()
        print('thread killed')


def run(stop):
    initMessage = "Greetings, I am your virtual assistant. What can I do for you?"
    global recognizer
    aiSaid = text_box.insert(INSERT, initMessage + "  \n")
    speaker.say(initMessage)
    speaker.runAndWait()
    while True:
        print("listening..")
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                message = message.lower()

            print("You said: " + message)
            youSaid = text_box.insert(INSERT, "You said: " + message + "\n")
            assistant.request(message)
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
        if stop():
            break


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        global stop_threads
        stop_threads = True


threading()


window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
# my_label.pack(pady=20)
# label.pack()
# text_box.pack()

window.iconbitmap("static/images/simplerobot.ico")
window.title("VirtualAssistant")
window.geometry("800x500")
window.resizable(False, False)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
