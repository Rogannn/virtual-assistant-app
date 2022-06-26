from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import tkinter as tk

window = tk.Tk()

text_box = tk.Text(window, height=10)
# label = tk.Label(
#     text="Be sure to speak loud enough if it cannot hear you.",
#     fg="black",
#     bg="white"
# )

# bot image 1873 x 1870
# background image 5667 x 3750
raw_pic = Image.open("static/images/simplerobot.png")
resized = raw_pic.resize((89, 89), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(resized)
my_label = Label(window, image=my_img)

my_label.grid(row=0, column=0)
text_box.grid(row=0, column=1, sticky=tk.EW)
scrollbar = ttk.Scrollbar(window, orient='vertical', command=text_box.yview)
scrollbar.grid(row=0, column=2, sticky=tk.NS)
text_box['yscrollcommand'] = scrollbar.set
