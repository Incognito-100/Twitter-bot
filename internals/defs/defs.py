import os

# ==========================================|auto import/install modules|==========================================#
try:
    import tweepy

except ModuleNotFoundError:
    print(f'\nmodules not found | Installing for you\n')
    os.system("pip install tweepy")
    os.system("pip install colorama")
    os.system("pip install time")
    os.system("pip install selenium")
    os.system("pip install pyperclip")

from time import sleep
from colorama import Fore, Style, init
from time import sleep
import sys, platform, ctypes, time
from internals.credentials import *
from bot import mainmenue

# ==========================================|setup auth components for bot|==========================================#
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# ==========================================|option 1|==========================================#
def opt1():
    for line in file_lines:
        # Add try ... 
        try:
            print(line)
            if line != '\n':
                api.update_status(line)
                print("tweeting next in 15 minuts")
                #make a progress bar for the user to see how long it takes to tweet the next line in 15 minutes
                for i in range(0, 15):
                    print(f"{i}/15")
                    sleep(60)
                    clear()
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(900)


# ==========================================|option 2|==========================================#
def opt2():
    os.system("start \"\" https://twitter.com/anti_breathing")
    os.system("start \"\" https://developer.twitter.com")
    mainmenue()


# ==========================================|option 3|==========================================#
def opt3():
    ttt = input("Enter tweet to tweet: ")
    print(ttt)
    api.update_status(ttt)
    mainmenue()


# ==========================================|option 4|==========================================#

my_file = open('opnames.txt', 'r')
file_lines = my_file.readlines()
my_file.close()
