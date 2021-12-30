from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def add_book(self, tte, atr, rig):
    obj = User(title=tte, author=atr, rating=rig)
    db.session.add(obj)
    db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"



x = User.query.all()[1]
print(x.id)
