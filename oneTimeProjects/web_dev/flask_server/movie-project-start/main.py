from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

id_movie_url = "https://api.themoviedb.org/3/movie/"
no_img_link = "https://th.bing.com/th/id/R1e54ddf5be1bc1cfc1ec660b5a629770?rik=Wu22K3FZtdnafg&riu=http%3a%2f" \
              "%2falliance.education.nmsu.edu%2ffiles%2f2013%2f10%2fno-photo-available-icon.jpg&ehk" \
              "=a5y0UhLEkpnsL74Prf7KhueaPAHhKi%2fNXwElH8990Kk%3d&risl=&pid=ImgRaw "
image_url = "https://image.tmdb.org/t/p/w500"
path_image_url = "https://api.themoviedb.org/3/movie/"
movie_url = "https://api.themoviedb.org/3/search/movie"
DB_API_KEY = "6927a10b43bc23ab0e252b3e471f350a"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)


def get_image(idx):
    path_url = path_image_url + str(idx) + "/images"
    para = {"api_key": DB_API_KEY}
    img_response = requests.get(path_url, params=para)
    data = img_response.json()["posters"]
    if len(data) != 0:
        path = data[0]["file_path"]
        img_link = image_url + path
    else:
        img_link = no_img_link
    return img_link

#
# def set_ranking():
#     obj_data = Movie.query.order_by(Movie.ranking.desc()).all()
#     i = len(obj_data)
#     if len(obj_data) != 0:
#         for movie in obj_data:
#             idx = movie.id
#             m = Movie.query.get(idx)
#             m.ranking = i
#             db.session.commit()
#             i -= 1


def edit(idx, rate, review):
    m = Movie.query.get(idx)
    m.rating = rate
    m.review = review
    db.session.commit()


def delete(idx):
    m = Movie.query.get(idx)
    db.session.delete(m)
    db.session.commit()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class EditMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5 :", validators=[DataRequired()])
    review = StringField("Your Review :", validators=[DataRequired()])
    submit = SubmitField("Submit It")


class AddMovieForm(FlaskForm):
    movie = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # check = Movie.query.all()
    movies_data = []
    obj_data = Movie.query.order_by(Movie.rating.asc()).all()
    rank = len(obj_data)
    if rank != 0:
        for m in obj_data:
            d_add = {
                "id": m.id, "title": m.title, "year": m.year,
                "desc": m.description, "rating": m.rating,
                "rank": rank, "rev": m.review, "img": m.img_url
            }
            movies_data.append(d_add)
            rank -= 1
        return render_template("index.html", movies=movies_data, msg=0)
    return render_template("index.html", msg=1)


@app.route("/edit_movie/<idx>", methods=["GET", "POST"])
def edit_movie_details(idx):
    form = EditMovieForm()
    if form.validate_on_submit():
        rate = form.rating.data
        review = form.review.data
        edit(idx, rate, review)
        return redirect("/")
    return render_template("edit.html", id=idx, form=form)


@app.route("/delete_movie/<idx>")
def delete_movie(idx):
    delete(idx)
    # set_ranking()
    return redirect("/")


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_name = form.movie.data
        para = {
            "query": movie_name,
            "api_key": DB_API_KEY
        }
        response = requests.get(movie_url, params=para)
        data = response.json()["results"]
        send_data = []
        for e in data:
            e_data = {
                "print_data": f"{e['title']} - {e['release_date'][0:4]}",
                "id": e["id"]
            }
            print(e_data)
            send_data.append(e_data)
        return render_template("select.html", data=send_data)
    return render_template("add.html", form=form)


@app.route("/add/<idx>")
def add_movie_to_db(idx):
    para = {"api_key": DB_API_KEY}
    m_response = requests.get(id_movie_url + str(idx), params=para)
    data = m_response.json()
    img = get_image(idx)
    m = Movie(
        title=data["title"],
        year=data["release_date"][0:4],
        description=data["overview"],
        rating=data["vote_average"],
        review="Nothing To Show",
        img_url=img
    )
    db.session.add(m)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
