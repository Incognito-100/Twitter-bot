import os, sys, platform, ctypes, time

from colorama import Fore
from time import sleep
from itertools import cycle


THIS_VERSION = "1.3"

def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120
    return

def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str} | Made By Incognito100")
    else:
        os.system(f"\033]0;{str} | Made By Incognito100\a")