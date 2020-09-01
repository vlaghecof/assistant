import datetime

import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
import datetime
import psutil
import platform
import webbrowser
from actions import sleep,conversation
import subprocess

from Dispatcher import getActions
from Audio import AudioManager
from actions import System

# ToDO Clean main , add a module for for conversation to be active only partially ,
#  think about the wake word
#  create and open a project ,


def system_status():
    os, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    battery_at= psutil.sensors_battery()

    response = "I am currently running on %s version %s. \n" % (os, version)
    response += "This system is named %s and has %s CPU cores. \n" \
        % (name, cores)
    response += "Current CPU utilization is %s percent. \n" % cpu_percent
    response += "Current memory utilization is %s percent. \n" % memory_percent
    response += "Current disk utilization is %s percent. \n" % disk_percent
    response += "Current Battery  utilization is  at %s percent. \n" %str(battery_at.percent)
    if battery_at.power_plugged:
         response += "Currently the device is  plugged in  \n"
    else:
        response += "Currently the device is not plugged in  \n"

    return response


num=0
def speak(output):
    global num
    num += 1
    print("PerSon : ", output)
    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)




def speaks(text):
    engine.say(text)
    engine.runAndWait()







def wishMe():
    hour = int(datetime.datetime.now().hour)
    say=""
    if hour >= 0 and hour < 12:
        say+="     Good Morning Sir ! "

    elif hour >= 12 and hour < 18:
        say+="     Good Afternoon Sir ! "

    else:
        say+="    Good Evening Sir ! "

    assname = ("     Jarvis 1 point o ")
    say+="   I am your Assistant"
    speak(say)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

# speak("Nice to meet you")
# wishMe()
# takeCommand()

# speak("Nice to meet you , good morning sir i am your assistant , Jarvis 1.0")


# speak("I am online Sir , call me if i can help you ")
# note("I can say here almos enything")
# speak(system_status())

WAKE = ["sexy","hey sexy","wake up","start"]
NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]


sentace= "this is a sentace , are you interested "

table={

     print:["make a note", "write this down", "remember this", "type this"]
}



# speak(conversation.determineCommand("asfasfd"))

# text = myCommand()


while True==False:

    memory_percent = psutil.virtual_memory()[2]
    print(memory_percent)
    if(memory_percent>50) :
        speak(f'Sir , The memory utilization surpasses 50% beeing at a {memory_percent}' )

    text = AudioManager.myCommand()
    for phrase in WAKE:
      if phrase in text:
        active=True
        speak("I am ready")
        while active==True:
            text =AudioManager.myCommand()
            if "status" in text:
                info=system_status()
                speak(info)

            if "initialise "in text:
                webbrowser.open("https://www.youtube.com/watch?v=23EfsN7vEOA&t=10s")
            if "sleep" in text:
               speak(sleep.go_to_sleep())
               active=False
            if"turn off" in text or "over" in text :
                speak("It was a pleasure serving you ")
                exit()

            for phrase in NOTE_STRS:
                if phrase in text:
                    speak("What would you like me to write down? ")
                    write_down = AudioManager.myCommand()
                    note(write_down)
                    speak("I've made a note of that.")



# wishMe()


try :
    getActions(AudioManager.myCommand())
    getActions(AudioManager.myCommand())
except:
    speak("Sorry sir i did not get that ")






