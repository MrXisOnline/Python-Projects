from flask import Flask, render_template, redirect, url_for, flash, abort, request
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from functools import wraps
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    tasks = relationship("Tasklist", back_populates="user")


class Tasklist(db.Model):
    __tablename__ = "tasklist"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(250), unique=True, nullable=False)
    creation_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    user = relationship("Users", back_populates="tasks")
    item = relationship("Items", back_populates="task")


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(250))
    creation_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    task = relationship("Tasklist", back_populates="item")
    task_id = db.Column(db.Integer, db.ForeignKey("tasklist.id"))


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route("/")
def landing():
    return render_template("index.html", is_logged=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        passwd = form.passwd.data
        all_users = Users.query.all()
        for user in all_users:
            if user.email == email:
                flash("Email Already Exists!")
                return redirect("/login")
        enc_passwd = generate_password_hash(passwd, method="pbkdf2:sha256", salt_length=8)
        user = Users(
            name=name,
            email=email,
            password=enc_passwd
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect("/home")
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        passwd = form.passwd.data
        all_users = Users.query.all()
        for user in all_users:
            if user.email == email:
                if check_password_hash(user.password, passwd):
                    login_user(user)
                    return redirect("/home")
                else:
                    flash("Email/Password is Incorrect")
                    return redirect("/login")
        flash("Email Doesn't Exists!")
        return redirect("/register")
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/home")
@login_required
def home():
    tasks = current_user.tasks
    if len(tasks) != 0:
        all_task_dict = []
        for t in tasks:
            task_dl = {"id": t.id,
                       "name": t.name,
                       "cd": t.creation_date,
                       "ed": t.end_date}
            items = t.item
            if len(items) != 0:
                all_item_dict = []
                for i in items:
                    if i.status == "mark":
                        item_dl = {"id": i.id,
                                   "name": i.name,
                                   "status": True,
                                   "cd": i.creation_date,
                                   "ed": i.end_date}
                    else:
                        item_dl = {"id": i.id,
                                   "name": i.name,
                                   "status": False,
                                   "cd": i.creation_date,
                                   "ed": i.end_date}
                    all_item_dict.append(item_dl)
                task_dl["item-exist"] = True
                task_dl["items"] = all_item_dict
            else:
                task_dl["item-exist"] = False
            all_task_dict.append(task_dl)
        return render_template("home.html", is_logged=current_user.is_authenticated, task=True, tasks=all_task_dict)
    return render_template("home.html", is_logged=current_user.is_authenticated, task=False)


@app.route("/add-task", methods=["POST"])
@login_required
def addtask():
    form = request.form
    task_name = form["task-name"]
    end_date = form["e-date"]
    cre_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    task = Tasklist(
        name=task_name,
        creation_date=end_date,
        end_date=cre_date,
        user=current_user
    )
    db.session.add(task)
    db.session.commit()
    return redirect("/home")


@app.route("/del-task/<int:idx>")
@login_required
def deltask(idx):
    task = Tasklist.query.get(int(idx))
    db.session.delete(task)
    db.session.commit()
    return redirect("/home")


@app.route("/add-item/<int:idx>", methods=["POST"])
@login_required
def additem(idx):
    form = request.form
    task = Tasklist.query.get(int(idx))
    item_name = form["item-name"]
    end_date = form["ie-date"]
    cre_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    item = Items(
        name=item_name,
        status="unmarked",
        creation_date=end_date,
        end_date=cre_date,
        task=task
    )
    db.session.add(item)
    db.session.commit()
    return redirect("/home")


@app.route("/del-item/<int:idx>")
@login_required
def delitem(idx):
    item = Items.query.get(int(idx))
    db.session.delete(item)
    db.session.commit()
    return redirect("/home")


@app.route("/up-status/<int:idx>/<int:call>")
@login_required
def update_status(idx, call):
    item = Items.query.get(int(idx))
    if call == 1:
        item.status = "unmark"
        db.session.commit()
    else:
        item.status = "mark"
        db.session.commit()
    return redirect("/home")


if __name__ == "__main__":
    app.run()
