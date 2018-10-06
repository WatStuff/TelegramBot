import json
import requests
import time

token="603809094:AAGSs4gbLqhK8xfqicOwAIDWN3eTwXfuy6k"
URL = "https://api.telegram.org/bot{}/".format(token)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

while True:
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    time.sleep(0.5)
