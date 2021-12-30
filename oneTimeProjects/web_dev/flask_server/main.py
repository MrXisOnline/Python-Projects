from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_em(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, world</h1>" \
           "<p>This is main page</p>" \
           "<img src='https://media.giphy.com/media/azawGiVGDD2dTqD8X4/giphy.gif'>"


@app.route("/set")
@make_bold
@make_em
@make_underline
def add_style():
    return "Hello"


@app.route("/bye")
def bye():
    return "Bye"

# defining Variable in URLs
# @app.route("/hello/<name>")
# def say_hello(name):
#     return f"Hii {name}"


if __name__ == "__main__":
    app.run(debug=True)
