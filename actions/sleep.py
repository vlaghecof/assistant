
import random
from Audio.AudioManager import  speak
import settings
def go_to_sleep(text):
    replies = ['See you later!', 'Just call my name and I\'ll be there!']
    return (random.choice(replies))


def terminate(text):
    replies = ['See you later!', 'Just call my name and I\'ll be there!',"Sir it was a pleasure ","See you latter "]
    settings.online=False
    return random.choice(replies)



