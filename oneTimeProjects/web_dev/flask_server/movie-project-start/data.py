from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.id}"


# db.create_all()
# m = Movie(
#     title="Matrix",
#     year=2018,
#     description="A biologist signs up for a dangerous, secret expedition into a mysterious zone where the laws of "
#                 "nature don't apply.",
#     rating=7.8,
#     review="To be sure, the climax delivers copious amounts of blood and guts and tension and look-away temptations. "
#            "But there are enough interesting surprises, in addition to the narrative promise, to provide for the "
#            "presumed, and now quite desired, sequels.",
#     img_url="https://www.bing.com/th?id=AMMS_a62ab6a54831fd9e1a5e4a1a96b06913&w=96&h=149&c=8&rs=1&o=5&dpr=1.25&pid=3"
#             ".1&rm=2 "
# )
# db.session.add(m)
# db.session.commit()
# data = Movie.query.order_by(Movie.rating.asc()).all()
# data = Movie.query.all()
# for m in data:
#     print(m.title)
