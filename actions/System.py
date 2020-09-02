import psutil
import platform
import os
import random
from Audio import AudioManager
import settings


def system_status(text):
    os, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    battery_at= psutil.sensors_battery()
    response=""

    if "full" in text:
        response = "I am currently running on %s version %s. \n" % (os, version)
        response += "This system is named %s and has %s CPU cores. \n"% (name, cores)

    response += "Current CPU utilization is %s percent. \n" % cpu_percent
    response += "Current memory utilization is %s percent. \n" % memory_percent
    response += "Current disk utilization is %s percent. \n" % disk_percent
    response += "Current Battery  utilization is  at %s percent. \n" %str(battery_at.percent)
    if battery_at.power_plugged:
        response += "Currently the device is  plugged in  \n"
    else:
        response += "Currently the device is not plugged in  \n"

    print(response)

    return response

def changeAudio(text):
    settings.audio=not settings.audio
    print(settings.audio)
    return "Changing imput mode"

def Mute(text):
    settings.speak=not settings.speak
    print(settings.speak)
    return "Changing output mode"


def creteProject(text):
    replies = [
        'Project Initialized',
        'Project Created'
    ]

    AudioManager.speak("Right away , please tell me the name")
    # name = AudioManager.myCommand()
    name=input("Name of the project , can also specify the type:")

    if "python" in text or "_py" in text or "py" in name:
        mode="py"
    else:
        if"java" in text or "_ja" in text or "ja" in name:
            mode="ja"

    name=name.split(" ")[0]




    if 'default' in text:
        gitFlag='l'
        if 'git'in text or "it" in text:
            gitFlag=''

        print(f"C:\\Users\\Vlad\\create.bat {name}_{mode} {gitFlag}")

        os.system(f"C:\\Users\\Vlad\\create.bat {name}_{mode} {gitFlag}")
    else:
       if "project" in text:

            _dir=settings.ProjectFolder+"\\"+name
            os.mkdir(_dir)
            os.chdir(_dir)
            os.system(f'echo "# {name}" > README.txt')
            os.system('start.')



    print(random.choice(replies))
    return (random.choice(replies))






