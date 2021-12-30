import os

import colorgram
from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        f = request.files['img']
        f.save(secure_filename(f.filename))
        img_name = f.filename
        split_tup = os.path.splitext(img_name)
        if split_tup[1] in [".png", ".jpg", ".jpeg"]:
            colors = colorgram.extract(img_name, 50)
            color_list = []
            for c in colors:
                color_list.append(tuple(c.rgb))
            return render_template("index.html", photo=True, colors=color_list)
    return render_template("index.html", photo=False)


if __name__ == "__main__":
    app.run()
