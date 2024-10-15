import os
import sys
from time import sleep
import platform

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m" 

def ci():
    def check_internet():
        try:
            if platform.system() == 'Windows':
                result = os.system("ping -n 1 google.com > NUL")
            elif platform.system() == 'Linux' or platform.system() == 'Darwin':
                result = os.system("ping -c 1 google.com > /dev/null 2>&1")
            else:
                return False
            return result == 0
        except Exception as e:
            return False

    if not check_internet():
        print(f"{ROUGE}No internet connection detected.{RESET}")
        sys.exit(1)
    else:
        sleep(0.5)
        print(f"{VERT}Internet connection Found!{RESET}")
        sleep(0.5)
        print("Please wait...")

if __name__ == "__main__":
    ci()
