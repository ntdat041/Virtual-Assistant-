import speech_recognition
import pyttsx3
import datetime
import webbrowser
import requests
import ctypes
import time
from tkinter import *
import threading

# Friday setting up to say
friday = pyttsx3.init()
friday_hearing = speech_recognition.Recognizer()
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
main = Tk()
main.resizable(width=False, height=False)
main.configure(width=530, height=550, bg=BG_COLOR)
main.title("Friday")
head_label = Label(main, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)
line = Label(main, width=510, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)
def speak(audio):
    friday.setProperty('rate', 180)
    friday.say(audio)
    friday.setProperty('rate', 200)
    friday.runAndWait()


def write_bot(str):
    msgs.insert(END, "Bot : " + str)
    speak(str)
    textF.delete(0, END)
    msgs.yview(END)


def write_boss(str):
    textF.delete(0, END)
    textF.insert(0, str)
    msgs.insert(END, "You : " + str.capitalize())


def command():
    with speech_recognition.Microphone() as mic:
        audio = friday_hearing.record(mic, duration=5)
    try:
        voice_boss = friday_hearing.recognize_google(audio, language='en')
        write_boss(voice_boss)
        a = voice_boss.lower()
        search(a)
        conversation(a)
        print(voice_boss)
    except speech_recognition.UnknownValueError:
        voice_boss=""
        write_bot("I didn't get that. Could you try again")
        print("...")
    return voice_boss


def browser(link):
    url = f"{link}"
    webbrowser.get().open(url)


def open_friday():
    hour = datetime.datetime.now().hour
    if 5 <= hour <= 10:
        hello = "Good morning, Boss. How can i help you"
    elif 11 <= hour <= 12:
        hello = "Good noon, Boss. How can i help you"
    elif 13 <= hour <= 18:
        hello = "Good afternoon, Boss. How can i help you"
    elif 19 <= hour <= 21:
        hello = "Good evening, Boss. How can i help you"
    else:
        hello = "Good night, Boss. How can i help you"
    write_bot(hello)


def search(str):
    if "google" in str:
        value = "What should i search Boss"
        write_bot(value)
        keyword = command().lower()
        write_boss(keyword)
        url = f"https://www.google.com/search?q={keyword}"
        webbrowser.get().open(url)
        value_01 = f'Here is your {keyword} on google chrome'
        write_bot(value_01)
    elif "youtube" in str:
        value = "What should i search Boss"
        write_bot(value)
        keyword = command().lower()
        write_boss(keyword)
        url = f"https://www.youtube.com/search?q={keyword}"
        webbrowser.get().open(url)
        value_01 = f'Here is your {keyword} on youtube'
        write_bot(value_01)
    elif "open facebook" in str:
        value = "Facebook is opening"
        write_bot(value)
        browser('https://www.facebook.com/')
    elif "music" in str:
        value = "Opening music on youtube"
        write_bot(value)
        browser('https://www.youtube.com/watch?v=leAlprToECY&list=PLfauYiLl00OpKReDoJbtrwKRIyOQiFH2a')
    elif "photo" in str:
        value = "Opening photo on google chrome"
        write_bot(value)
        browser('https://photos.google.com')
    elif "weather" in str:
        try:
            write_bot("Tell me about the city:")
            city = command()
            write_boss(city)
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            url = api_address + city
            json_data = requests.get(url).json()
            format_add_temp = json_data['main']['temp']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            weather_description = json_data['weather'][0]['description']  # drizzle
            visibility = json_data['visibility']
            # print(json_data)
            value_01 = f"The temperature of {city} city is {int(format_add_temp - 273)} degrees Celsius"
            value_02 = f"The humidity is {humidity} percent"
            value_03 = f"Wind speed is {wind} meter per second"
            value_04 = f"Visibility  is {int(visibility / 1000)} kilometer"
            value_05 = f"The weather is {weather_description}"
            write_bot(value_01)
            write_bot(value_02)
            write_bot(value_03)
            write_bot(value_04)
            write_bot(value_05)
            # print(int(format_add_temp - 273))
            # print(humidity)
            # print(wind)
            # print(int(visibility/1000))
            # print(weather_description)

        except:
            try:
                value_01 = "The city invalid, please try again"
                write_bot(value_01)
                value_02 = "Tell me about the city:"
                write_bot(value_02)
                city = command()
                api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                url = api_address + city
                json_data = requests.get(url).json()
                format_add_temp = json_data['main']['temp']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                weather_description = json_data['weather'][0]['description']  # drizzle
                visibility = json_data['visibility']
                # print(json_data)
                value_01 = f"The temperature of {city}  is {int(format_add_temp - 273)} degrees Celsius"
                value_02 = f"The humidity is {humidity} percent"
                value_03 = f"Wind speed is {wind} meter per second"
                value_04 = f"Visibility  is {int(visibility / 1000)} kilometer"
                value_05 = f"The weather is {weather_description}"
                write_bot(value_01)
                write_bot(value_02)
                write_bot(value_03)
                write_bot(value_04)
                write_bot(value_05)
            except:
                value = "The city invalid, try later"
                write_bot(value)


def time_():
    friday.setProperty('rate', 160)
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    value_time = f"The time is {Time}"
    friday.say(value_time)
    friday.setProperty('rate', 200)
    friday.runAndWait()
    print(Time)


def praise():
    friday.setProperty('rate', 160)
    friday.say("oh boss, thanks")
    friday.setProperty('rate', 200)
    friday.runAndWait()


def conversation(str):
    if "hello" in str:
        value = "Hello my boss, how can i help you"
        write_bot(value)
    elif 'how are you' in str:
        value = "I am fine, Thank you"
        write_bot(value)
    elif "time" in str:
        time_()
    elif "friday" in str:
        value = "I'm listening"
        write_bot(value)
    elif 'window' in str:
        value = "Locking the device"
        write_bot(value)
        ctypes.windll.user32.LockWorkStation()
    elif "don't listen" in str or "stop listening" in str:
        write_bot("For how much time you want to stop FRIDAY from listening commands")
        try:
            a = int(command())
            value = f'Time to slepp is {a} second'
            write_bot(value)
            time.sleep(a)
            value_01 = "Hello boss, I'm waiting for command"
            write_bot(value_01)
        except:
            try:
                value_02 = "Please try again"
                write_bot(value_02)
                a = int(command())
                value_03 = f'Time to slepp is {a} second'
                write_bot(value_03)
                time.sleep(a)
                value_04 = "Hello boss, I'm waiting for command"
                write_bot(value_04)
            except:
                value_05 = "Exception for set up the time, try later"
                write_bot(value_05)
    elif "take note" in str:
        value = "What should i write, sir"
        write_bot(value)
        note = command()
        file = open('jarvis.txt', 'w')
        value_01 = "Sir, should i include date and time"
        write_bot(value_01)
        snfm = command()
        print(snfm)
        if 'yes' in snfm or 'sure' in snfm:
            str_time = datetime.datetime.now().strftime("%I:%M:%p")
            file.write(str_time)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        value_02 = "Write success"
        write_bot(value_02)
    elif "open notebook" in str:
        value = "Showing Notes"
        write_bot(value)
        file = open('jarvis.txt', 'r')
        print(file.read())
        write_bot(file.read(6))
    elif "goodbye" in str:
        value = "Have a nice day boss, goodbye"
        write_bot(value)
        main.quit()
        main.destroy()


msgs = Listbox(main , width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,font=FONT)
sc = Scrollbar(msgs)
sc.place(relheight=1, relx=0.974)
sc.configure(command=msgs.yview)
msgs.place(relheight=0.745, relwidth=1, rely=0.08)
msgs.config(highlightbackground=BG_COLOR)
bottom_label = Label(main, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)
# creating text field
textF = Entry(main, font=("Verdana", 18))
#
# send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
#                              command=repeat_l)
# send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

# creating a function
# def enter_function(event):
#     send_button.invoke()
#
#
# # going to bind main window with enter key...
#
# main.bind('<Return>', enter_function)


def repeat_l():
    open_friday()
    while True:
        command()

t = threading.Thread(target=repeat_l)
t.setDaemon(True)
t.start()

main.mainloop()
