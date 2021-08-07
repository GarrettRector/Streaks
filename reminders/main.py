import sendmsg
import time
import requests
import ast
from datetime import datetime


def main():
    while True:
        now = datetime.now()
        stime = now.strftime("%S")
        htime = now.strftime("%H")
        if stime == "30":
            request(htime)
            print("30 seconds")
        else:
            time.sleep(0.5)
            print(stime)


def request(htime):
    headers = {'Accept': 'application/vnd.github.cloak-preview'}
    params = ('q', 'author:GarrettRector author-date:2021-08-07')

    while True:
        response = requests.get('https://api.github.com/search/commits', headers=headers, params=params)
        response = "{" + response.text[1:16] + "}"
        response = ast.literal_eval(response)
        commits = response["total_count"]
        if htime == "5":
            if commits < 1:
                sendmsg.sendmessage(f"You have not commited to GitHub today.")
        else:
            time.sleep(60)


if __name__ == '__main__':
    main()
