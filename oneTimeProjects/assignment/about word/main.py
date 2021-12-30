from flask import Flask, render_template, request
import requests
header = {
    "Authorization": "Token 87ad2f225d6ab3ed277d994a42a1946ed3b9a9d7"
}
url = "https://owlbot.info/api/v4/dictionary/"
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        word = request.form["word"]
        if len(word) != 0:
            s_url = url + word
            response = requests.get(s_url, headers=header)
            data = response.json()
            if type(data) != list:
                send_dict = {
                    "word": data["word"],
                    "type": data["definitions"][0]["type"],
                    "define": data["definitions"][0]["definition"],
                    "ex": data["definitions"][0]["example"]
                }
                return render_template("index.html", error=False, first=True, send=send_dict)
            return render_template("index.html", error=True, first=True, word=word)
    return render_template("index.html", first=False)


if __name__ == "__main__":
    app.run()
