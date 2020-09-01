from sounder import Sounder
from actions import webBrowse,sleep,conversation,System
from Audio.AudioManager import speak
# ToDo :add the speach response to all the functions
# ToDo make a list of key words for the activities
sounder = Sounder([[''],['mars', 'photo','space '],['search',"find","look up "],['open']
                    ,["make","note","write"],['sleep','pause'],['terminate','stop all',"over"],
                    ["full",'system','status'],['change','input'],['mute'],['create','project','folder']
                  ])

sounder.set_filter(  {
      "what", "where", "which", "how", "when", "who",
      "is", "are", "makes", "made", "make", "did", "do",
      "to", "the", "of", "from", "against", "and", "or",
      "you", "me", "we", "us", "your", "my", "mine", 'yours',
      "could", "would", "may", "might", "let", "possibly",
      'tell', "give", "told", "gave", "know", "knew",
      'a', 'am', 'an', 'i', 'like', 'has', 'have', 'need',
      'will', 'be', "this", 'that', "for","hey","baby", ",","please",
      "if","so",'kind'
  })

# ToDo make a list of functions

activities=[conversation.undefined,webBrowse.get_mars_photo_url,webBrowse.serch,webBrowse.openWebsite,webBrowse.note,
            sleep.go_to_sleep,sleep.terminate,
            System.system_status,System.changeAudio,System.Mute,System.creteProject

            ]

def getActions(text):
    query=text
    # query="hey baby , open  note   "
    keyWords = sounder.filter(query).get( 'key_words');
    print(keyWords)
    find = sounder.search(keyWords)
    print(find)
    speak(activities[find](query))
    return 3

# getActions("asd")

