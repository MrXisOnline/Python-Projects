from flask import Flask, render_template
from datetime import datetime as dt
import requests

blog_url = "https://api.npoint.io/3dc6a01aed758dd851d7"
gender_url = "https://api.genderize.io/"
age_url = "https://api.agify.io/"
app = Flask("__name__")


@app.route("/")
def home():
    return render_template("index.html", name="Suraj", year=dt.now().year)


@app.route("/guess/<name>")
def guess(name):
    para = {"name": name}
    age_res = requests.get(url=age_url, params=para)
    gender_res = requests.get(url=gender_url, params=para)
    age_json = age_res.json()
    gender_json = gender_res.json()
    return render_template("guess.html",
                           person=name,
                           age=age_json["age"],
                           gender=gender_json["gender"],
                           year=dt.now().year)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_res = requests.get(url=blog_url)
    blog_data = blog_res.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run()
