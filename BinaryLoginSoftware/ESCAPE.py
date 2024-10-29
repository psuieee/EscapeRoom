#ESCAPE_ROOM WORKSHOP PSU IEEE FA24
#PYTHON GUI CODE 


import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import threading
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   #boost startup speed by hiding: 
                                                    #pygame 2.6.1 (SDL 2.28.4, Python 3.10.11)
                                                    #Hello from the pygame community. https://www.pygame.org/contribute.html
import pygame


def main():
    #initialize pygame mixer
    pygame.mixer.init()

    #app settings
    app = ttk.Window(themename='vapor')
    app.title("you can't escape")
    app.minsize(500,500)
    app.attributes('-topmost', True)
    app.attributes('-fullscreen', True)
    app.iconbitmap("eyeball.ico")

    #frames for each page
    Page1_frame = ttk.Frame(app)
    Page2_frame = ttk.Frame(app)
    Page3_frame = ttk.Frame(app)
    Page4_frame = ttk.Frame(app)
    Page5_frame = ttk.Frame(app)

    #Playaudio
    def play_audio():
        pygame.mixer.music.load('scream.mp3')
        pygame.mixer.music.play()

    #Show a frame
    def show_frame(frame):
        frame.tkraise()
        if frame == Page5_frame:
            #if frame ==5, play audio in new thread
            threading.Thread(target=play_audio, daemon=True).start()

    #Place all frames in same location
    for frame in (Page1_frame, Page2_frame, Page3_frame, Page4_frame, Page5_frame):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    #Page1_frame
    courier_font = ('Courier New', 26)
    label1 = ttk.Label(Page1_frame, text="\n\n\n\n\n\n\n\nPlease enter the access token to gain access to the app", font=courier_font)
    label1.pack(pady=20)
    password_entry = ttk.Entry(Page1_frame)
    password_entry.pack(pady=10)
    def check_password():
        if password_entry.get() == "cmpenis#1":  #INITIAL DIGISPARK PWD
            show_frame(Page2_frame)
        else:
            error_label = ttk.Label(Page1_frame, text="Incorrect password. Try again.", foreground='red')
            error_label.pack()
    submit_button = ttk.Button(Page1_frame, text="Submit", command=check_password, bootstyle = DANGER)
    submit_button.pack(pady=10)

    #Page2_frame
    binary_code = "\n\n\n\n\nTranslate binary to text and enter below:\n\n\t01001001 01000101 01000101 01000101\n\t01110011 01100001 01111001 01110011\n\t01001000 01001001\n\n(case-sensitive, no spaces)"  #"IEEEsaysHI" in binary
    label2 = ttk.Label(Page2_frame, text=binary_code, font=courier_font)
    label2.pack(pady=20)
    translation_entry = ttk.Entry(Page2_frame)
    translation_entry.pack(pady=10)
    def check_translation():
        if translation_entry.get() == "IEEEsaysHI":  #TRANSLATION
            show_frame(Page3_frame)
            app.attributes('-alpha', 0.8)
        else:
            error_label = ttk.Label(Page2_frame, text="Incorrect translation. Try again.", foreground='red')
            error_label.pack()
    submit_translation_button = ttk.Button(Page2_frame, text="Submit", command=check_translation, bootstyle = PRIMARY)
    submit_translation_button.pack(pady=10)
    stuck_button = ttk.Button(Page2_frame, text="Stuck?", command=lambda: show_frame(Page4_frame), bootstyle = SECONDARY)
    stuck_button.pack(pady=10)
    extra_button = ttk.Button(Page2_frame, text="Click here for more clues", command=lambda: show_frame(Page5_frame), bootstyle = DANGER)
    extra_button.pack(pady=10)

    #Page4_frame
    instructions = """\n\n\n\nTo convert binary to text:
\t- Each byte (8 bits) represents a character.
\t- First 3 bits represent either uppercase or lowercase.
\t- Last 5 bits represent the letter itself.

\tExamples:
\t  [8]    -> [3]  [5]
\t01100001 -> 011 00001 -> 'a'
\t01000001 -> 010 00001 -> 'A'
\t01100010 -> 011 00010 -> 'b'
\t01000010 -> 010 00010 -> 'B'
\tetc....
"""
    label4 = ttk.Label(Page4_frame, text=instructions, font=courier_font)
    label4.pack(pady=20)
    back_button = ttk.Button(Page4_frame, text="Back", command=lambda: show_frame(Page2_frame))
    back_button.pack(pady=10)

    #Page5
    pigOriginal = Image.open("pig.png")
    pig = pigOriginal.resize((1700, 1000), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(pig)
    label5 = ttk.Label(Page5_frame, image=photo)
    label5.pack(pady=10)
    back_button = ttk.Button(Page5_frame, text="Back", command=lambda: show_frame(Page2_frame), bootstyle = DANGER)
    back_button.pack(pady=10)

    #Page3_frame
    final_password = "\n\n\n\n\n\nTo unlock folder:\n\nSECRET_FOLDER_PWD = \"CursedByFentanyl\" "
    label3 = ttk.Label(Page3_frame, text=final_password, font=courier_font)
    label3.pack(pady=20)
    destroyButton = ttk.Button(Page3_frame, text="CLICK TO DESTROY APPLICATION", command=app.destroy, bootstyle = DANGER)
    destroyButton.pack(ipady=35, ipadx=50, pady=20)

    #Start w Page1_frame
    show_frame(Page1_frame)

    app.mainloop()

if __name__ == "__main__":
    main()
