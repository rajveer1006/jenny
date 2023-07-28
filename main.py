import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyttsx3
import PyPDF2
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 as ps

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jack' in command:
                command = command.replace('alexa', '')
                print(command)

    except: pass
    return command


def run_alexa():
    talk('hello,how can i assist you')
    command = take_command()
    print(command)
    if 'play ' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who is ' in command:
        person = command.replace('who is' ,  '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date =datetime.datetime.now().strptime('%D:%M:%Y')
        talk('Current date is')
    elif 'are you single' in command:
        talk('No I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am fine, how are you')
    elif 'listen your voice' in command:
        talk('thankyou, how can i help you ')
    elif 'help' in command:
        talk('yes sure, you just command me what you want')
    elif 'love' in command:
        talk('i love you too')
    elif 'what is your name' in command:
        talk('my name is jack')
    elif 'life partner' in command:
        talk('Jenny is love of my life')
    elif 'age' in command:
        talk('I am elder enough to get covid vaccine dose')
    elif 'search' in command:
        say = command.replace('search', '')
        talk('searching' + say)
        info = webbrowser.open('http://google.com/search?q='+command)
        print(info)
        talk(info)
    elif 'read' in command:
        talk('activating reading mode')
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        book = open('The Alchemist.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        info = PyPDF2.PdfFileReader('The Alchemist.pdf')
        print(info)
        print(pages)

        speaker = pyttsx3.init()
        for num in range(0, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif 'learning' in command:
        engine = ps.init()
        talk('activating learning mode')

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def speak(word):
            engine.say(word)
            engine.runAndWait()

        chatbot = ChatBot('ChatBot')
        trainer = ChatterBotCorpusTrainer(chatbot)

        trainer.train("chatterbot.corpus.english")

        # print(chatbot.get_response("english"))

        # while True:
        #   query = input(">>>")
        #  print(chatbot.get_response(Statement(text=query, search_text=query)))

        main = Tk()
        main.geometry("500x650")
        main.title("Learning Bot")
        img = PhotoImage(file="lb.png")
        photoL = Label(main, image=img)
        photoL.pack(pady=10)

        def learn():
            query = textF.get()
            answer = chatbot.get_response(query)
            msg.insert(END, "you : " + query)
            print(type(answer))
            msg.insert(END, "bot : " + str(answer))
            speak(answer)
            textF.delete(0, END)
            msg.yview(END)

        frame = Frame(main)

        sc = Scrollbar(frame)
        msg = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

        sc.pack(side=RIGHT, fill=Y)
        msg.pack(side=LEFT, fill=BOTH, pady=15)

        frame.pack()

        # creting text field
        textF = Entry(main, font=("Verdana", 20))
        textF.pack(fill=X, pady=10)

        btn = Button(main, text="Enter", font=("Verdena", 20), command=learn)
        btn.pack()

        def enter_function(event):
            btn.invoke()

        main.bind('<Return>', enter_function)
        main.mainloop()

while True:
    run_alexa()