isgd_array = []

addresses = []

import requests

url = ""

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "",
    "DNT": "1",
    "Host": "",
    "Pragma": "no-cache",
    "Referer": "",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "",
    "X-Requested-With": "XMLHttpRequest"
}

value = 0

for isgd_link in isgd_array:
    querystring = {"action":"add","url":isgd_link,"keyword":addresses[value],"nonce":""}
    response = requests.request("GET", url, headers=headers, params=querystring)
    value = value + 1
    print("URL VALUE ON", value, "ADDED WITH CODE",addresses[value - 1])

print(response.text)