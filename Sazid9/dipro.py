hhfrom datetime import datetime
from email.mime import audio
import speech_recognition as sr
import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak('Good morning')

    elif hour >= 12 and hour < 18 :
        speak('good evening!')
    speak('sir i am sara your personial assistent gg how can i help you')    

def take_comand(): 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print('Recognizing..')
        query = r.recognize_google(audio , language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        print(e)

        print('say that again please...')
        return 'None'
    return query

if __name__ == '__main__':
    # speak('dipro is a good boy')
    wishme()
    take_comand()