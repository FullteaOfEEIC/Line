import requests
import json

def sendLINE(content,to,CHANNEL_ACCESS_TOKEN):
    #LINEアカウントにアクセスするためのトークン


    url = "https://api.line.me/v2/bot/message/push"
    headers = {
    "Content-Type" : "application/json; charset=UTF-8",
    'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN
    }
    data={"to":to,"messages":[{"type":"text","text":content}]}

    requests.post(url,data=json.dumps(data),headers=headers)
