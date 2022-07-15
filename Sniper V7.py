import os, json
from unicodedata import name
from timeit import repeat
import requests
import json
import time
import re
import pyfiglet
from pprint import pprint
from pyfiglet import figlet_format 

print(figlet_format("KBSNIPER", font = "big" ))


uuid = str(input("Enter their uuid >>> "))
apikey = str(input("Enter your api key >>> "))


while True:


    def getInfo(call):
        r = requests.get(call)
        return r.json()

#URL for api request
    url = f"https://api.hypixel.net/status?key="+ apikey + "&uuid="+ uuid


    data = getInfo(url)

   

    stat = data["session"]

    print(stat)


    time.sleep(1)