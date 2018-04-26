import requests
import re
import time
import hashlib
import base64
import struct

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5ad83e5b"
API_KEY = "35245cc62c1bf716fde81e591a8956e4"


def getHeader():
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + AUE + "\",\"lame\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    bytesString = param.encode(encoding="utf-8")
    paramBase64 = base64.standard_b64encode(bytesString)
    print(paramBase64)
    m2 = hashlib.md5()
    updateStr = str(API_KEY) + str(curTime) + str(paramBase64);
    print(str(API_KEY) + str(curTime) + str(paramBase64))
    m2.update(updateStr.encode(""))
    checkSum = m2.hexdigest()
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        #'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def getBody(text):
    data = {'text': text}
    return data


def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()


r = requests.post(URL, headers=getHeader(), data=getBody("科大讯飞是中国最大的智能语音技术提供商"))
contentType = r.headers['Content-Type']
if contentType == "audio/mpeg":
    sid = r.headers['sid']
    if AUE == "raw":
        writeFile("audio/" + sid + ".wav", r.content)
    else:
        writeFile("audio/" + sid + ".mp3", r.content)
    print
    "success, sid = " + sid
else:
    print
    r.text
