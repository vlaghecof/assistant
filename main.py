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

import subprocess

from Dispatcher import getActions
from Audio import AudioManager
from actions import System
import settings

# ToDO Clean main , add a module for for conversation to be active only partially ,
#  think about the wake word
#  create and open a project ,



def wishMe():
    hour = int(datetime.datetime.now().hour)
    say=""
    if hour >= 0 and hour < 12:
        say+="     Good Morning Sir ! "

    elif hour >= 12 and hour < 18:
        say+="     Good Afternoon Sir ! "

    else:
        say+="    Good Evening Sir ! "

    say+="   I am your Assistant , Now Systems are online , whit what can i help you"

    AudioManager.speak(say)



wishMe()


while  settings.online:
 try :

    getActions(AudioManager.myCommand())

 except:
    AudioManager.speak("Sorry sir i did not get that ")






