from sounder import Sounder
from actions import webBrowse,sleep,conversation,System
from Audio.AudioManager import speak
# ToDo moove the change input funciton and mute autside the dispatcher , its anoying to triger them by mistake
sounder = Sounder([[''],['mars', 'photo','space '],['search',"find","look up "],['open']
                    ,["make","note","write"],['sleep','pause'],['terminate','stop all',"over"],
                    ["full",'system','status'],['create','project','folder']
                  ])

sounder.set_filter(  {
      "what", "where", "which", "how", "when", "who",
      "is", "are", "makes", "made", "did", "do",
      "to", "the", "of", "from", "against", "and", "or",
      "you", "me", "we", "us", "your", "my", "mine", 'yours',
      "could", "would", "may", "might", "let", "possibly",
      'tell', "give", "told", "gave", "know", "knew",
      'a', 'am', 'an', 'i', 'like', 'has', 'have', 'need',
      'will', 'be', "this", 'that', "for","hey","baby", ",","please",
      "if","so",'kind','hello','there',"ok","friend","let's"
  })





activities=[conversation.determineCommand,webBrowse.get_mars_photo_url,webBrowse.serch,webBrowse.openWebsite,webBrowse.note,
            sleep.go_to_sleep,sleep.terminate,
            System.system_status,System.creteProject

            ]

def getActions(text):
    query=text
    keyWords = sounder.filter(query).get( 'key_words')

    for word in keyWords:    # a separate check to stop the accitental use of mute functions
        if "mute" in word:
            speak(System.changeAudio("Test"))
            speak(System.Mute("Test"))
            return 4

    find = sounder.search(keyWords)
    probs=sounder.probability(keyWords)
    print(keyWords)
    print(probs[find])
    print(probs)
    print(find , activities[find])
    if probs[find]<60 :
        print(" function stopped, low probability ")
        speak(conversation.determineCommand(text))
        return 0
    speak(activities[find](query))
    return 0

# getActions("asd")

