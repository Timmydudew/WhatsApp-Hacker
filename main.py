import colorama
import time, sys
from colorama import Fore, Style
Green = Fore.GREEN
Yellow =Fore.YELLOW
Blue = Fore.BLUE
def show_banner() :
    banner = print(f'''
{Fore.GREEN}
    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌       ▐░▌         ▐░▌ ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌         ▐░▌▐░▌       ▐░▌
    ▐░▌       ▐░▌        ▐░▌  ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
    ▐░▌       ▐░▌       ▐░▌   ▐░░░░░░░░░░░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░▌       ▐░▌      ▐░▌    ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀
    ▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌       ▐░▌▐░▌     ▐░▌            ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌         ▐░▌▐░▌     ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌    ▐░▌      ▐░▌               ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌           ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌
    ▐░░░░░░░░░░░▌   ▐░▌       ▐░▌               ▐░░░░░░░░░░░▌▐░▌       ▐░▌          ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
    ▀▀▀▀▀▀▀▀▀▀▀     ▀         ▀                 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀            ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀
    Coded by Mr Juice
    I mma Say Fuck You If you Dont Follow Me🖕
    Chat Me: https://bio.link/mrjuice
    
********************************
    ''')
show_banner()
def delay_print(s) :
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.095)
def num():
    while True:
        number = input("Number : +91")
        numberr = "+91" +number
        lenfind = len(number)
        if (number.isnumeric()):
            if (lenfind < 10):
                print(f"{Fore.RED}Number must be atleast 10 digits")
            elif (lenfind > 10):
                print(f"{Fore.RED}Number must be less than 10 digits")
            elif (lenfind==10):
                delay_print(f"{Fore.YELLOW}Signalling " + numberr + " . . .\n")
                delay_print(f"{Fore.YELLOW}Checking the network availability . . .\n")
                delay_print("Connection successfull with " + numberr+"\n")
                print(f"{Fore.BLUE}****MAKE SURE YOU REQUESTED THE OTP****\n")
                delay_print(f"{Fore.YELLOW}Gaining access to SMS . . . ( This will take some time )\n")
                time.sleep(3)
                delay_print(f"{Fore.GREEN}Access gained to SMS of " + numberr+"\n")
                delay_print(f"{Fore.YELLOW}Reading SMS . . .\n")
                print(f"{Fore.GREEN}Whatsapp OTP found ! !\n")
                otp = input("Press '1' to show the OTP : ")
                print(f"{Fore.CYAN}USE THE OTP CODE AND LOGIN\n")
                print(f"{Fore.RED}Follow and Support Me By Subscribing and following on Instagram. . . ")
            else:
                print("Unexpected error occured, contact https://bio.link/mrjuice for a solution")
        else: print(f"{Fore.RED}Number format is incorrect")
        num()

num()



