from flask import Flask, render_template, redirect, flash
from form_model import MyForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "testing_purpose"
ADMIN_MAIL = "sg704992@gmail.com"
ADMIN_PASS = "hello123"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.mail.data == ADMIN_MAIL and form.passwd.data == ADMIN_PASS:
            return redirect("/success")
        else:
            return redirect("/access-denied")
    return render_template("login.html", form=form)


@app.route("/success")
def logged_in():
    return render_template("success.html")


@app.route("/access-denied")
def un_auth():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run()
