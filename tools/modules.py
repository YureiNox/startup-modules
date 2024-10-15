import os
import json
import platform
from time import sleep

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m"   

def cd():
    def getmodules():
        with open(os.path.join(os.path.dirname(__file__), 'json/startup.json')) as f:
            return json.load(f)['modules']

    dependencies = getmodules()

    def check_dependencies():
        missing_dependencies = []
        for dependency in dependencies:
            try:
                __import__(dependency)
                print(f"{VERT}{dependency} is already installed.{RESET}")
                sleep(0.5)
            except ImportError:
                print(f"{ROUGE}{dependency} is not installed.{RESET}")
                missing_dependencies.append(dependency)
        
        return missing_dependencies

    sleep(1.5)

    missing_dependencies = check_dependencies()

    if missing_dependencies:
        for dependency in missing_dependencies:
            print(f"Installing {dependency}...")
            sleep(1)
            if platform.system() == 'Windows':
                os.system(f"pip install {dependency}")
            else:
                os.system(f"pip3 install {dependency}")
            sleep(2)
    else:
        print(f"{VERT}All dependencies are already installed.{RESET}")

if __name__ == "__main__":
    cd()
