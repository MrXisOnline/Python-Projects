from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
key = "TopSecret"


def get_data_dict(ins):
    cafe = ins
    data_dict = {
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price
    }
    return data_dict


# Cafe TABLE Configuration
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


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    data = Cafe.query.all()
    cafe = random.choice(data)
    return jsonify(get_data_dict(cafe))


@app.route("/all")
def all_cafes():
    all_dict = {}
    data = Cafe.query.all()
    for i in range(len(data)):
        all_dict[i+1] = get_data_dict(data[i])
    return jsonify(all_dict)


@app.route("/search/<loc>")
def search_cafe(loc):
    data = Cafe.query.all()
    for e in data:
        if e.location.lower() == loc.lower():
            return jsonify(get_data_dict(e))
    return jsonify(error="NOT FOUND")


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    form = request.form
    cafe = Cafe(
        name=form["name"],
        map_url=form["map_url"],
        img_url=form["img_url"],
        location=form["location"],
        seats=form["seats"],
        has_toilet=bool(form["has_toilet"]),
        has_wifi=bool(form["has_wifi"]),
        has_sockets=bool(form["has_sockets"]),
        can_take_calls=bool(form["can_take_calls"]),
        coffee_price=form["coffee_price"]
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response="Success")


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<idx>", methods=["PATCH"])
def update_price(idx):
    price = request.args.get("new_price")
    print(price)
    data = Cafe.query.all()
    for e in data:
        if e.id == int(idx):
            cafe = Cafe.query.get(idx)
            cafe.coffee_price = price
            db.session.commit()
            return jsonify(Message="Success")
    return jsonify(error="ID Not Found"), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<idx>", methods=["DELETE"])
def delete_cafe_data(idx):
    api_key = request.args.get("api-key")
    data = Cafe.query.all()
    if api_key == key:
        for e in data:
            if e.id == int(idx):
                cafe = Cafe.query.get(idx)
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(message="Cafe Data Deleted")
        return jsonify(error="ID Not Found"), 404
    return jsonify(error="Not Authorised"), 403


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
