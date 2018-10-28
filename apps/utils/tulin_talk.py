"""
  Created by Amor on 2018-10-24
"""
import json
import requests

__author__ = '骆杨'

s = requests.session()


def talk(content, user_id):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "perception": {
            "inputText": {"text": content}
        },
        "userInfo": {
            "apiKey": "bb77d7d4ac8b4f569ec81a46f3bb2593",
            "userId": user_id
        }
    }
    data = json.dumps(data)
    r = s.post(url, data=data)
    r = json.loads(r.text)
    code = r['intent']['code']
    if code < 10000:
        result = '抱歉，不知道你在说什么(+_+)'
    else:
        result = ''.join([i['values']['text'] for i in r['results']])
    return result
