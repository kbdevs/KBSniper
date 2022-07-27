
from timeit import repeat
import requests
import json
import time
from pprint import pprint


while True:

    api_token = 'get your own'
    api_url = 'https://apiv2.nethergames.org/v1/players/kbcats'

    headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


    def get_account_info():


        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    account_info = get_account_info()

    status = account_info['lastServerParsed']

    status2 = account_info[ 'lastSeen']

    print(status)
    print(status2)


    time.sleep(1)