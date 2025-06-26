from flask import Flask, request, render_template
import requests

app = Flask(__name__)

NASA_API_KEY = "DEMO_KEY"  # ← 自分のNASA APIキーに置き換えてください

@app.route("/", methods=["GET", "POST"])
def index():
    photos = []
    date = ""
    if request.method == "POST":
        date = request.form["date"]
        api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
        params = {
            "earth_date": date,
            "api_key": NASA_API_KEY
        }
        res = requests.get(api_url, params=params)
        if res.status_code == 200:
            all_photos = res.json().get("photos", [])
            # Navigation Camera の写真を最大4枚だけ取得
            photos = [p for p in all_photos if p["camera"]["full_name"] == "Navigation Camera"][:4]
    return render_template("index.html", photos=photos, date=date)

if __name__ == "__main__":
    app.run(debug=True)