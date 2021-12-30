from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def add_book(tte, atr, rig):
    obj = User(title=tte, author=atr, rating=rig)
    db.session.add(obj)
    db.session.commit()


def delete_book(idx):
    book_ins = User.query.get(idx)
    db.session.delete(book_ins)
    db.session.commit()


def edit_rating(idx, rate):
    book_ins = User.query.get(idx)
    book_ins.rating = rate
    db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"


@app.route('/')
def home():
    all_books = User.query.all()
    text_list = []
    id_list = []
    if len(all_books) != 0:
        for b in all_books:
            text = f"{b.title} - {b.author} - {b.rating}/10"
            id_list.append(b.id)
            text_list.append(text)
        return render_template("index.html", books=text_list, id=id_list, msg="")
    else:
        message = "Library Is Empty."
        return render_template("index.html", books=text_list, msg=message)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/add_book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        req = request.form
        book_name = req["book-name"]
        book_author = req["book-author"]
        book_rating = req["book-rating"]
        if book_name != "" and book_author != "" and book_rating != "":
            add_book(book_name, book_author, book_rating)
            return redirect("/")
    return redirect("/add")


@app.route("/del/<idx>")
def deletion(idx):
    delete_book(idx)
    return redirect("/")


@app.route("/set_rating/<idx>")
def edit_rate(idx):
    book_ins = User.query.get(idx)
    return render_template("edit.html", idx=idx, book_name=book_ins.title, rating=book_ins.rating)


@app.route("/edit", methods=["GET", "POST"])
def set_new_rating():
    if request.method == "POST":
        form = request.form
        idx = form["id"]
        rate = form["rating"]
        edit_rating(idx, rate)
        return redirect("/")
    return redirect("/")


if __name__ == "__main__":
    app.run()
