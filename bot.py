import tweepy
from time import sleep
from colorama import Fore, Style, init
import os
from internals.defs.defs import *
from internals.common import clear, THIS_VERSION, setTitle
from internals.credentials import *


def mainmenue():
	setTitle(f"PIP GUI")
	#Main banner
	clear()
	banner = Style.BRIGHT + f'''{Fore.LIGHTGREEN_EX}
	
            ████████╗██╗    ██╗██╗████████╗████████╗███████╗██████╗     ██████╗  ██████╗ ████████╗
            ╚══██╔══╝██║    ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
               ██║   ██║ █╗ ██║██║   ██║      ██║   █████╗  ██████╔╝    ██████╔╝██║   ██║   ██║   
               ██║   ██║███╗██║██║   ██║      ██║   ██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║   ██║   
               ██║   ╚███╔███╔╝██║   ██║      ██║   ███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
               ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                                        
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
					{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.BLACK} continue with bot                               
					{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.BLACK} open twitter window                        
					{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.BLACK} tweet typed text                
					{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}]{Fore.RED} exits the program 
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
	print(banner)
	choice = str(input(
			f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))

	#all options
	if choice == '1':
		clear()
		opt1()


	elif choice == '2':
		opt2()


	elif choice == '3':
		opt3()


	elif choice == '4':
		clear()
		Style.RESET_ALL
		Fore.RESET
		exit()


if __name__ == "__main__":
	sleep(1)
	mainmenue()

try:
	my_file=open('opnames.txt','r')
	file_lines=my_file.readlines()
	my_file.close()
except FileNotFoundError:
		print(f'\n{Fore.YELLOW}file not found | making it for you{Fore.RESET}\n')
		os.system('type nul > opnames.txt')
