from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "DEMO_KEY"  # NASAのAPIキー（DEMO_KEYでもOK）

@app.route("/", methods=["GET", "POST"])
def index():
    default_date = "2015-06-03"
    # フォームからの日付、なければデフォルト
    date = request.form.get("date") if request.method == "POST" else default_date

    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {"earth_date": date, "api_key": API_KEY}
    response = requests.get(url, params=params)

    photos = []
    if response.ok:
        data = response.json()
        photos = [photo["img_src"] for photo in data["photos"][:4]]  # 最大4枚表示

    return render_template("index.html", photos=photos, date=date)
