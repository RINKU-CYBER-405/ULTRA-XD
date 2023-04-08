import os, platform
 
try:
        import requests
        os.system("git pull")
        os.system('clear');print('\x1b[38;5;46m checking new update\033[32;1m FB-KING \x1b[38;5;46m ULTRA-GREEN Tools')
        
except:
        os.system('pip2 install requests')
import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from ULTRA import register_device
        register_device()
elif bit == "32bit":
        from ULTRA import register_device
        register_device()
