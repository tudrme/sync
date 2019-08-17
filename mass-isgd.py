magic_array = []

import requests
import time

url = "https://is.gd/create.php"

headers = {
    'User-Agent': "FeelsBad/1.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "is.gd",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

counter = 0

for shortlink in magic_array:
    counter = counter + 1
    print("Now on", counter, "for URL", shortlink)
    querystring = {"format":"simple","url":"https://www.tudrme.com","shorturl":shortlink}
    response = requests.request("GET", url, headers=headers, params=querystring)
    if not (shortlink in response.text):
        print("Something went wrong!")
    time.sleep(20)
