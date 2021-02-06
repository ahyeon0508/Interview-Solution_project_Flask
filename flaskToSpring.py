from flask import Flask  # 간단히 플라스크 서버를 만든다

import urllib.request

app = Flask(__name__)

@app.route("/tospring")
def spring():
    return "yejin"

if __name__ == '__main__':
    app.run(debug=False, host="localhost", port=5000)