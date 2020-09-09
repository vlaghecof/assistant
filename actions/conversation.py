import random







def greetings():
    replies = [
        'Have a good one Sir',
        'Hello there.',
        'I am fully online Sir'
    ]
    return (random.choice(replies))


def who_are_you():
    va_name = " "
    messages = ['I am ' + va_name + ', your lovely personal assistant.',
                va_name + ', did\'nt I tell you before?',
                'You ask that so many times! I am ' + va_name]

    return (random.choice(messages))


def toss_coin():
    outcomes = ['heads', 'tails']
    return ('I just flipped a coin. It shows ' + random.choice(outcomes))


def how_am_i():
    replies = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You are sexy!',
        'You look like the kindest person that I have met.'
    ]
    return (random.choice(replies))


def who_am_i():
    return ('You are my creator  a brilliant person. I love you!')


def where_born():
    replies = [
        'I was created by Vlad ,  but dont tell further  it is supposed to be a secret' ,
        'Master V is my creator '
    ]
    return (random.choice(replies))



def how_are_you():
    replies = [
        'I am still online Sir',
        'I am very good .'
    ]
    return (random.choice(replies))


def are_you_up():
    replies = [
               'For you sir, always.',
               'Functioning at 100% capacity ! '
              ]
    return (random.choice(replies))


def love_you():
    replies = [
               'I love you too.',
               'You are looking for love in the wrong place.'
              ]
    return (random.choice(replies))


def marry_me():
    return ('I have been receiving a lot of marriage proposals recently.')


def undefined(text):
    return ('I dont know what that means!')

WORDS = { greetings:    ['hello','hy','good day','good evening'],
         who_are_you :  ['who are you'],
         toss_coin :     ['heads', 'tails','head or tail',
                                  'toss a coin', 'flip a coin'],
         how_am_i:       ['how  i look ','how do i look' ,'how am i'],
         who_am_i:       ['who am  i'],
         where_born:     ['where created',"who created you"],
         how_are_you:    ['how are you','are you ok'],
         are_you_up:     ['you up', "you online ","system online"],
         love_you:       ['love you'],
         marry_me:       ['marry me'],
         undefined:      [],
          }
conversationList=[]
for key,val in WORDS.items():
    conversationList+=val

def determineCommand( text):
    for key, val in WORDS.items():
        for phrase in val:
            if phrase in text:
                print(phrase,key ,"->",val)
                return key()
    return "I did not quite got that , please repeat "