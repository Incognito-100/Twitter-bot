from time import sleep
from colorama import Fore, Style, init
import tweepy
from time import sleep
import os
import os, sys, platform, ctypes, time
from internals.credentials import *
from bot import mainmenue

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#==========================================|option 1|==========================================#
def opt1():
	for line in file_lines:
    # Add try ... except block to catch and output errors
		try:
			print(line)
			if line != '\n':
				api.update_status(line)
			else:
				pass
		except tweepy.TweepError as e:
			print(e.reason)
		sleep(1000000)
#==========================================|option 2|==========================================#
def opt2():
	os.system("start \"\" https://twitter.com/anti_breathing")
	os.system("start \"\" https://developer.twitter.com")
	mainmenue()

#==========================================|option 3|==========================================#
def opt3():
	ttt = input("Enter tweet to tweet: ")
	print(ttt)
	api.update_status(ttt)
	mainmenue()
#==========================================|option 4|==========================================#

my_file=open('opnames.txt','r')
file_lines=my_file.readlines()
my_file.close()
