# by Jakub Wawak
# kubawawak@gmail.com
# all rights reserved

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# object for coloring terminal output
class CPrint:

    # constructor
    def __init__(self):
        colorama_init() # starting the colorama module

    # function for printing text to terminal
    # setting - NORMAL, ERROR, BLUE, GREEN
    def cprint(self,text_to_print, setting):
        match setting:
            case "NORMAL":
                print(text_to_print)
            case "ERROR":
                print(f"{Fore.RED}"+text_to_print+f"{Fore.RESET}")
            case "BLUE":
                print(f"{Fore.BLUE}"+text_to_print+f"{Fore.RESET}")
            case "GREEN":
                print(f"{Fore.GREEN}" + text_to_print + f"{Fore.RESET}")
