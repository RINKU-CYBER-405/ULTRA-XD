import os, platform
 
try:
        import requests
        os.system("git pull")
        
        
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
