from flask import Flask
import random

ran_num = random.randint(0, 9)
app = Flask(__name__)


# def high(num):
#     return f"<h3>{num} is Too high</h3>" \
#            f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300>" \
#            f"<p>Guess Again</p>"
#
#
# def low(num):
#     return f"<h3>{num} is Too low</h3>" \
#            f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300>" \
#            f"<p>Guess Again</p>"
#
#
# def correct(num):
#     return f"<h3>{num} is that Number</h3>" \
#            f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300>" \
#            f"<p>You Got It!</p>"


@app.route("/")
def main_page():
    return '<h1 style="text-align: center">Guess the Number</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>' \
           '<h3>Have fun!</h3>'


@app.route("/<int:number>")
def guess(number):
    if number > ran_num:
        return f"<h3>{number} is Too high</h3>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300>" \
               f"<p>Guess Again</p>"
    elif number < ran_num:
        return f"<h3>{number} is Too low</h3>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300>" \
               f"<p>Guess Again</p>"
    else:
        return f"<h3>{number} is that Number</h3>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300>" \
               f"<p>You Got It!</p>"


if __name__ == "__main__":
    app.run(debug=True)
