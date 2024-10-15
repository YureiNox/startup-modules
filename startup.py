from tools.internet import ci
from tools.modules import cd
from tools.key import jinfo
from time import sleep
import os

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"
RESET = "\033[0m"

info = jinfo()
file = info.get_value("filename")

def main():
    print(f"{VIOLET}\n--- Checking Info ---{RESET}")
    sleep(2)
    ci()
    sleep(1)
    cd()
    sleep(2)
    print(f"{VIOLET}\n--- Startup ---{RESET}")
    sleep(2)
    print(f"{JAUNE}Loading Script Files...{RESET}")
    sleep(2)
    os.system("python3 " + file)

if __name__ == '__main__':
    main()
