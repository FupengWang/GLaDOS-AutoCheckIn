import requests
import json
##########不需要钉钉通知请删除↓中所有代码##########
import time
import hmac
import hashlib
import base64
import urllib.parse
secret = '钉钉群机器人SECRET'
key = "钉钉群机器人加签KEY"
timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
DING = "https://oapi.dingtalk.com/robot/send?access_token=" + key + "&timestamp=" + timestamp + "&sign=" + sign
##########不需要钉钉通知请删除↑中所有代码##########
def start():
    #填入COOKIE
    cookie = "__cfduid=##########; _ga=##########; _gid=##########; koa:sess=##########; koa:sess.sig=##########"
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
    #本地输出请清除下面一行代码的注释
    #print(text)
    ##########不需要钉钉通知请删除↓中所有代码##########
    requests.encoding = "utf-8"
    head = {'Content-Type': 'application/json'}
    tmp = "{\"msgtype\": \"text\", \"text\": {\"content\": \"" + text + "\"}}"
    requests.post(DING, data=json.dumps(eval(tmp)), headers=head)
    ##########不需要钉钉通知请删除↑中所有代码##########
if __name__ == '__main__':
    start()

def main_handler(event, context):
    start()