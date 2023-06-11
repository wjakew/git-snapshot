# by Jakub Wawak
# kubawawak@gmail.com
# all rights reserved

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


# object for coloring terminal output
class CPrint:
    history_collection = []
    history_user_input = []

    # constructor
    def __init__(self):
        colorama_init()  # starting the colorama module

    # function for printing text to terminal
    # setting - NORMAL, ERROR, BLUE, GREEN
    def cprint(self, text_to_print, setting):
        self.history_collection.append(text_to_print)
        match setting:
            case "NORMAL":
                print(text_to_print)
            case "ERROR":
                print(f"{Fore.RED}" + text_to_print + f"{Fore.RESET}")
            case "BLUE":
                print(f"{Fore.BLUE}" + text_to_print + f"{Fore.RESET}")
            case "GREEN":
                print(f"{Fore.GREEN}" + text_to_print + f"{Fore.RESET}")
            case "RED":
                print(f"{Fore.RED}" + text_to_print + f"{Fore.RESET}")

    # function for printing menu elements
    def menuprint(self, menu_text, mode):
        if mode == 1:
            # UI printing
            print(f"{Fore.LIGHTCYAN_EX}" + menu_text + f"{Fore.RESET}")
        else:
            # normal printing
            print(f"{Fore.CYAN}" + menu_text + f"{Fore.RESET}")

    # function for getting user terminal input
    def getuianswer(self):
        user_input = input(f"{Fore.GREEN}"+">"+f"{Fore.RESET}")
        self.history_user_input.append(user_input)


