import requests

url_final = "http://tinyurl.com/create.php"

magic_urls = []

my_link = "http://www.tudrme.com"

headers = {
    'User-Agent': "Client/1.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "tinyurl.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

for url in magic_urls:
    print("Now using URL" + url)
    querystring = {"url":"http://www.tudrme.com","submit":"Make%20TinyURL%21","alias":url}
    response = requests.request("GET", url_final, headers=headers, params=querystring)
    if("TinyURL was created!" in response.text):
        print("Created URL.")
    else:
        print("Error in creating URL!")
        print(response.text)
