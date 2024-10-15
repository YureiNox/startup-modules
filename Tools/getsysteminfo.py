import os
import platform
import socket

class GetInfo:
    def __init__(self):
        self._username = os.getlogin()
        self._hostname = socket.gethostname()
        self._ip_address = socket.gethostbyname(self._hostname)
        self._platform_name = platform.system()
        self._platform_version = platform.version()
        self._architecture = platform.architecture()
        self._machine = platform.machine()
        self._processor = platform.processor()
        self._help = print("Available option are username, hostname, ip_adress, platform_name, plateform_version, architecture, machine, processor, help")

    def username(self):
        return self._username

    def hostname(self):
        return self._hostname

    def ip_address(self):
        return self._ip_address

    def platform_name(self):
        return self._platform_name

    def platform_version(self):
        return self._platform_version

    def architecture(self):
        return self._architecture

    def machine(self):
        return self._machine

    def processor(self):
        return self._processor
    
    def help(self):
        return self._help

if __name__ == "__main__":
    info = GetInfo()
    print(info.username()) 
