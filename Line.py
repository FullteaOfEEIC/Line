import requests
import json
from keys import CHANNEL_ACCESS_TOKEN, me


def sendLINE(content, type="text", to=me, CHANNEL_ACCESS_TOKEN=CHANNEL_ACCESS_TOKEN):
    # LINEアカウントにアクセスするためのトークン

    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN
    }
    data = createData(type, to)

    print(requests.post(url, data=json.dumps(data), headers=headers).text)


def createData(type, to, *, text=None, stickerId=None, packageId=None, originalContentUrl=None, previewImageUrl=None):
    data = {"to": to}
    if type == "text":
        assert text != None
        messages = {"type": "text", "text": content}
    elif type == "sticker":
        assert stickerId != None
        assert packageId != None
        messages = {"type": "sticker",
                    "packageId": packageId, "stickerId": stickerId}
    elif type == "image":
        messages = {"type": "image", "originalContentUrl": originalContentUrl,
                    "previewImageUrl": previewImageUrl}
    elif type == "video":
        messages = {"type": "video", "originalContentUrl": originalContentUrl,
                    "previewImageUrl": previewImageUrl}


    data["messages"] = [messages]
    return data


if __name__ == "__main__":
    sendLINE("テスト送信です", type="image")
