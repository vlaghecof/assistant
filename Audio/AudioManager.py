import os

import playsound
import speech_recognition as sr
from gtts import gTTS

import settings


num=0
def speak(output):
    global num
    if settings.speak==False:
        return print(output)
    num += 1
    print("PerSon : ", output)
    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)


def myCommand():
    "listens for commands"
    print('Ready...')
    if settings.audio==True:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Ready...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')


        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            command = ""
    else:
        command=input("Your command Sir:" )
    return command

