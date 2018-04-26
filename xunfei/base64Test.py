import base64;

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5ad83e5b"
API_KEY = "35245cc62c1bf716fde81e591a8956e4"

param = {"engine_type": "sms16k","aue": "raw"}

#转成bytes string
bytesString = param.encode(encoding="utf-8")
print(bytesString)
paramBase64 = base64.b64encode(bytesString);
print(paramBase64);


