"""Created by Pau Cava"""

"""UTILITIES"""
import time
import sys
"""Text style"""
from colorama import Fore


print(Fore.YELLOW + "███████╗██╗     ███████╗ ██████╗███████╗██████╗  ██████╗ ███╗   ██╗")
print("██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║")
print("█████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║   ██║██╔██╗ ██║")
print("██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║██║╚██╗██║")
print("███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║")
print("╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
print(Fore.LIGHTBLUE_EX + "By Pau Cava. Special thanks: Joe. Who's Joe? JOE MAMA(I have no friends)")
print(Fore.RESET)
def clear_all():
    for i in range(0, 30):
        time.sleep(0.05)
        print()

while True:
    code = input("~$ ")

    if code == "help":
        print(">> exit: exit the terminal.")
        print(">> color: 1->blue 2->red 3->green.")
        print(">> print: prints what you want.")
        print(">> clear: deletes all the text on screen.")
        print(">> math: basic math operations.")
        print(">> joke: tells you a really bad joke ;).")    
    elif code == "exit":
        exit()
    
    elif code == "color 1":
        print(Fore.BLUE + ">> Color set to '1'.")
    
    elif code == "color 2":
        print(Fore.RED + ">> Color set to '2'.")
    
    elif code == "color 3":
        print(Fore.GREEN + ">> Color set to '3'.")
    
    elif code == "print":
        what_to_print = input(">> What do you want me to print? ")
        print(">>" + what_to_print)
    
    elif code == "clear":
        clear_all()

    ########################################################################
    #                           BAD JOKES                                  #
    ########################################################################

    elif code == "joke":
        print(">> How do you call a man that died while eating pasta? He pasta way hahaha.")
    
    ########################################################################
    #                           UTILITIES                                  #
    ########################################################################          
    
    elif code == "ver" or code == "version":
        print("TODO: show python version.")
    
    ########################################################################
    #                             MATH                                     #
    ########################################################################
    
    elif code == "math":
        op = input(">>Operations: (s)um (su)bstract (m)ultipy (d)ivide: ")

        if op == "s":
            num1 = input(">>First num: ")

            num2 = input(">>Second num: ")
            print(">>", int(num1) + int(num2))

        elif op == "su":
            num3 = input(">>First num: ")
           
            num4 = input(">>Second num: ")
            
            print(">>", int(num3) - int(num4))

        elif op == "m":
            num5 = input(">>First num: ")
            num6 = input(">>Second num: ")

            print(">>", int(num5) * int(num6))

        elif op == "d":
            num7 = input(">>First num: ")
            num8 = input(">>Second num: ")

            print(">>", int(num7) / int(num8))
        
    elif code == "joe mama":
        print(Fore.GREEN + ">> DO YOU THINK YOU ARE FUNNY?")
        print(Fore.RESET)
    else:
        print(Fore.RED + ">> That's not a command -> '", code + " ' Type 'help' for more information.")
        print(Fore.RESET)
