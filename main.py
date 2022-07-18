
import pyttsx3          # Used for speak functon
import datetime         # To getdate and time
import speech_recognition as sr       # used in function to convert audio in query
import webbrowser       # To search .com in webbrowser
import wikipedia        # To search n wikipedia
import os               # Used to operate with system
import smtplib          # Module used for sending mai l 
from requests import get

#pyaudio module must be installed in pc

engine = pyttsx3.init('sapi5')           #To speak
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)  #voices[o].id mean jo voices present voices variable me, 0th voice set kr do

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    #It will tell time in 24hrs format(only hours 0-24)

    if hour>=0 and hour<12:
        speak("Good Morning !")

    if hour>=12 and hour<18:    
        speak("Good Afternoon !")

    else:
        speak("Good Evening")

    speak("I am Desktop Assistant (Alex). Please tell me how i can help you")

def takeCommand():
    '''
    It takes Input from user using microphone
    and return query(Query means converting input into text string).
    '''

    r = sr.Recognizer()                 #To recognise sound internet is must.
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1     #mean input dete time (1 sec) ruke to recognizer bnd nhi hoga and pressing (ctrl) we can check and impememt more functions
        audio = r.listen(source)

    try :
        print("Recognizng....")
        query = r.recognize_google(audio,language="en-in")    #Different recogrnizers are available.But google Recognizer is best
        print(f'User said {query}\n')

    except Exception as e:
        print('Say that again please...')
        return 'none'

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.@gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('ajayanand2149@gmail.com','Funbookfunbook')
    server.sendmail("techstaan7@gmail.com",to,content)
    server.close()



if __name__ == '__main__':
    wishMe()

while True:
    if 1:
        query = takeCommand().lower()

        if 'who are you' in query:
            speak("My name is Alex. I am personal Desktop Assistant")

        if 'open google' in query:
            speak("Sir, What should i search on google")
            cm= takeCommand().lower()
            webbrowser.open(f"{cm}")

        if 'open youtube' in query:
            webbrowser.open('youtube.com')

        if 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        if 'play music' in query:
            path = "D:\\BACKGROUND MUSIC"
            songs = os.listdir(path)
            os.startfile(os.path.join(path,songs[0]))

        if 'open facebook' in query:
            webbrowser.open("facebook.com")
 


        if 'open code' in query:
            os.startfile(r"C:\\Users\\AJAY ANAND\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        if 'open calculator' in query:
            os.startfile(r"C:\\Windows\\system32\\calc.exe")

        if 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(time)

        if 'local disk d' in query:
            os.startfile("D:\\")

        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("acording to wikipedia")
            speak(results)
            print(results)

        if 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}") 

        if 'open chrome' in query:
            os.startfile(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        if 'open command prompt' in query:
            os.system("start CMD")    

        if 'open local disk p' in query  :
            os.startfile("P:\\")

        if 'local disk a' in query  :
            os.startfile("A:\\")

        if 'email to ajay' in query:
           try:
               print("Speak content to sent")
               content = "Emal done"
               to = 'ajy57@gmail.com'

               sendEmail(to,content)
               print('Email has been sent !')
               speak('Email has been sent !')

           except Exception as e:
               print (e)
               print('Email not sent')
               speak('Email not sent')
