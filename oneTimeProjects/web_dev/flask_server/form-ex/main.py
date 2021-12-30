from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/login", methods=["POST"])
def recv_data():
    if request.method == "POST":
        req = request.form

        user = req["username"]
        passwd = req["passwd"]
        return f"<h1>{user},{passwd}</h1>"
    return render_template("form.html")


if __name__ == "__main__":
    app.run()
