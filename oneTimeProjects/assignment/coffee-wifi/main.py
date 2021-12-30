from flask import Flask, render_template, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from typing import List

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
key = "TopSecret"


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def get_data_dict(ins):
    cafe = ins
    data_dict = {
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "has_toilet": cafe.coffee_price
    }
    return data_dict


def get_keys(d):
    return d.keys()


@app.route("/")
def home():
    data = Cafe.query.all()
    all_dict = {}
    data = Cafe.query.all()
    for i in range(len(data)):
        all_dict[i + 1] = get_data_dict(data[i])
    app.jinja_env.globals.update(get_keys=get_keys)
    return render_template("index.html", data=all_dict)

@app.route("/update-price/<idx>", methods=["POST"])
def update_price(idx):
    price = request.form["new-price"]
    data = Cafe.query.all()
    for e in data:
        if e.id == int(idx):
            cafe = Cafe.query.get(idx)
            cafe.coffee_price = price
            db.session.commit()
            return redirect("/")
    return jsonify(error="ID Not Found"), 404

@app.route("/delete/<idx>", methods=["POST"])
def delete_cafe_data(idx):
    api_key = request.form["api-key"]
    data = Cafe.query.all()
    if api_key == key:
        for e in data:
            if e.id == int(idx):
                cafe = Cafe.query.get(idx)
                db.session.delete(cafe)
                db.session.commit()
                return redirect("/")
        return jsonify(error="ID Not Found"), 404
    return jsonify(error="Not Authorised"), 403
if __name__ == "__main__":
    app.run()
