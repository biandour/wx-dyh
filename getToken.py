import json
import requests
from appsecret import APPSECRET

def get_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    args = {
        'grant_type': 'client_credential',
        'appid': 'wxd195bd8545e019a2',
        'secret': APPSECRET
    }
    response = requests.get(url, params=args)
    return json.loads(response.text)

# print(json.dumps(response))
