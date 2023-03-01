from flask import Flask

helloworld = Flask(__name__)


@helloworld.route('/')
def run():
    return "{\"message\": \"Hey there python\"}"


@helloworld.route('/api')
def run_api():
    return "<h1> Hey there, it's API!"


if __name__ == '__main__':
    helloworld.run(host="0.0.0.0", port=int("3000"), debug=True)


# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/api")
# def hello_api():
#     return "<h1>Hey there, it's API!</h1>"
