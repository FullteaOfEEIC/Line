import requests
import json
from Line.keys import CHANNEL_ACCESS_TOKEN, me

def sendLINE(content,to=me,CHANNEL_ACCESS_TOKEN=CHANNEL_ACCESS_TOKEN):
    #LINEアカウントにアクセスするためのトークン


    url = "https://api.line.me/v2/bot/message/push"
    headers = {
    "Content-Type" : "application/json; charset=UTF-8",
    'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN
    }
    data={"to":to,"messages":[{"type":"text","text":content}]}

    requests.post(url,data=json.dumps(data),headers=headers)
