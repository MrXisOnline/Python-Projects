from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
db = SQLAlchemy(app)


def add_blog(tte, sub, iu, au, bd):
    n = dt.now()
    n_date = n.strftime("%B %d, %Y")
    b = BlogPost(
        title=tte,
        subtitle=sub,
        img_url=iu,
        author=au,
        body=bd,
        date=n_date
    )
    db.session.add(b)
    db.session.commit()


def reassign_blog(idx, tte, sub, iu, au, bd):
    bg = BlogPost.query.get(idx)
    bg.title = tte
    bg.subtitle = sub
    bg.img_url = iu
    bg.author = au
    bg.body = bd
    db.session.commit()


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = BlogPost.query.all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_blog(post_id):
    posts = BlogPost.query.all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == post_id:
            requested_post = blog_post
    form = CreatePostForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        author=requested_post.author,
        img_url=requested_post.img_url,
        body=requested_post.body
    )
    if request.method == "POST":
        title = form.title.data
        subtitle = form.subtitle.data
        img_url = form.img_url.data
        author = form.author.data
        body = form.body.data
        reassign_blog(post_id, title, subtitle, img_url, author, body)
        return redirect("/")
    return render_template("make-post.html", id=post_id, form=form, edit=1)


@app.route("/make-blog", methods=["GET", "POST"])
def make_blog():
    form = CreatePostForm()
    if request.method == "POST":
        title = form.title.data
        subtitle = form.subtitle.data
        img_url = form.img_url.data
        author = form.author.data
        body = form.body.data
        add_blog(title, subtitle, img_url, author, body)
        return redirect("/")
    return render_template("make-post.html", form=form, edit=0)


@app.route("/delete-blog/<int:index>")
def delete_blog(index):
    bg = BlogPost.query.get(index)
    db.session.delete(bg)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
