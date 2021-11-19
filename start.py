import tweepy
from time import sleep
from colorama import Fore, Style, init
import os
from internals.defs.defs import *
from internals.common import clear, THIS_VERSION, setTitle

try:
	import tweepy

except ModuleNotFoundError:
		print(f'\n{Fore.YELLOW}modules not found | Installing for you{Fore.RESET}\n')
		os.system("pip install tweepy")
		os.system("pip install colorama")
		os.system("pip install time")
 

def mainmenue():
	setTitle(f"twitter bot {THIS_VERSION}")
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
					{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.BLACK} name scraper                               
					{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.BLACK} sentence generator                        
					{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.BLACK} bot start  
					{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}]{Fore.BLACK} cleanup
					{Fore.RESET}[{Fore.GREEN}5{Fore.RESET}]{Fore.RED} exits the program 
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
	print(banner)
	choice = str(input(
			f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))

	#all options 
	if choice == '1':
		os.startfile('scraper.py')
		mainmenue()

	
	elif choice == '2':
		file = open('fnames.txt')
		ffile = open('opnames.txt', 'w')
		filelines = file.readlines()
		file.close()
		for line in filelines:
			print(line)
			ffile.writelines("the last leader of the society died of asphyxiation please welocme "+ line)
		ffile.close()
		mainmenue()


	elif choice == '3':
		os.startfile('bot.py')




	elif choice == '4':
		os.system("del opnames.txt")
		os.system("del scraped.txt")
		os.system("del fnames.txt")
		

	elif choice == '5':
		clear()
		Style.RESET_ALL
		Fore.RESET
		exit()


if __name__ == "__main__":
    sleep(1)
    mainmenue()
