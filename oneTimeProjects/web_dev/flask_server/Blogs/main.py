from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/3dc6a01aed758dd851d7"
app = Flask(__name__)


@app.route("/")
def home():
    blog_res = requests.get(url=blog_url)
    blog_data = blog_res.json()
    return render_template("index.html", posts=blog_data)


@app.route("/post/<num>")
def load_blog(num):
    print(num)
    blog_res = requests.get(url=blog_url)
    blog_data = blog_res.json()[int(num)-1]
    return render_template("blog.html", data=blog_data, id=num)


if __name__ == "__main__":
    app.run(debug=True)
