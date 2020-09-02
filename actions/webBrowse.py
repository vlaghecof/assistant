import subprocess
import webbrowser
import datetime
import requests
from Audio.AudioManager import speak

def note(text):
    speak("Im on it ")
    date = datetime.datetime.now()
    print(date)
    message=input("What would you like me to write down? ")
    title=input("Input the title or leave empty ")
    if title:
        file_name = title + "-note.txt"
    else:
         file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(message)

    subprocess.Popen(["notepad.exe", file_name])
    return "Your note Was Taken "

websites= { "youtube":"https://www.youtube.com/",
            "google":"https://www.google.com",
            "github":"https://github.com/vlaghecof",
            "git":"https://github.com/vlaghecof",
            "it":"https://github.com/vlaghecof",
            "whatsapp":"https://web.whatsapp.com/",
            "news":"https://stirioficiale.ro/informatii",
            "school":"https://websinu.utcluj.ro/",
            "intranet":"https://intranet.utcluj.ro/login",
            "facultate":"https://www.ac.utcluj.ro/",
            "yahoo":"https://mail.yahoo.com/d/folders/1" ,
            "gmail":"https://mail.google.com/mail/u/0/#inbox" ,
            "browser":"https://www.google.com"


}

def openWebsite(text):

    website_to_open = text[text.index('open') +5:].split(" ")[0].lower()
    print(website_to_open)
    url=f"https://www.google.com/search?q={website_to_open}"
    print(url)
    if website_to_open  in websites:
        webbrowser.open_new_tab(websites[website_to_open])
    else:
        webbrowser.open_new_tab(url)

    return "Here you go ,  enjoy Sir"

def serch(text):
    look_up = text[text.index('search') + 7:].lower().replace(" ","+")
    print(look_up)
    url = f"https://www.google.com/search?q={look_up}"
    print(url)

    webbrowser.open_new_tab(url)

    return "That is what i could find "


rover_url = 'https://api.nasa.gov/planetary/apod'

def get_mars_photo_url( text):
    params = { 'api_key': "X1cqGZoLRbyRojM4VpfzehmJDZtDLW7OdWKhnuD2"}
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['url']
    explanation=response_dictionary['explanation']
    noteText=""
    for char in explanation:
        if char=="." or char=="?":
         noteText+=".\n"
         continue
        else:
          noteText+=char
    webbrowser.open_new_tab(photos)
    print(noteText)

    return " Here you go "

