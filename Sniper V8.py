import os, json
from unicodedata import name
from timeit import repeat
import requests
import json
import time
import re
import pyfiglet
import mojang
from mojang import MojangAPI
from pprint import pprint
from pyfiglet import figlet_format 

print(figlet_format("KBSNIPER", font = "big" ))


kb = str(input("Enter their username >>> "))
cats = str(input("Enter your api key >>> "))

kbcats = MojangAPI.get_uuid(kb)




while True:


    def getInfo(call):
        r = requests.get(call)
        return r.json()

#URL for api request
    kbc = f"https://api.hypixel.net/status?key="+ cats + "&uuid="+ kbcats


    ats = getInfo(kbc)

   
    kbcat = ats["session"]

    print(kbcat)


    time.sleep(1)