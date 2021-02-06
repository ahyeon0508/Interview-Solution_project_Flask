from flask import Flask  # 간단히 플라스크 서버를 만든다

import json
import base64
import requests

app = Flask(__name__)

@app.route("/tospring")
def spring():

    with open("./yejin.jpg", "rb") as f:
        img = base64.b64encode(f.read())

    URL = "https://afc413bab530409c91e165f3dea9c303.apigw.ntruss.com/custom/v1/6722/e97c53914953b8d900e806f8863dd10ad1162a7ffa1940f053bf57e847abecb5/general"

    # 본인의 Secret Key로 치환
    KEY = "TnlFQ3huV09DdWRYbndOWE1iRWJidURJc05va1dNbWU="

    headers = {
        "Content-Type": "application/json",
        "X-OCR-SECRET": KEY
    }

    data = {
        "version": "V1",
        "requestId": "sample_id",  # 요청을 구분하기 위한 ID, 사용자가 정의
        "timestamp": 0,  # 현재 시간값
        "images": [
            {
                "name": "sample_image",
                "format": "png",
                "data": img.decode('utf-8')
            }
        ]
    }
    data = json.dumps(data)
    response = requests.post(URL, data=data, headers=headers)
    res = json.loads(response.text)

    text = ""
    for img in res['images']:
        for field in img['fields']:
            print(field['inferText'], end=' ')
            text += field['inferText']
            text += " "

    return text

if __name__ == '__main__':
    app.run(debug=False, host="localhost", port=5000)