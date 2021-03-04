import requests
import json
def Ding(key, secret, content):
    import time
    import hmac
    import hashlib
    import base64
    import urllib.parse
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + key + "&timestamp=" + timestamp + "&sign=" + sign
    head = {'Content-Type': 'application/json'}
    r.encoding = 'utf-8'
    tmp = "{\"msgtype\": \"text\", \"text\": {\"content\": \"" + content + "\"}}"
    r.post(url, data=json.dumps(eval(tmp)), headers=head)


def start():
    cookie = "__cfduid=##########; _ga=##########; _gid=##########; koa:sess=##########; koa:sess.sig=##########"
    key = '钉钉群机器人Webhook'
    secret = "钉钉群机器人加签secret"
    CheckIn = "https://glados.rocks/api/user/checkin"
    Status = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
        'token': 'glados_network'
    }
    checkin = requests.post(CheckIn, headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent,
                                'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(Status, headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    if 'message' in checkin.text:
        text = str("剩余: "+state.json()['data']['leftDays'].split('.')[0]+"天...服务器返回了: "+checkin.json()['message'])
    else:
        text = "COOKIES已失效,请更换!"

    try:
        Ding(key, secret, text)
    except:
        print("未填写钉钉群机器人S/K, 采用本地通知")
        print(text)
if __name__ == '__main__':
    start()

def main_handler(event, context):
    start()
