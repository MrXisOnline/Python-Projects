from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#
# def append_user(em, pd, n):
#     enc_passwd = generate_password_hash(pd, method="pbkdf2:sha256", salt_length=8)
#     u = User(
#         email=em,
#         password=enc_passwd,
#         name=n
#     )
#     db.session.add(u)
#     db.session.commit()


def get_name(em):
    users = User.query.all()
    for u in users:
        if u.email == em:
            return u.name
    return "No Name"


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = request.form
        name = form["name"]
        email = form["email"]
        passwd = form["password"]
        users = User.query.all()
        for user in users:
            if user.email == email:
                flash("Email Already Exists!")
                return redirect("/login")
        enc_passwd = generate_password_hash(passwd, method="pbkdf2:sha256", salt_length=8)
        u = User(
            email=email,
            password=enc_passwd,
            name=name
        )
        db.session.add(u)
        db.session.commit()
        login_user(u)
        flash("User Registered")
        return redirect("/secrets")
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        email = form["email"]
        passwd = form["password"]
        users = User.query.all()
        for user in users:
            if user.email == email:
                if check_password_hash(user.password, passwd):
                    login_user(user)
                    flash("Successfully Logged-in")
                    return redirect("/secrets")
                else:
                    flash("Email/Password is Incorrect")
                    return redirect("/login")
        flash("Email Doesn't Exists")
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("User Logged-Out")
    return redirect("/")


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run()
