from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "クラゲです…Flaskで直接文字を表示しています<br>Renderでアプリを公開できましたね<br>これからPythonのアプリ制作を解説していくのでみんなで頑張りましょう！"
