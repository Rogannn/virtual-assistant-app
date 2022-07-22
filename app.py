from neuralintents import GenericAssistant
from threading import *
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from datetime import datetime
import pyttsx3 as tts
import datetime
import speech_recognition as sr
import threading

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
# voices[0] = male, voices[1] = female
speaker.setProperty('voice', voices[0].id)

window = Tk()

window_height = 670
window_width = 740
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

ex = (screen_width / 2) - (window_width / 2)
ey = (screen_height / 2) - (window_height / 2)

window.iconbitmap("static/images/logo.ico")
window.title("VirtualAssistant")
window.geometry(f"{window_width}x{window_height}+{int(ex)}+{int(ey)}")
window.configure(bg="#D9BB8E")

show_categories = False
show_category_data = False

query_btn_list = []
spoken_list = []

CLEAR_BTN_RELY = 0.22
CLEAR_BTN_RELX = 0.6
REPEAT_BTN_RELY = 0.17
REPEAT_BTN_RELX = 0.6

def hello():
    response = "Greetings, what would you like to ask?"
    aiResponse(response)


def current_date():
    d = datetime.today().strftime('%B %d,%Y')
    response = "Today is " + d
    aiResponse(response)


def howisit():
    response = "I'm good, thank you for asking"
    aiResponse(response)


def timeCheck():
    time = datetime.datetime.now().strftime('%I:%M %p')
    response = "The current time is " + time
    aiResponse(response)


def gratitude():
    response = "Your welcome"
    aiResponse(response)


def courses():
    aiResponse("AVAILABLE COURSES IN DHVSU PORAC CAMPUS. "
               "Bachelor of Elementary Education Major in General Education. "
               "Bachelor of Science in Business Administration Major in Marketing. "
               "Bachelor of Science in Information Technology. "
               "Bachelor of Science in Social Work")


def register():
    aiResponse(
        "To register, go to the registrar of the school. You can then ask more questions to the person assigned there.")


def enrollment():
    aiResponse(
        "To enroll, you can go to the Administrative room. You can then ask the person in charge for further inquiries.")


def teachersToAsk():
    aiResponse(
        "You can go to the Faculty room of the school to see the teachers or you can go to their own office.")


def exitApp():
    response = "Have a nice day!"
    aiResponse(response)


mappings = {
    "to_register": register,
    "to_enroll": enrollment,
    "ask_teacher": teachersToAsk,
    "greeting": hello,
    "gratitude": gratitude,
    "howisit": howisit,
    "time_check": timeCheck,
    "exit": exitApp,
    "available_courses": courses,
    "current_date": current_date
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.load_model()

stop_event = threading.Event()


def word_splitter(words):
    word_limit = 10
    split_words = words.split()
    new_text = ""
    word_count = 0
    for word in split_words:
        new_text += word + " "
        word_count += 1
        if word_count > word_limit or "." in word:
            new_text += "\n"
            word_count = 0
    return new_text


def toggle_categories():
    global show_categories
    global show_category_data
    if show_categories:
        show_category_data = False
        show_categories = False
        hide_data()
    else:
        show_categories = True
        category1.place(anchor="n", relx=0.30, rely=0.54)
        category2.place(anchor="n", relx=0.5, rely=0.54)
        category3.place(anchor="n", relx=0.70, rely=0.54)


def show_category1_data():
    cat2query1.grid_remove()
    cat2query2.grid_remove()
    cat3query1.grid_remove()
    cat3query2.grid_remove()
    category_lbl2.place_forget()
    category_lbl2.place_forget()
    category_lbl3.place_forget()
    category_lbl3.place_forget()
    main_frame.place(relx=0.20, rely=0.63, width=450, height=130)
    category_lbl1.place(anchor="w", relx=0.20, rely=0.61)
    cat1query1.grid(row=0, column=0, sticky="w")
    cat1query2.grid(row=1, column=0, sticky="w")


def show_category2_data():
    cat1query1.grid_remove()
    cat1query2.grid_remove()
    cat3query1.grid_remove()
    cat3query2.grid_remove()
    category_lbl1.place_forget()
    category_lbl1.place_forget()
    category_lbl3.place_forget()
    category_lbl3.place_forget()
    main_frame.place(relx=0.20, rely=0.63, width=450, height=130)
    category_lbl2.place(anchor="w", relx=0.20, rely=0.61)
    cat2query1.grid(row=0, column=0, sticky="w")
    cat2query2.grid(row=1, column=0, sticky="w")


def show_category3_data():
    cat1query1.grid_remove()
    cat1query2.grid_remove()
    cat2query1.grid_remove()
    cat2query2.grid_remove()
    category_lbl2.place_forget()
    category_lbl2.place_forget()
    category_lbl1.place_forget()
    category_lbl1.place_forget()
    main_frame.place(relx=0.20, rely=0.63, width=450, height=130)
    category_lbl3.place(anchor="w", relx=0.20, rely=0.61)
    cat3query1.grid(row=0, column=0, sticky="w")
    cat3query2.grid(row=1, column=0, sticky="w")


category1_img = PhotoImage(file=r"static/images/category_1.png")
category2_img = PhotoImage(file=r"static/images/category_2.png")
category3_img = PhotoImage(file=r"static/images/category_3.png")
category1 = Button(window,
                   image=category1_img,
                   borderwidth=0,
                   highlightthickness=0,
                   relief="flat",
                   cursor="hand2",
                   activebackground="#D9BB8E",
                   command=show_category1_data)
category2 = Button(window,
                   image=category2_img,
                   borderwidth=0,
                   highlightthickness=0,
                   relief="flat",
                   cursor="hand2",
                   activebackground="#D9BB8E",
                   command=show_category2_data)
category3 = Button(window,
                   image=category3_img,
                   borderwidth=0,
                   highlightthickness=0,
                   relief="flat",
                   cursor="hand2",
                   activebackground="#D9BB8E",
                   command=show_category3_data)

query_btn_img = PhotoImage(file=r"static/images/available_questions.png")
query_btn = Button(window,
                   image=query_btn_img,
                   borderwidth=0,
                   highlightthickness=0,
                   relief="flat",
                   cursor="hand2",
                   activebackground="#D9BB8E",
                   command=toggle_categories)
query_btn.place(anchor="n", relx=0.5, rely=0.45)
bot_speech = Label(window, text="",
                   bg="white",
                   fg="black",
                   padx=20,
                   pady=10)


def aiResponse(response):
    repeat_btn.place_forget()
    clear_btn.place_forget()
    for btn in query_btn_list:
        btn.config(state=DISABLED)

    text = word_splitter(response)

    bot_speech.config(text=text)
    bot_speech.place(anchor="n", relx=0.5, rely=0.33)
    bot_speech.configure(font=getFont)

    speaker.say(response)
    speaker.runAndWait()

    repeat_btn.place(anchor="n", relx=CLEAR_BTN_RELX, rely=REPEAT_BTN_RELY)
    clear_btn.place(anchor="n", relx=CLEAR_BTN_RELX, rely=CLEAR_BTN_RELY)
    for btn in query_btn_list:
        btn.config(state=NORMAL)


def user_speech_textbox(message):
    text_box.delete(0, END)
    text_box.insert(0, message)
    spoken_list.append(message)
    t2 = Thread(target=run, args=(message,))
    t2.start()


def threading():
    t1 = Thread(target=run, args=("hello",))
    t1.start()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_event.set()
        window.destroy()


def clear_lbl():
    bot_speech.config(text="Cleared!")
    clear_btn.place_forget()
    repeat_btn.place_forget()


def repeat_speech():
    try:
        li = len(spoken_list) - 1
        speech = spoken_list[li]
        print("Repeating: " + speech)
        t3 = Thread(target=run, args=(speech,))
        t3.start()
    except IndexError:
        t3 = Thread(target=run, args=("hello",))
        t3.start()


clear_raw_img = PhotoImage(file=r"static/images/clear.png")
clear_img = clear_raw_img.subsample(22, 22)
clear_btn = Button(window,
                   text="Clear",
                   image=clear_img,
                   borderwidth=0,
                   highlightthickness=0,
                   relief="flat",
                   cursor="hand2",
                   background="white",
                   foreground="black",
                   activebackground="#D9BB8E",
                   command=clear_lbl)

repeat_raw_img = PhotoImage(file=r"static/images/repeat.png")
repeat_img = repeat_raw_img.subsample(16, 16)
repeat_btn = Button(window,
                    image=repeat_img,
                    borderwidth=0,
                    highlightthickness=0,
                    relief="flat",
                    cursor="hand2",
                    activebackground="#D9BB8E",
                    command=repeat_speech)


def run(text):
    global recognizer
    assistant.request(text)
    while True:
        print("listening..")
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                message = message.lower()
            text_box.delete(0, END)
            text_box.insert(0, message)
            spoken_list.append(message)
            assistant.request(message)
            clear_btn.place_forget()
            clear_btn.place(anchor="n", relx=CLEAR_BTN_RELX, rely=CLEAR_BTN_RELY)
            repeat_btn.place_forget()
            repeat_btn.place(anchor="n", relx=CLEAR_BTN_RELX, rely=REPEAT_BTN_RELY)
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
        if stop_event.is_set():
            break


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


def hide_data():
    main_frame.place_forget()
    canvas.place_forget()
    frame.place_forget()
    category_lbl1.place_forget()
    category_lbl2.place_forget()
    category_lbl3.place_forget()
    cat1query1.grid_remove()
    cat1query2.grid_remove()
    cat2query1.grid_remove()
    cat2query2.grid_remove()
    cat3query1.grid_remove()
    cat3query2.grid_remove()
    category1.place_forget()
    category2.place_forget()
    category3.place_forget()


def scroll_event(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=450, height=120)


def _on_mousewheel_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


botimg = PhotoImage(file=r"static/images/vaicon.png")
bot = botimg.subsample(5, 5)

banner = PhotoImage(file=r"static/images/banner.png")
Label(window,
      image=banner,
      borderwidth=0,
      highlightthickness=0).place(anchor="n", relx=0.5, rely=0.01)

Label(window,
      image=bot,
      borderwidth=0,
      highlightthickness=0).place(anchor="n", relx=0.5, rely=0.17)

user_lbl = Label(window, text="You said:", bg="#D9BB8E")
user_lbl.place(anchor="n", relx=0.5, rely=0.83)
text_box = Entry(window, cursor="arrow")
text_box.place(anchor="n", width=300, height=30, relx=0.5, rely=0.87)

category_lbl1 = Label(window, text="Category 1:", bg="#D9BB8E")
category_lbl2 = Label(window, text="Category 2:", bg="#D9BB8E")
category_lbl3 = Label(window, text="Category 3:", bg="#D9BB8E")

# QUESTIONS BUTTONS CONTAINER
main_frame = Frame(window, relief=GROOVE, bd=1, bg="#E4765D", borderwidth=0)

canvas = Canvas(main_frame, bg="#E4765D", borderwidth=0, highlightthickness=0)
frame = Frame(canvas, bg="#E4765D")

query_vscroll = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=query_vscroll.set)
query_hscroll = Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=query_hscroll.set)

query_vscroll.pack(side="right", fill="y")
query_hscroll.pack(side="bottom", fill="x")

canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='w')
frame.bind("<Configure>", scroll_event)
frame.bind_all("<MouseWheel>", _on_mousewheel_scroll)

category1_list = ["What are the available courses in DHVSU Porac Campus?",
                  "Category 1 Question 2?"]
category2_list = ["Category 2 Question 1?",
                  "Category 2 Question 2?"]
category3_list = ["Category 3 Question 1?",
                  "Category 3 Question 2?"]

cat1query1 = HoverButton(frame,
                         text=category1_list[0],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category1_list[0]))
query_btn_list.append(cat1query1)
cat1query2 = HoverButton(frame,
                         text=category1_list[1],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category1_list[1]))
query_btn_list.append(cat1query2)
cat2query1 = HoverButton(frame,
                         text=category2_list[0],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category2_list[0]))
query_btn_list.append(cat2query1)
cat2query2 = HoverButton(frame,
                         text=category2_list[1],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category2_list[1]))
query_btn_list.append(cat2query2)
cat3query1 = HoverButton(frame,
                         text=category3_list[0],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category3_list[0]))
query_btn_list.append(cat3query1)
cat3query2 = HoverButton(frame,
                         text=category3_list[1],
                         font=("Bahnschrift SemiBold SemiConden", 12),
                         relief="flat",
                         bg="#E4765D",
                         activebackground="#de593b",
                         activeforeground="white",
                         command=lambda: user_speech_textbox(category3_list[1]))
query_btn_list.append(cat3query2)

# CONFIGURE FONTS
getFont = Font(family="Bahnschrift SemiBold SemiConden", size=12)
query_btn.configure(font=getFont)
category1.configure(font=getFont)
category2.configure(font=getFont)
category3.configure(font=getFont)
user_lbl.configure(font=getFont)
text_box.configure(font=getFont)
category_lbl1.configure(font=getFont)
category_lbl2.configure(font=getFont)
category_lbl3.configure(font=getFont)
bot_speech.configure(font=getFont)

threading()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
