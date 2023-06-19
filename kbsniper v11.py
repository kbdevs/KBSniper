import pyfiglet
import requests
from mojang import API
import time

api = API()

print(pyfiglet.figlet_format("KBSNIPER", font="big"))

kb = input("Enter their username >>> ")
cats = input("Enter your api key >>> ")

kbcats = api.get_uuid(kb)

while True:
    def get_info(call):
        return requests.get(call).json()

    kbc = f"https://api.hypixel.net/status?key={cats}&uuid={kbcats}"
    ats = get_info(kbc)
    kbcat = ats["session"]
    print(kbcat)
    time.sleep(2)

