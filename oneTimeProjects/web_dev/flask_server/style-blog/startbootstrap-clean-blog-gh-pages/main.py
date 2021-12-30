from flask import Flask, render_template, request
import requests

blog_url = "https://api.npoint.io/3dc6a01aed758dd851d7"
app = Flask(__name__)


@app.route("/")
def home():
    blog_res = requests.get(url=blog_url)
    blog_data = blog_res.json()
    return render_template("index.html", posts=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def post(num):
    blog_res = requests.get(url=blog_url)
    blog_data = blog_res.json()[int(num) - 1]
    return render_template("post.html", data=blog_data, id=num)


@app.route("/send", methods=["GET","POST"])
def send_data():
    if request.method == "POST":
        req_data = request.form
        name = req_data["name"]
        mail = req_data["email-id"]
        no = req_data["ph-no"]
        msg = req_data["msg"]
        print(f"Name:{name}\nMail:{mail}\nNumber:{no}\nMessage:{msg}\n")
        return "<h1>Success</h1>"


if __name__ == "__main__":
    app.run()
